import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# ---------- Load environment variables
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ---------- Initialise the OpenAI client
print(f'Using OPENAI_API_KEY, {OPENAI_API_KEY}')
client = OpenAI(api_key=OPENAI_API_KEY)
model = "gpt-4o-mini"

def run_chat_completion (messages):
    collected_messages = []
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        # collect the system messages
        collected_messages.append(chunk_message)

    return collected_messages