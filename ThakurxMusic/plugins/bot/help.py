from typing import Union
import random

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, InputMediaPhoto

from ThakurxMusic import app
from ThakurxMusic.utils import help_pannel
from ThakurxMusic.utils.database import get_lang
from ThakurxMusic.utils.decorators.language import LanguageStart, languageCB
from ThakurxMusic.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, SHASHANK_PIC, SUPPORT_CHAT
from strings import get_string, helpers
from ThakurxMusic.utils.stuffs.buttons import BUTTONS
from ThakurxMusic.utils.stuffs.helper import Helper


# ==========================================================
# FIXED IMAGE FROM CONFIG
# ==========================================================

if isinstance(SHASHANK_PIC, (list, tuple)):
    START_IMAGE = SHASHANK_PIC[0]
else:
    START_IMAGE = SHASHANK_PIC


# ==========================================================
# MESSAGE EFFECTS
# ==========================================================

EFFECT_IDS = [
    5046509860389126442,
    5107584321108051014,
    5104841245755180586,
    5159385139981059251,
]


# ==========================================================
# PRIVATE HELP
# ==========================================================

@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("^settings_back_helper$") & ~BANNED_USERS)
async def helper_private(
    client: app,
    update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)

    if is_callback:
        try:
            await update.answer()
        except Exception:
            pass

        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)

        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard
        )

    else:
        try:
            await update.delete()
        except Exception:
            pass

        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)

        await update.reply_photo(
            photo=START_IMAGE,
            has_spoiler=True,
            message_effect_id=random.choice(EFFECT_IDS),
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


# ==========================================================
# GROUP HELP
# ==========================================================

@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)

    await message.reply_text(
        _["help_2"],
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==========================================================
# WELCOME HELP
# ==========================================================

@app.on_callback_query(filters.regex("^wel_cb$") & ~BANNED_USERS)
async def wel_cb(client, CallbackQuery):
    await CallbackQuery.answer()

    await CallbackQuery.edit_message_text(
        Helper.HELP_WEL,
        reply_markup=InlineKeyboardMarkup(BUTTONS.INFO_NEW)
    )


# ==========================================================
# VC LOGGER HELP
# ==========================================================

@app.on_callback_query(filters.regex("^vc_cb$") & ~BANNED_USERS)
async def vc_cb(client, CallbackQuery):
    await CallbackQuery.answer()

    await CallbackQuery.edit_message_text(
        Helper.HELP_VC,
        reply_markup=InlineKeyboardMarkup(BUTTONS.INFO_NEW)
    )


# ==========================================================
# THUMBNAIL HELP
# ==========================================================

@app.on_callback_query(filters.regex("^thumb_cb$") & ~BANNED_USERS)
async def thumb_cb(client, CallbackQuery):
    await CallbackQuery.answer()

    await CallbackQuery.edit_message_text(
        Helper.HELP_THUMB,
        reply_markup=InlineKeyboardMarkup(BUTTONS.INFO_NEW)
    )


# ==========================================================
# ABOUT BOT
# ==========================================================

@app.on_callback_query(filters.regex("^abot_cb$") & ~BANNED_USERS)
async def about_bot_cb(client, CallbackQuery):
    bot = await client.get_me()
    bot_mention = bot.mention

    await CallbackQuery.edit_message_text(
        Helper.HELP_ABOUT.format(bot_mention),
        reply_markup=InlineKeyboardMarkup(BUTTONS.INFO_BUTTON),
    )


# ==========================================================
# SUPPORT BOT
# ==========================================================

@app.on_callback_query(filters.regex("^sbot_cb$") & ~BANNED_USERS)
async def support_bot_cb(client, CallbackQuery):
    bot = await client.get_me()
    bot_mention = bot.mention

    await CallbackQuery.edit_message_text(
        Helper.HELP_SUPPORT.format(bot_mention),
        reply_markup=InlineKeyboardMarkup(BUTTONS.ABUTTON),
    )


# ==========================================================
# INFO BOT
# ==========================================================

@app.on_callback_query(filters.regex("^ibot_cb$") & ~BANNED_USERS)
async def info_bot_cb(client, CallbackQuery):
    bot = await client.get_me()
    bot_mention = bot.mention

    await CallbackQuery.edit_message_text(
        Helper.HELP_INFO.format(bot_mention),
        reply_markup=InlineKeyboardMarkup(BUTTONS.INFO_BUTTON),
    )


# ==========================================================
# BACK FROM ABOUT
# ==========================================================

@app.on_callback_query(filters.regex("^back_cb$") & ~BANNED_USERS)
async def back_cb(client, CallbackQuery):
    bot = await client.get_me()
    bot_mention = bot.mention

    await CallbackQuery.edit_message_media(
        media=InputMediaPhoto(
            media=START_IMAGE,
            has_spoiler=True,
            caption=Helper.HELP_ABOUT.format(bot_mention)
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS.INFO_BUTTON)
    )


# ==========================================================
# GENERAL HELP CALLBACKS
# ==========================================================

@app.on_callback_query(filters.regex("^help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):

    callback_data = CallbackQuery.data.strip()

    try:
        cb = callback_data.split(None, 1)[1]
    except (IndexError, AttributeError):
        return await CallbackQuery.answer(
            "ɪɴᴠᴀʟɪᴅ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ.",
            show_alert=True
        )

    keyboard = help_back_markup(_)

    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.HELP_1,
            reply_markup=keyboard
        )

    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.HELP_2,
            reply_markup=keyboard
        )

    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.HELP_3,
            reply_markup=keyboard
        )

    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.HELP_4,
            reply_markup=keyboard
        )

    elif cb == "hb5":
        await CallbackQuery.edit_message_text(
            helpers.HELP_5,
            reply_markup=keyboard
        )

    elif cb == "hb6":
        await CallbackQuery.edit_message_text(
            helpers.HELP_6,
            reply_markup=keyboard
        )

    elif cb == "hb7":
        await CallbackQuery.edit_message_text(
            helpers.HELP_7,
            reply_markup=keyboard
        )

    elif cb == "hb8":
        await CallbackQuery.edit_message_text(
            helpers.HELP_8,
            reply_markup=keyboard
        )

    elif cb == "hb9":
        await CallbackQuery.edit_message_text(
            helpers.HELP_9,
            reply_markup=keyboard
        )

    elif cb == "hb10":
        await CallbackQuery.edit_message_text(
            helpers.HELP_10,
            reply_markup=keyboard
        )

    elif cb == "hb11":
        await CallbackQuery.edit_message_text(
            helpers.HELP_11,
            reply_markup=keyboard
        )

    elif cb == "hb12":
        await CallbackQuery.edit_message_text(
            helpers.HELP_12,
            reply_markup=keyboard
        )

    elif cb == "hb13":
        await CallbackQuery.edit_message_text(
            helpers.HELP_13,
            reply_markup=keyboard
        )

    elif cb == "hb14":
        await CallbackQuery.edit_message_text(
            helpers.HELP_14,
            reply_markup=keyboard
        )

    elif cb == "hb15":
        await CallbackQuery.edit_message_text(
            helpers.HELP_15,
            reply_markup=keyboard
        )

    else:
        await CallbackQuery.answer(
            "ʜᴇʟᴘ ᴘᴀɢᴇ ɴᴏᴛ ғᴏᴜɴᴅ.",
            show_alert=True
    )
