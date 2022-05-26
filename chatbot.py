import PingPongWr
import asyncio

from dotenv import load_dotenv
import os

load_dotenv()

url = os.environ.get('URL')
pingpong_token = os.environ.get('Authorization')

# 핑퐁 모듈 클래스 선언
Ping = PingPongWr.Connect(url, pingpong_token)


async def Example():
    while True:
        str_text = input("입력: ")
        if str_text == "끝내기":
            break
        return_data = await Ping.Pong(session_id="Example", text=str_text, topic=False, image=False, dialog=False)
        print("피식이: " + return_data.get('text'))

asyncio.run(Example())
