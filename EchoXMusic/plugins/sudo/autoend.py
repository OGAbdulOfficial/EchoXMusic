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


from pyrogram import filters
from pyrogram.types import Message

from EchoXMusic import app
from EchoXMusic.misc import SUDOERS
from EchoXMusic.utils.database import autoend_off,autoend_on,autoleave_off, autoleave_on,is_autoend,is_autoleave


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    zerostate = await is_autoend()
    usage = f"<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]\n\n Current state : {zerostate}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state in ["enable","on","yes"]:
        await autoend_on()
        await message.reply_text(
            "» ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴇɴᴀʙʟᴇᴅ.\n\nᴀssɪsᴛᴀɴᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀғᴛᴇʀ ғᴇᴡ ᴍɪɴs ᴡʜᴇɴ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ."
        )
    elif state in ["disable","off","no"]:
        await autoend_off()
        await message.reply_text("» ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴅɪsᴀʙʟᴇᴅ.")
    else:
        await message.reply_text(usage)

@app.on_message(filters.command("autoleave") & SUDOERS)
async def auto_leave_chat(_, message: Message):
    zerostate = await is_autoleave()
    usage = f"<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoleave [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]\n\n Current state : {zerostate}"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state in ["enable","on","yes"]:
        await autoleave_on()
        await message.reply_text(
            "» ᴀᴜᴛᴏ leave chat ᴇɴᴀʙʟᴇᴅ.\n\nᴀssɪsᴛᴀɴᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀғᴛᴇʀ ғᴇᴡ ᴍɪɴs ᴡʜᴇɴ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ."
        )
    elif state in ["disable","off","no"]:
        await autoleave_off()
        await message.reply_text("» ᴀᴜᴛᴏ leave chat ᴅɪsᴀʙʟᴇᴅ.")
    else:
        await message.reply_text(usage)
        


# ©️ Copyright Reserved - @OGAbdulOfficial  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @OGAbdulOfficial)
# 🔗 GitHub : https://github.com/OGAbdulOfficial/EchoXMusic
# 📢 Telegram Channel : https://t.me/AbdulBotzOfficial
# ===========================================


# ❤️ Love From EchoXMusic 
