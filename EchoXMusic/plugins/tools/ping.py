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


from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from EchoXMusic import app
from EchoXMusic.core.call import Nand
from EchoXMusic.utils import bot_sys_stats
from EchoXMusic.utils.decorators.language import language
from EchoXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    try:
        response = await message.reply_photo(
            photo=PING_IMG_URL,
            caption=_["ping_1"].format(app.mention),
        )
    except Exception:
        response = await message.reply_text(_["ping_1"].format(app.mention))
    pytgping = await Nand.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )


# ©️ Copyright Reserved - @OGAbdulOfficial  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @OGAbdulOfficial)
# 🔗 GitHub : https://github.com/OGAbdulOfficial/EchoXMusic
# 📢 Telegram Channel : https://t.me/AbdulBotzOfficial
# ===========================================


# ❤️ Love From EchoXMusic 
