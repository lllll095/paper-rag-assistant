import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_PATH)

api_key = os.getenv("DASHSCOPE_API_KEY")
base_url = os.getenv("LLM_BASE_URL")
model = os.getenv("LLM_MODEL", "qwen-plus")

if not api_key:
    raise ValueError("DASHSCOPE_API_KEY is not set. Please check your .env file.")

if not base_url:
    raise ValueError("LLM_BASE_URL is not set. Please check your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain retrieval-augmented generation in one sentence."},
    ],
)

print(response.choices[0].message.content)