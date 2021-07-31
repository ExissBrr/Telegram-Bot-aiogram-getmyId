import os

from dotenv import load_dotenv

load_dotenv()
TOKEN_BOT: str = os.getenv("TOKEN_BOT")
PG_USER: str = os.getenv("PG_USER")
PG_PASSWORD: str = os.getenv("PG_PASSWORD")
PG_DATABASE: str = os.getenv("DATABASE")
IP: str = os.getenv("IP")
PG_PORT: str = os.getenv("PG_PORT")
PG_URL = f'postgresql://{PG_USER}:{PG_PASSWORD}@{IP}:{PG_PORT}/{PG_DATABASE}'
print(PG_USER)