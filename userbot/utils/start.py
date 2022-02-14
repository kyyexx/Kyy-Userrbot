from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot




async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/2b610c918dec590d2777b.jpg",
                caption="✨ **Kyy Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 5.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @NastyProject ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/NastySupportt"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
