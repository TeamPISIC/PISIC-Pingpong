import PingPongWr
import asyncio
from dotenv import load_dotenv
import os
import csv

load_dotenv()

url = os.environ.get('URL')
pingpong_token = os.environ.get('Authorization')

# 핑퐁 모듈 클래스 선언
Ping = PingPongWr.Connect(url, pingpong_token)

# 질문 데이터 가져오기
f = open('sampleData.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)


async def Example():
    for str_text in rdr:
        print(str_text)
        return_data = await Ping.Pong(session_id="Example", text=str_text, topic=False, image=False, dialog=False)
        print("피식이: " + return_data.get('text'))

asyncio.run(Example())

f.close()
