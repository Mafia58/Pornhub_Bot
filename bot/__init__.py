from pyrogram import Client
from os import getenv
from config import Config
from helpers import download_progress_hook

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
SQL_DB = getenv("SQL_DB")
SUDO_ID = getenv("SUDO_ID")
SUDO = [int(x) for x in SUDO_ID.split()]
MONGODB = getenv("MONGODB")
OWNER = SUDO_ID

app = Client("pornhub_bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN)
