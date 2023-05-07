from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOGGER_ID
from OpVirMusic import app


async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "Uɴᴋɴᴏᴡɴ Usᴇʀ"
        title = message.chat.title
        chat_id = message.chat.id
        chatusername = f"@{message.chat.username}" if message.chat.username else "Pʀɪᴠᴀᴛᴇ Cʜᴀᴛ"
        atiya = f"**~⟩ Nᴇᴡ Gʀᴏᴜᴘ #Aᴅᴅᴇᴅ Tᴏ Bᴏᴛ ✓**\n\n• Cʜᴀᴛ Tɪᴛʟᴇ ~ {title}\n• Cʜᴀᴛ Iᴅ ~ {chat_id} \n• Cʜᴀᴛ Lɪɴᴋ ~ {chatusername}\n• Aᴅᴅᴇᴅ Bʏ ~ {added_by}"
        await new_message(LOGGER_ID, atiya)
        with open('group_username.txt', 'w') as f:
            f.write(chatusername)


#-----------------@itz_rocks_krishna-----------------

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.left_chat_member]:
        randi = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        chat_id = message.chat.id
        with open('group_username.txt', 'r') as f:
            chatusername = f.read()
        atiya = f"#ʟᴇꜰᴛ ɢʀᴏᴜᴘ\n\nᴄʜᴀᴛ ɪᴅ : {chat_id}\nᴄʜᴀᴛ ᴛɪᴛʟᴇ : {title}\nᴄʜᴀᴛ ʟɪɴᴋ : {chatusername}\nʀᴇᴍᴏᴠᴇᴅ ʙʏ : {randi}"
        await new_message(LOGGER_ID, atiya)
        
#itz_rocks_krishna
