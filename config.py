import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)
GPT_API = os.getenv("GPT_API")

# Bot token and MongoDB URL fetched from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
MONGO_URL = os.getenv("MONGO_URL", None)

# Bot owner's Telegram user ID and username
OWNER_ID = os.getenv("OWNER_ID",7006715434)
OWNER_USERNAME = "Moonshining6"

# Support group and update channel names
SUPPORT_GROUP = "grandxmasti"
UPDATE_CHANNEL = "kittyxupdates"
