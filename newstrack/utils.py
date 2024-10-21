import os
from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    return os.getenv("THE_NEWS_API_KEY")


