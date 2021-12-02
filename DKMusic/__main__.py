import requests
from pyrogram import Client as Bot

from DKMusic.config import API_HASH
from DKMusic.config import API_ID
from DKMusic.config import BG_IMAGE
from DKMusic.config import BOT_TOKEN
from DKMusic.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DKMusic.modules"),
)

bot.start()
run()
