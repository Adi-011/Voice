import os
import openai
from openai import OpenAI
client = xyz

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "write email for resignation\n"
    },
    {
      "role": "user",
      "content": "how are you "
    },
    {
      "role": "assistant",
      "content": "i am fine"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
