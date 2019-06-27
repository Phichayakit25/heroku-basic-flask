import json
import requests
from flask import Flask, request, abort

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_channel_access_token = '+KFVmAgqGF06XRdrtHTUwKXZfdZ3EOsXWoX3mliWdQrxSA5xph14V4a9M1Ji+KBtoPtdZDwl9ivMmw5nZC0GlP7du75Via+7Ei1RYzQIZmgU8mklQhTMb2bus3cHSbtMX+gJqBpuyMpGKk3djismMwdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(line_channel_access_token)
Authorization = "Bearer {}".format(line_channel_access_token)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    body = json.loads(body)
    print (body)

    reply_token = body['events'][0]["replyToken"]
    print("reply_token: {}".format(reply_token))

    event_type = body['events'][0]['type']
    print("event_type: {}".format(event_type))

    if event_type == "message":
        message_type = body['events'][0]['message']['type']
        # print("message_type: {}".format(message_type))
        if message_type == "text":
            text = body['events'][0]['message']['text']
            print("text: {}".format(text))
            if "home" in text or "Home" in text:
                print("replying text:{}".format(text))
                reply_menu(reply_token)

    return '',200

def reply_menu(reply_token):
    response = requests.post(
        url="https://api.line.me/v2/bot/message/reply",
        headers={
            "Content-Type": "application/json",
            "Authorization": Authorization,
        },
        data=json.dumps({
            "replyToken": str(reply_token),
            "messages": [{
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
    "type": "carousel",
    "actions": [],
    "columns": [
      {
        "thumbnailImageUrl": "https://sv1.picz.in.th/images/2019/06/27/1CCpqZ.th.jpg",
        "text": "weather",
        "actions": [
          {
            "type": "message",
            "label": "weather",
            "text": "weather"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://d3n8a8pro7vhmx.cloudfront.net/edonsw/pages/995/attachments/original/1386210667/green_energy_320.jpg",
        "text": "energy",
        "actions": [
          {
            "type": "message",
            "label": "energy",
            "text": "energy"
          }
        ]
      },
              "thumbnailImageUrl": "https://m.media-amazon.com/images/M/MV5BYWU4YjAzNzctMmUzZi00MTliLWE2MGEtZWIwODdiMWE4ZjlkXkEyXkFqcGdeQXVyMjA4OTI5NDQ@._V1_.jpg",
              "text": "booty",
              "actions": [
                {
                  "type": "message",
                  "label": "booty",
                  "text": "booty"
    ]
  }
}]
        })
    )

if __name__ == "__main__":
    app.run()
