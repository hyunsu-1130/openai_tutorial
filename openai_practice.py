from dotenv import load_dotenv
import os
from openai import OpenAI

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옵니다.
openai_api_key = os.getenv("OPENAI_API_KEY")

# API 키를 출력하여 확인합니다. 실제 사용시에는 출력하지 않도록 주의하세요.
# print(openai_api_key)

# 이 API 키를 사용하여 OpenAI API 등에 요청을 보낼 수 있습니다.

client = OpenAI(api_key=openai_api_key)

MODEL = "gpt-3.5-turbo-1106"

response = client.chat.completions.create(
  model=MODEL,
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "너는 고객의 만족도를 분석하는 로봇이야. 고객의 응답내용을 토대로 만족 또는 불만족을 구분해줘. You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "오늘 구매한 컴퓨터는 소음이 심하고 가격에 비해서 느린 것 같아"},
  ]
)

print(response.choices[0].message.content)