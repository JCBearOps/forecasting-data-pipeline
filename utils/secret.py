import os
from dotenv import load_dotenv

load_dotenv()

def get_secret(key: str, fallback: str = None):
    return os.getenv(key, fallback)
