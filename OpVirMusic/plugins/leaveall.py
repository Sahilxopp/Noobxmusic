import config
import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from OpVirMusic import app, userbot as app2
from config import OWNER_ID as OWNER, SUPPORT_GROUP as SUNAME


@app.on_message(filters.command(["leaveall", "assleaveall"]) & filters.user(OWNER))
async def ass_leaveall(_, message: Message):
    lear = await message.reply_text(f"» {app2.one.name} sᴛᴀʀᴛᴇᴅ ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛs...")
    left = 0
    failed = 0
    chats = []
    async for dialog in app2.one.iter_dialogs():
        chats.append(int(dialog.chat.id))
    schat = (await app.get_chat(SUNAME)).id
    for i in chats:
        if i in (config.LOGGER_ID, int(schat)):
            continue
        try:
            await app2.one.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
            failed += 1
    try:
        await lear.edit_text(f"<u>**» {app2.one.name} sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :**</u>\n\n**ʟᴇғᴛ :** `{left}`\n**ғᴀɪʟᴇᴅ :** `{failed}`")
    except:
        await message.reply_text(f"<u>**» {app2.one.name} sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :**</u>\n\n**ʟᴇғᴛ :** `{left}`\n**ғᴀɪʟᴇᴅ :** `{failed}`")
