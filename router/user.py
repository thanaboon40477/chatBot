from fastapi import FastAPI, Request, Response, Body, HTTPException, APIRouter
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, CameraAction, QuickReply, QuickReplyButton, MessageAction
import json
import pyrebase
from flexmasage import *
from typing import Optional
from chatBot import chatBot

with open("config/db_firebase.json", encoding="utf8") as json_file:
    json_load = json.load(json_file)
    config = json_load['firebase']
    pb = pyrebase.initialize_app(config)
    db = pb.database()
    line_bot_api = LineBotApi(json_load["channelAccess"])
    handler = WebhookHandler(json_load["channelSecret"])

router = APIRouter()
app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@router.get('/index')
async def index(request: Request):
    return templates.TemplateResponse('index.html', context={'request':request})


@router.post('/chatbot')
async def chatbot(request: Request, raw_json:Optional[dict] = Body(None)):

    with open("log_line.json", "w") as data_line:
        json.dump(raw_json, data_line)
    
    json_line = json.dumps(raw_json)
    decoder =json.loads(json_line)

    try:
        no_event = len(decoder['events'])
        for i in range(no_event):
            event = decoder['events'][i]
            event_type(event)   

    except:
        event = decoder["events"][0]
        _type = event['type']
        if _type == "follow":
            # เก็บข้อมูลไว้ใน DataBase เมื่อ Follow
            userId = event['source']['userId']
            profile = line_bot_api.get_profile(userId)
            displayName = profile.display_name
            img = profile.picture_url
            status = profile.status_message
            interted = {"displayName": displayName, 'img':img, 'status': status, 'userId': userId}
            db.child('BotTest').push(interted)
        elif _type == "unfollow":
            # ลบข้อมูลของ user(Line) เมื่อ UnFollow
            userId = event['source']['userId']
            remove = db.child("BotTest").order_by_child('userId').equal_to(userId).get()
            remove = remove.val()
            print(remove)
            remove = remove.keys()
            for i in remove:
                db.child('BotTest').child(i).remove()

    signature = request.headers['X-Line-Signature']
    body = await request.body()
    print(signature)
      
    try:
        handler.handle(str(body, encoding="utf-8"), signature)
    except InvalidSignatureError as v:
        api_error = {'status_code': v.status_code, "message":v.message}
        raise HTTPException(status_code=400, detail=api_error)
    return raw_json

@handler.add(MessageEvent, message=TextMessage)
def message_type(event):
    # ตอบ user ที่ user พิมพ์เข้ามาเป็น Text
    # print(event)
    # texts = event['message']['type']
    texts = event.message.text
    print("Your Message :",texts)
    # userId = event_handler_add()[0]
    # print("Your UserId :",userId)
    replyToken = event.reply_token
    print("Your replyToken :",replyToken)
    # TextSendMessage(text= 'สวัสดี 😀')
    if texts == "ไง":
        line_bot_api.reply_message(replyToken, TextSendMessage(text='กรุณาเลือกหัวข้อ',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(image_url="https://media2.giphy.com/media/R3IxJW14a3QNa/giphy.gif?cid=ecf05e47ptuw3dl3x03u0i97mqhit3ryu9m5zipi90sokouz&rid=giphy.gif",action=MessageAction(label="สวัสดี", text="ยินดีต้อนรับ")),
                                  QuickReplyButton(image_url="https://static.wixstatic.com/media/afc648_7e70f2fcc96443efaa236f0fe18ac3d0~mv2.gif",action=CameraAction(label="ถ่ายภาพ"))
                               ])))
    if texts:
            word = chatBot(texts)
            line_bot_api.reply_message(replyToken, TextSendMessage(text=word))

def event_type(event):
    typeline = event['message']['type']
    replyToken = event['replyToken']
    if typeline == "sticker":
        userId = event['source']['userId']
        print("UserID :", userId)
        # line_bot_api.push_message(userId, StickerSendMessage(package_id='11537', sticker_id='52002746')
        line_bot_api.push_message(userId, StickerSendMessage(package_id='11537', sticker_id='52002746'))

    return event

@router.get('/lineliff')
def lineliff(request:Request):
        return templates.TemplateResponse('line.html', context={'request':request})

@router.post('/lineliff')
def lineliff(request:Request, raw_json:Optional[dict] = Body(None)):
        # เมื่อมีการ POST จะแสดง FlexMesseage ใน Line (LineLiff)
        event = raw_json
        firstname = event["firstname"]
        company = event["company"]
        tel = event["tel"]
        product = event["product"]
        image  = event["image"]
        linename = event["linename"]
        email = event["email"]
        userId = event["userId"]

        flexprofile = flexuser(image, linename, firstname, email, company, tel, product)
        line_bot_api.push_message(userId, flexprofile)
        return event

if __name__ == "__main__":
    uvicorn.run("app:app", debug=True)

    