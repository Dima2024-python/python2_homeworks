import os

from dotenv import load_dotenv

load_dotenv()


TOKEN_API = os.getenv("TOKEN_API")
USER = os.getenv("USER")
IMAP_SERVER = os.getenv("IMAP_SERVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
