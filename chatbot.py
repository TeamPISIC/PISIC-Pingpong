import requests

# 1. 헤더설정
header = {
    'Authorization': 'Basic a2V5OjRlYzg4MDBiOWIwMGRjOTBkODc3NGYwMDk2YTMzNmNl',  # 본인의 인증키를 적어야겠죠?
    'Content-Type': "application/json",
}

# 2. Request Body 설정
param = {
    "request": {
        "query": "안녕하세요"
    }
}

# 3. 주소설정
sessionId = "mySessionId"  # 본인의 Session Id를 적어주세요
url = 'https://builder.pingpong.us/api/builder/5ebe0072e4b0e921afb5c210/integration/v0.2/custom/' + sessionId

# 설정 끝 Request 날리기
req = requests.post(url, data=param, headers=header)

# Response 확인하기
data = req.json()
print(data)
