from dotenv import load_dotenv
import os

load_dotenv()

YA_TOKEN = os.environ.get("YA_TOKEN")
TG_TOKEN = os.environ.get("TG_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
PREP_DIR = os.environ.get("PREP_DIR")
PAST_DIR = os.environ.get("PAST_DIR")