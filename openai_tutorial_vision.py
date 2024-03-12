from dotenv import load_dotenv
import os
from PIL import Image
import requests
from openai import OpenAI

# 웹 상에 있는 이미지 사용

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4-vision-preview"

client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model=MODEL,
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 이미지는 무슨 내용이니?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_DH91p8tc-ngQO01c4PcVofIO0cofedJVpw&usqp=CAU",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])