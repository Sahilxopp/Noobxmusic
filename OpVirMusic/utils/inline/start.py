from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=" Hᴇʟᴩ ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text=" Sᴇᴛᴛɪɴɢs ", callback_data="settings_helper"
            )
        ],
        [   
            InlineKeyboardButton(
                text="Rᴀɴᴀ [🇮🇳]", user_id=OWNER
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴩ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="Rᴀɴᴀ", user_id=OWNER
            )
        ],
        [    
            InlineKeyboardButton(
                text="Sᴏᴜʀᴄᴇ", url="https://te.legra.ph/file/5fa7b4d86dcd5720ef30c.mp4"
            ),
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇs", url=config.SUPPORT_CHANNEL
            )   
        ],
     ]
    return buttons
