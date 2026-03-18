import asyncio
import inspect
async def main():
    from pytgcalls.types import MediaStream
    from pytgcalls.types import AudioQuality
    from pytgcalls.types import VideoQuality
    print("MediaStream signature:", inspect.signature(MediaStream.__init__))
asyncio.run(main())
