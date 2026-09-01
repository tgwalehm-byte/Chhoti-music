from ThakurxMusic.utils.styled_button import InlineKeyboardButton
from pyrogram import filters
from pyrogram.types import (
    InputMediaVideo,
    InlineKeyboardMarkup,
)

from ThakurxMusic import app


@app.on_callback_query(filters.regex("^gib_source$"))
async def gib_repo_callback(_, callback_query):
    await callback_query.answer()

    await callback_query.edit_message_media(
        media=InputMediaVideo(
            "https://telegra.ph/file/b1367262cdfbcd0b2af07.mp4",
            has_spoiler=True,
            caption=(
                "<b>✦ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ</b>\n\n"
                "⊚ Cʟɪᴄᴋ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tᴏ Gᴇᴛ Tʜᴇ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ."
            ),
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="• ʙᴀᴄᴋ •",
                        callback_data="settingsback_helper",
                    ),
                    InlineKeyboardButton(
                        text="• ᴄʟᴏsᴇ •",
                        callback_data="close",
                    ),
                ]
            ]
        ),
    )
