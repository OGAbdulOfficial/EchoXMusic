# Copyright (c) 2025 Nand Yaduwanshi <OGAbdulOfficial>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


from EchoXMusic.core.bot import Nand
from EchoXMusic.core.dir import dirr
from EchoXMusic.core.git import git
from EchoXMusic.core.userbot import Userbot
from EchoXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Nand()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()


# ©️ Copyright Reserved - @OGAbdulOfficial  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @OGAbdulOfficial)
# 🔗 GitHub : https://github.com/OGAbdulOfficial/EchoXMusic
# 📢 Telegram Channel : https://t.me/AbdulBotzOfficial
# ===========================================


# ❤️ Love From EchoXMusic 
