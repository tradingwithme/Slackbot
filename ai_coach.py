from openai import ChatCompletion
from os import getenv, environ
from dotenv import load_dotenv

OPENAI_API_KEY = getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    load_dotenv()
    OPENAI_API_KEY = environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY: raise ValueError("OPENAI_API_KEY is not set. Please set it in your environment or .env file.")

def generate_ai_response(user_message):
    response = ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI coach."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].message['content']
