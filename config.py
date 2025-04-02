import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMIN_CHAT_ID = str(os.getenv("ADMIN_CHAT_ID"))
