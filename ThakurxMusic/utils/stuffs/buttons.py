from pyrogram.types import InlineKeyboardMarkup, Message
from ThakurxMusic.utils.styled_button import InlineKeyboardButton
from pyrogram import Client, filters, enums 
import config

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/BOTxBOOSTER"),
        InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/BOTxBOOSTER")
    ],
    [
        InlineKeyboardButton("˹ ❍ᴡηєʀ ˼", user_id=config.OWNER_ID),
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settingsback_helper")
    ]
]

    INFO_BUTTON = [
    [
        InlineKeyboardButton("˹ ʀєᴘσ ˼", callback_data="gib_source"),
        InlineKeyboardButton("˹ ʏᴛ-ᴀᴘɪ ˼", callback_data="bot_info_data"),
        InlineKeyboardButton("˹ ʟᴧηɢᴜᴧɢє ˼", callback_data="LG"),
    ],
    [
        
        InlineKeyboardButton("˹ ᴘʀɪᴠᴧᴄʏ ˼", url="https://telegra.ph/Privacy-Policy--Purvi-Bots-by-ALPHA-BABY-08-06"),
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settingsback_helper"),
    ]
    ]
    


    INFO_NEW = [
    [
        InlineKeyboardButton("• ʙᴧᴄᴋ •", callback_data="settings_back_helper")],
    ]
    
    
