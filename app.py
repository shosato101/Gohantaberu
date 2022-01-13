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

app = Flask(__name__)

line_bot_api = LineBotApi('VesLcVYuxdpH+o/mcgIybSjqFA5IhxOXlloAT2MQXT2NEKCWV8LZ8i0ZDk37/N1pL0RD4nXvGtbFnX2vGkb4O2Kgk7AAOZDLyeqwowgZrNd7rFSUAABkBVx7L0eh6zWIj5HOpi7Br2HBLU4xI6iefAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('929e793e95704e31010b645aa0d3e31c')

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
#    keyword = event.message.text
    reccomend = ""
    hit = ""

    pickup.pickup_datas(event.message.text)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"{reccomend}"))

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"全{hit}件"))

if __name__ == "__main__":
        app.run()
