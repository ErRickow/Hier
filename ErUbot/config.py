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


MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://esaproject:esaproject@cluster0.dgdvkh5.mongodb.net/?retryWrites=true&w=majority",
)

SESSION_STRING = os.environ.get(
    "SESSION_STRING",
    "BQFSFokARpqY1_eS3aZ1rEjvKVizFZsiwmsddEbUEueiQ3zN82EKtCqG3nq1LupthUUQFpcU27oauZVCHBuAclETDaXA0laHAL-MbIcGlRZARg1TLt0sablE_-fLijPNAQuf8ueaQ4plwnXWBlwCaFWH1-W_x-qMNfDrjIkIZs1JScT6vStmZMVeMrm1-Mmdd88hc8h7WhDEk8EjXF8vAL89EINYoWNiKB6fY2o8hQZ6oIism6oVTnGxCI_kfoG-66dJZHEXb5l_oeT9GNBu1L0LcaZVJGsnYdcFSMm4sGCUQlB4sDTiZxcYbEvdbVgpIav1rLYDgaazABgdV51efhJ-ToS7pgAAAAGBSrSYAA",
)
