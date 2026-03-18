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


from pyrogram.types import InlineKeyboardButton as Ikb, InlineKeyboardMarkup

class InlineKeyboard(InlineKeyboardMarkup):
    def __init__(self, row_width=2):
        self.row_width = row_width
        super().__init__(inline_keyboard=[])

    def add(self, *args):
        for i in range(0, len(args), self.row_width):
            self.inline_keyboard.append(list(args[i:i + self.row_width]))
        return self

    def row(self, *args):
        self.inline_keyboard.append(list(args))
        return self

from .functions import get_urls_from_text as is_url


def keyboard(buttons_list, row_width: int = 2):
    buttons = InlineKeyboard(row_width=row_width)
    data = [
        (
            Ikb(text=str(i[0]), callback_data=str(i[1]))
            if not is_url(i[1])
            else Ikb(text=str(i[0]), url=str(i[1]))
        )
        for i in buttons_list
    ]
    buttons.add(*data)
    return buttons


def ikb(data: dict, row_width: int = 2):
    return keyboard(data.items(), row_width=row_width)


# ©️ Copyright Reserved - @OGAbdulOfficial  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @OGAbdulOfficial)
# 🔗 GitHub : https://github.com/OGAbdulOfficial/EchoXMusic
# 📢 Telegram Channel : https://t.me/AbdulBotzOfficial
# ===========================================


# ❤️ Love From EchoXMusic 
