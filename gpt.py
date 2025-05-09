import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def ask_gpt(message_history):
    response = client.chat.completions.create(
        model="openai/gpt-4o",
        messages=message_history,
        temperature=0.7,
    )
    return response.choices[0].message.content
