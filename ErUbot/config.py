import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1557184285, #Kage
    6464124056,
    6444512773,
    2098545567
]


API_ID = os.environ("API_ID")


API_HASH = os.environ("API_HASH")


OPENAI_API = os.environ.get("OPENAI_API", "ssk-f3185kP8hFfcOeONlTRrT3BlbkFJjwAMOE92hL7OdpgBwuyR")


BOT_TOKEN = os.environ("BOT_TOKEN")


OWNER_ID = int(os.environ.get("OWNER_ID", "6464124056"))


MAX_BOT = int(os.environ.get("MAX_BOT", "50"))


SKY = int(os.environ.get("SKY", "-1001941886895"))


MONGO_URL = os.environ(
    "MONGO_URL"
)

SESSION_STRING = os.environ(
    "SESSION_STRING"
)
