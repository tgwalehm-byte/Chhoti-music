from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

spam_chats = []


async def is_admin(chat_id, user_id, client):
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in ["administrator", "owner"]


@Client.on_message(filters.command(["tagall", "all"]) & filters.group)
async def tag_all(client: Client, message: Message):
    chat_id = message.chat.id

    if not await is_admin(chat_id, message.from_user.id, client):
        return await message.reply_text("**Only admins can mention all!**")

    if chat_id in spam_chats:
        return await message.reply_text("**Tagall is already running in this chat.**")

    if message.reply_to_message and len(message.command) > 1:
        return await message.reply_text("**Reply to a message OR give text only, not both.**")

    if len(message.command) > 1:
        mode = "text"
        msg = message.text.split(None, 1)[1]
    elif message.reply_to_message:
        mode = "reply"
        msg = message.reply_to_message
    else:
        return await message.reply_text(
            "**Reply to a message or give me some text to tag everyone!**"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for member in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break

        if member.user.is_bot:
            continue

        usrnum += 1
        usrtxt += f"[{member.user.first_name}](tg://user?id={member.user.id}) "

        if usrnum == 5:
            if mode == "text":
                await client.send_message(chat_id, f"{msg}\n\n{usrtxt}")
            elif mode == "reply":
                await msg.reply_text(usrtxt)

            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""

    if usrtxt:
        if mode == "text":
            await client.send_message(chat_id, f"{msg}\n\n{usrtxt}")
        elif mode == "reply":
            await msg.reply_text(usrtxt)

    try:
        spam_chats.remove(chat_id)
    except:
        pass


@Client.on_message(filters.command("cancel") & filters.group)
async def cancel_tagall(client: Client, message: Message):
    chat_id = message.chat.id

    if not await is_admin(chat_id, message.from_user.id, client):
        return await message.reply_text("**Only admins can execute this command!**")

    if chat_id not in spam_chats:
        return await message.reply_text("**There is no ongoing tagall process...**")

    try:
        spam_chats.remove(chat_id)
    except:
        pass

    return await message.reply_text("**Stopped Mention All.**")
