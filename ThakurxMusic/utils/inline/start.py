from pyrogram.types import InlineKeyboardButton

import config
from ThakurxMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="˹ sυᴘᴘσʀᴛ ˼",
                callback_data="purvi_scb",
            ),
            InlineKeyboardButton(
                text="🌐 Lᴀɴɢᴜᴀɢᴇ",
                callback_data="LG",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
