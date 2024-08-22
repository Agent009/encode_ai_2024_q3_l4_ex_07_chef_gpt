import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialise the OpenAI client
print(f'Using OPENAI_API_KEY, {OPENAI_API_KEY}')
client = OpenAI(api_key=OPENAI_API_KEY)


if __name__ == '__main__':
    print(f'Hello, let\'s get started')

