import asyncio
import glob
import os
import re
from typing import Union
import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from EchoXMusic.utils.formatters import time_to_seconds
import aiohttp
from EchoXMusic import LOGGER

try:
    from py_yt import VideosSearch
except ImportError:
    from youtubesearchpython.__future__ import VideosSearch

API_URL = "https://abdulbotz.site"


def _download_with_ytdlp(link: str, video_id: str, as_video: bool) -> str | None:
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    # Clean up stale files for this id so we can resolve the final output path reliably.
    for stale in glob.glob(os.path.join(download_dir, f"{video_id}.*")):
        try:
            os.remove(stale)
        except OSError:
            pass

    outtmpl = os.path.join(download_dir, f"{video_id}.%(ext)s")
    if as_video:
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "outtmpl": outtmpl,
            "merge_output_format": "mp4",
            "noplaylist": True,
            "nocheckcertificate": True,
            "extractor_args": {"youtube": {"player_client": ["mweb", "web", "android"]}},
            "sleep_interval_requests": 1,
        }
        if os.path.exists("cookies.txt"):
            ydl_opts["cookiefile"] = "cookies.txt"
    else:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": outtmpl,
            "quiet": True,
            "noplaylist": True,
            "nocheckcertificate": True,
            "extractor_args": {"youtube": {"player_client": ["mweb", "web", "android"]}},
            "sleep_interval_requests": 1,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        if os.path.exists("cookies.txt"):
            ydl_opts["cookiefile"] = "cookies.txt"

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except Exception as exc:
        LOGGER(__name__).warning("yt-dlp fallback failed for %s: %s", video_id, exc)
        return None

    for candidate in glob.glob(os.path.join(download_dir, f"{video_id}.*")):
        if os.path.isfile(candidate) and os.path.getsize(candidate) > 0:
            return candidate
    return None

