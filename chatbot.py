import PingPongWr
import asyncio
from dotenv import load_dotenv
import os
import csv
import pandas as pd

load_dotenv()

url = os.environ.get('URL')
pingpong_token = os.environ.get('Authorization')

# 핑퐁 모듈 클래스 선언
Ping = PingPongWr.Connect(url, pingpong_token)

# 질문 데이터 가져오기
f = open('sampleData.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)

result = []


async def getData():
    for str_text in rdr:
        return_data = await Ping.Pong(session_id="Example", text=str_text, topic=False, image=False, dialog=False)
        result.append([str_text[0], return_data.get('text')])

asyncio.run(getData())

f.close()

df = pd.DataFrame(result, columns=['Question', 'Answer'])
df.to_excel('result.xlsx', index=False)

print("챗봇 질문-답변 작업 완료!")
