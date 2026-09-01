from pyrogram import filters
from pyrogram.types import Message

from ThakurxMusic import app
from ThakurxMusic.utils.database import thumb_on, thumb_off
from ThakurxMusic.utils.decorators import AdminRightsCheck
from config import BANNED_USERS


@app.on_message(
    filters.command("thumb")
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def thumbnail_settings(
    client,
    message: Message,
    _,
    chat_id: int,
):
    # /thumb
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>ᴜsᴀɢᴇ :</b>\n\n"
            "<code>/thumb enable</code> - ᴛʜᴜᴍʙɴᴀɪʟ ᴏɴ\n"
            "<code>/thumb disable</code> - ᴛʜᴜᴍʙɴᴀɪʟ ᴏғғ\n\n"
            "<b>ᴀʟɪᴀs :</b>\n"
            "<code>/thumb on</code>\n"
            "<code>/thumb off</code>"
        )

    action = message.command[1].lower().strip()

    # Thumbnail ON
    if action in ("enable", "on"):
        await thumb_on(chat_id)

        return await message.reply_text(
            "<b>✅ ᴛʜᴜᴍʙɴᴀɪʟ ᴇɴᴀʙʟᴇᴅ</b>\n\n"
            "🎵 ɴᴏᴡ ᴘʟᴀʏɪɴɢ ᴍᴇssᴀɢᴇs ᴡɪʟʟ sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟs."
        )

    # Thumbnail OFF
    if action in ("disable", "off"):
        await thumb_off(chat_id)

        return await message.reply_text(
            "<b>❌ ᴛʜᴜᴍʙɴᴀɪʟ ᴅɪsᴀʙʟᴇᴅ</b>\n\n"
            "🎵 ɴᴏᴡ ᴘʟᴀʏɪɴɢ ᴍᴇssᴀɢᴇs ᴡɪʟʟ ɴᴏᴛ sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟs."
        )

    # Wrong argument
    return await message.reply_text(
        "<b>❌ ɪɴᴠᴀʟɪᴅ ᴏᴘᴛɪᴏɴ</b>\n\n"
        "<b>ᴜsᴇ :</b>\n"
        "<code>/thumb enable</code>\n"
        "<code>/thumb disable</code>\n\n"
        "<b>ᴏʀ :</b>\n"
        "<code>/thumb on</code>\n"
        "<code>/thumb off</code>"
    )
