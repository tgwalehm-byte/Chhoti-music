from pyrogram import enums, types


def InlineKeyboardButton(*args, **kwargs):
    """Create styled inline buttons using Kurigram ButtonStyle."""
    if "style" not in kwargs:
        text = str(kwargs.get("text", args[0] if args else "")).lower()
        callback = str(kwargs.get("callback_data", "")).lower()

        if (
            any(word in text for word in ("back", "ʙᴧᴄᴋ", "ʙᴀᴄᴋ"))
            or "back" in callback
        ):
            style = enums.ButtonStyle.PRIMARY
        elif (
            any(word in text for word in ("close", "ᴄʟᴏsᴇ", "cancel"))
            or any(word in callback for word in ("close", "cancel"))
        ):
            style = enums.ButtonStyle.DANGER
        else:
            style = enums.ButtonStyle.SUCCESS

        kwargs["style"] = style

    return types.InlineKeyboardButton(*args, **kwargs)