async def download_song(link: str) -> str:
    video_id = link.split('v=')[-1].split('&')[0] if 'v=' in link else link

    if not video_id or len(video_id) < 3:
        return None

    DOWNLOAD_DIR = "downloads"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp3")

    if os.path.exists(file_path):
        return file_path

    try:
        async with aiohttp.ClientSession() as session:
            params = {"url": video_id, "type": "audio"}

            async with session.get(
                f"{API_URL}/download",
                params=params,
                timeout=aiohttp.ClientTimeout(total=15)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    download_token = data.get("download_token")

                    if download_token:
                        stream_url = f"{API_URL}/stream/{video_id}?type=audio&token={download_token}"

                        async with session.get(
                            stream_url,
                            timeout=aiohttp.ClientTimeout(total=300)
                        ) as file_response:
                            if file_response.status == 302:
                                redirect_url = file_response.headers.get('Location')
                                if redirect_url:
                                    async with session.get(redirect_url) as final_response:
                                        if final_response.status == 200:
                                            with open(file_path, "wb") as f:
                                                async for chunk in final_response.content.iter_chunked(16384):
                                                    f.write(chunk)
                                            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                                                return file_path
                            elif file_response.status == 200:
                                with open(file_path, "wb") as f:
                                    async for chunk in file_response.content.iter_chunked(16384):
                                        f.write(chunk)
                                if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                                    return file_path

    except Exception:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass
        return await asyncio.to_thread(_download_with_ytdlp, link, video_id, False)

    return await asyncio.to_thread(_download_with_ytdlp, link, video_id, False)

async def download_video(link: str) -> str:
    video_id = link.split('v=')[-1].split('&')[0] if 'v=' in link else link

    if not video_id or len(video_id) < 3:
        return None

    DOWNLOAD_DIR = "downloads"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp4")

    if os.path.exists(file_path):
        return file_path

    try:
        async with aiohttp.ClientSession() as session:
            params = {"url": video_id, "type": "video"}

            async with session.get(
                f"{API_URL}/download",
                params=params,
                timeout=aiohttp.ClientTimeout(total=15)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    download_token = data.get("download_token")

                    if download_token:
                        stream_url = f"{API_URL}/stream/{video_id}?type=video&token={download_token}"

                        async with session.get(
                            stream_url,
                            timeout=aiohttp.ClientTimeout(total=600)
                        ) as file_response:
                            if file_response.status == 302:
                                redirect_url = file_response.headers.get('Location')
                                if redirect_url:
                                    async with session.get(redirect_url) as final_response:
                                        if final_response.status == 200:
                                            with open(file_path, "wb") as f:
                                                async for chunk in final_response.content.iter_chunked(16384):
                                                    f.write(chunk)
                                            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                                                return file_path
                            elif file_response.status == 200:
                                with open(file_path, "wb") as f:
                                    async for chunk in file_response.content.iter_chunked(16384):
                                        f.write(chunk)
                                if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                                    return file_path

    except Exception:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass
        return await asyncio.to_thread(_download_with_ytdlp, link, video_id, True)

    return await asyncio.to_thread(_download_with_ytdlp, link, video_id, True)

async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz:
        if "unavailable videos are hidden" in (errorz.decode("utf-8")).lower():
            return out.decode("utf-8")
        else:
            return errorz.decode("utf-8")
    return out.decode("utf-8")

class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        return text[entity.offset: entity.offset + entity.length]
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        return None

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        
        try:
            results = VideosSearch(link, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration_min = result["duration"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                vidid = result["id"]
                duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
            return title, duration_min, duration_sec, thumbnail, vidid
        except Exception as e:
            LOGGER(__name__).warning(f"VideosSearch failed for {link}: {e}. Falling back to yt-dlp.")
            # Fallback to yt-dlp for details
            try:
                ydl_opts = {
                    "quiet": True, 
                    "no_warnings": True, 
                    "extractor_args": {"youtube": {"player_client": ["mweb", "web", "android"]}},
                    "sleep_interval_requests": 1,
                }
                if os.path.exists("cookies.txt"):
                    ydl_opts["cookiefile"] = "cookies.txt"
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=False)
                    title = info.get("title")
                    duration_sec = info.get("duration", 0)
                    duration_min = str(duration_sec // 60).zfill(2) + ":" + str(duration_sec % 60).zfill(2)
                    thumbnail = info.get("thumbnail")
                    vidid = info.get("id")
                    return title, duration_min, duration_sec, thumbnail, vidid
            except Exception as ex:
                LOGGER(__name__).error(f"yt-dlp details fallback failed for {link}: {ex}")
                raise ex

    async def title(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["title"]

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["duration"]

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["thumbnails"][0]["url"].split("?")[0]

    async def video(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        try:
            downloaded_file = await download_video(link)
            if downloaded_file:
                return 1, downloaded_file
            else:
                return 0, "Video download failed"
        except Exception as e:
            return 0, f"Video download error: {e}"

    async def playlist(self, link, limit, user_id, videoid: Union[bool, str] = None):
        if videoid:
            link = self.listbase + link
        if "&" in link:
            link = link.split("&")[0]
        playlist = await shell_cmd(
            f"yt-dlp -i --get-id --flat-playlist --playlist-end {limit} --skip-download {link}"
        )
        try:
            result = [key for key in playlist.split("\n") if key]
        except:
            result = []
        return result

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            vidid = result["id"]
            yturl = result["link"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        track_details = {
            "title": title,
            "link": yturl,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumb": thumbnail,
        }
        return track_details, vidid

    async def formats(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        ytdl_opts = {"quiet": True}
        ydl = yt_dlp.YoutubeDL(ytdl_opts)
        with ydl:
            formats_available = []
            r = ydl.extract_info(link, download=False)
            for format in r["formats"]:
                try:
                    if "dash" not in str(format["format"]).lower():
                        formats_available.append(
                            {
                                "format": format["format"],
                                "filesize": format.get("filesize"),
                                "format_id": format["format_id"],
                                "ext": format["ext"],
                                "format_note": format["format_note"],
                                "yturl": link,
                            }
                        )
                except:
                    continue
        return formats_available, link

    async def slider(self, link: str, query_type: int, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        a = VideosSearch(link, limit=10)
        result = (await a.next()).get("result")
        title = result[query_type]["title"]
        duration_min = result[query_type]["duration"]
        vidid = result[query_type]["id"]
        thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
        return title, duration_min, thumbnail, vidid

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> str:
        if videoid:
            link = self.base + link

        try:
            if video:
                downloaded_file = await download_video(link)
            else:
                downloaded_file = await download_song(link)
            
            if downloaded_file:
                return downloaded_file, True
            else:
                return None, False
        except Exception:
            return None, False
