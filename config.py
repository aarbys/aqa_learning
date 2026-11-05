import os
from dotenv import load_dotenv

BASE_URL = "http://localhost:8080/api/"


# Токен авторизации
load_dotenv()
AUTH_TOKEN = os.getenv("AUTH_TOKEN")