# ZauTeKm <https://t.me/ZauTeKm>
# @ZauTeKm

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from ZKSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ZKSongBot import Jebot as app
from ZKSongBot import LOGGER

pm_start_text = """
<b>Hi [{}](tg://user?id={}), I'm Song Downloader Bot.</b>

Send me /help for know my commands.

Mαde by😎 [@sparkysunny](https://t.me/sparkysunny/604)
"""

help_text = """
<b><u>Helpful Commands</u></b>
- /song <song name>: Download songs via Youtube
- /saavn : Download songs via JioSaavn
- /deezer : Download songs via Deezer

Mαde by😎 @sparkysunny
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('My group💗', url='https://t.me/animefan_club777'),
                    InlineKeyboardButton('My channel💗', url='https://t.me/moviesebseriesAnimes')
                  ],[
                    InlineKeyboardButton('Owner', url='https://t.me/cheater_01_02/604'),
                    InlineKeyboardButton('Helper1', url='https://t.me/Shoto_GirlFriend_777/604'),
                    InlineKeyboardButton('Helper2', url='https://t.me/Mochi875/604')
                  ],[
                    InlineKeyboardButton('✨Anime Wallpaper✨', url='https://t.me/Todoroki_Shoto_777')
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("ZKSongBot is online.")
idle()
