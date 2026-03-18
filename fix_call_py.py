import re
with open(r'EchoXMusic\core\call.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Imports
text = text.replace(
    'from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped',
    'from pytgcalls.types import MediaStream'
)
text = text.replace(
    'from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo',
    '# obsolete import'
)

# 2. parameters
text = text.replace('additional_ffmpeg_parameters=', 'ffmpeg_parameters=')
text = text.replace('audio_parameters=HighQualityAudio(),\n', '')
text = text.replace('audio_parameters=HighQualityAudio(),', '')
text = text.replace('video_parameters=MediumQualityVideo(),\n', '')
text = text.replace('video_parameters=MediumQualityVideo(),', '')
text = text.replace('audio_parameters=HighQualityAudio()\n', '')
text = text.replace('audio_parameters=HighQualityAudio()', '')

# 3. Class Names
text = text.replace('AudioVideoPiped(', 'MediaStream(')
text = text.replace('AudioPiped(', 'MediaStream(')

# write it back
with open(r'EchoXMusic\core\call.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Replacements done")
