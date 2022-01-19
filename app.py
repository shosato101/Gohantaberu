from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


import pickup
import config

app = Flask(__name__)

LINE_BOT_API_KEY = config.LINE_BOT_API_KEY
LINE_WEBHOOK_HANDLER = config.LINE_WEBHOOK_HANDLER

line_bot_api = LineBotApi(LINE_BOT_API_KEY)
handler = WebhookHandler(LINE_WEBHOOK_HANDLER)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 全角スペースを半角にするため
    word = event.message.text
    keywords = word.replace("　", " ")

    recommendation = pickup.Reccomend(keywords)
    reccomend = recommendation.pickup_datas()

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reccomend))

    # line_bot_api.reply_message(
        # event.reply_token,
        # TextSendMessage(text=f"全{hit}件"))

if __name__ == "__main__":
        app.run()
