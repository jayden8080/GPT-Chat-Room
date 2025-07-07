import openai
from openai import OpenAI

client = OpenAI(
    api_key=""
)

respons = client.responses.create(
    model="gpt-4o-2024-05-13",
    input = "한글로 반갑게 나한테 인사해줘."
)

print(respons.output_text)


