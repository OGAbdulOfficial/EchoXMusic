# Authored By EchoX Networks © 2025
import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnnieXMedia import LOGGER, app, userbot
from AnnieXMedia.core.call import StreamController
from AnnieXMedia.misc import sudo
from AnnieXMedia.plugins import ALL_MODULES
from AnnieXMedia.utils.database import get_banned_users, get_gbanned
from AnnieXMedia.utils.cookie_handler import fetch_and_store_cookies
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ᴀssɪsᴛᴀɴᴛ sᴇssɪᴏɴ ɴᴏᴛ ғɪʟʟᴇᴅ, ᴘʟᴇᴀsᴇ ғɪʟʟ ᴀ ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ...")
        exit()

    # ✅ Try to fetch cookies at startup
    try:
        await fetch_and_store_cookies()
        LOGGER("EchoXMusic").info("YouTube cookies loaded successfully ✅")
    except Exception as e:
        LOGGER("EchoXMusic").warning(f"⚠️ Cookie error: {e}")


    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AnnieXMedia.plugins" + all_module)

    LOGGER("EchoXMusic.plugins").info("EchoXMusicBot's modules loaded...")

    await userbot.start()
    await StreamController.start()

    try:
        await StreamController.stream_call("http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4")
    except NoActiveGroupCall:
        LOGGER("EchoXMusic").error(
            "Please turn on the voice chat of your log group/channel.\n\nEchoXMusicBot stopped..."
        )
        exit()
    except:
        pass

    await StreamController.decorators()
    LOGGER("EchoXMusic").info("EchoXMusicBot started successfully.")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("EchoXMusic").info("Stopping EchoXMusicBot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
