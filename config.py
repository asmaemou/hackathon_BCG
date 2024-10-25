import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_API_SECRET = os.getenv('GEMINI_API_SECRET')
GEMINI_API_SECRET_ENCODED = GEMINI_API_SECRET.encode()
GEMINI_API_URL = 'https://api.gemini.com'
