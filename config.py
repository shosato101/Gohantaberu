from dotenv import load_dotenv
load_dotenv()

import os
HOTPEPPER_API_KEY = os.getenv('HOTPEPPER_API_KEY')
LINE_BOT_API_KEY = os.getenv('LINE_BOT_API_KEY')
LINE_WEBHOOK_HANDLER = os.getenv('LINE_WEBHOOK_HANDLER')
