from pyrogram.enums import ParseMode

from EchoXMusic import app
from EchoXMusic.utils.database import is_on_off
from config import LOG_GROUP_ID


async def play_logs(message, streamtype):
    if not await is_on_off(2):
        return

    raw_text = message.text or message.caption or ""
    query_parts = raw_text.split(None, 1)
    query = query_parts[1] if len(query_parts) > 1 else "N/A"

    chat_name = message.chat.title or getattr(message.chat, "first_name", None) or "Unknown Chat"
    chat_username = (
        f"@{message.chat.username}" if getattr(message.chat, "username", None) else "N/A"
    )

    user_id = message.from_user.id if message.from_user else "N/A"
    user_mention = message.from_user.mention if message.from_user else "Unknown User"
    user_username = (
        f"@{message.from_user.username}"
        if message.from_user and message.from_user.username
        else "N/A"
    )

    logger_text = f"""
<b>{app.mention} play log</b>

<b>chat id :</b> <code>{message.chat.id}</code>
<b>chat name :</b> {chat_name}
<b>chat username :</b> {chat_username}

<b>user id :</b> <code>{user_id}</code>
<b>name :</b> {user_mention}
<b>username :</b> {user_username}

<b>query :</b> {query}
<b>streamtype :</b> {streamtype}"""

    if message.chat.id != LOG_GROUP_ID:
        try:
            await app.send_message(
                chat_id=LOG_GROUP_ID,
                text=logger_text,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        except Exception:
            pass
