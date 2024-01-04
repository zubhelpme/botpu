# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Zo7uhKbzTTn6wt3NGZlwKWl6XYumt0bUIEOmifQjMQnxByNCpS4xUlSr9S8fSse2au6u99vluA+JsGySYtgpOzhadnk7QtSlpjGef2K3ySriadx4Vb0MAIHgRAN3d/pNmEObbMHrwpgNTvnTA8dqAAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('164a6d03a1c0aae498d8eae9a00e19c7')

line_bot_api.push_message('U49dc41cd7de29de6c36b346b105c0432', TemplateSendMessage(
    alt_text='ButtonsTemplate',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/ZHf1apg.jpg',
        title='寵物用品公司',
        text='寵物用品公司購買網站',
        actions=[
            URIAction(
                lable='官方網站',
                uri='https://chongwuyongpinzhuanmai.webnode.tw/'
            ),
            URIAction(
                lable='狗狗用品',
                uri='https://chongwuyongpinzhuanmai.webnode.tw/%e7%8b%97%e7%8b%97%e7%94%a2%e5%93%81/'
            ),
            URIAction(
                lable='貓貓用品',
                uri='https://chongwuyongpinzhuanmai.webnode.tw/%e8%b2%93%e5%92%aa%e7%94%a2%e5%93%81/'
            )
        ]
    )
))

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=message)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)