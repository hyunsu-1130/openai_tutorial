from dotenv import load_dotenv
import os
from PIL import Image
import requests
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "dall-e-3"

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
  model=MODEL,
  prompt="아주 맛있게 익은 오렌지와 사과를 먹는 꼬마 남자 아이를 그려줘",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
# print(image_url)

# 저장 파일 이름 설정
filename = 'image.jpg'
response = requests.get(image_url)
with open(filename, 'wb') as f:
  f.write(response.content)
Image.open(filename)