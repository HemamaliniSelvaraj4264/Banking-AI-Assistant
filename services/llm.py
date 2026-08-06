import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

def get_llm():

    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    return client