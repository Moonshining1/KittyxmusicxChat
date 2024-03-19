import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("API_ID", None)
API_HASH = os.getenv("API_HASH", None)

# Bot token and MongoDB URL fetched from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
MONGO_URL = os.getenv("MONGO_URL", None)

# Bot owner's Telegram user ID and username
OWNER_ID = os.getenv("OWNER_ID",7157587567)
OWNER_USERNAME = "JARVIS_V2"

# Support group and update channel names
SUPPORT_GROUP = "CHATTING_2024"
UPDATE_CHANNEL = "JARVIS_X_SUPPORT"