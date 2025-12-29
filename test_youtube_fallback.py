import asyncio
from AnnieXMedia.platforms.Youtube import YouTubeAPI

async def run_test(queries):
    api = YouTubeAPI()
    for q in queries:
        print("---\nQuery:", q)
        try:
            details, vid = await api.track(q)
            print("Result id:", vid)
            print("Title:", details.get("title"))
            print("Thumb:", details.get("thumb"))
        except Exception as e:
            print("Error:", repr(e))

if __name__ == "__main__":
    queries = [
        "MAQAMAT/SUBLIME BRILLIANCE | Surah At-Tawba | سورة ٱلتوبة (كاملة) | Yasser Al Dosari | ياسرالدوسري",
        "Zara Zara Bahekta Hai | JalRaj",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    ]
    asyncio.run(run_test(queries))
