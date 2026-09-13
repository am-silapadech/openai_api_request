import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Write a polite reply accepting an AI Engineer job offer."}
    ]
)

print(response.choices[0].message.content)

