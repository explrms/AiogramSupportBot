import os
from dotenv import load_dotenv

load_dotenv()

# Bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')
SUPPORT_CHAT_ID = int(os.getenv('SUPPORT_CHAT_ID'))
