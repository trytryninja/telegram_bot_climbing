import os
import sys
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"
payload = {
    "chat_id": CHAT_ID,
    "question": "Climb this week?",
    "options": ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun", "Not this week"],
    "is_anonymous": False,
}

try:
    r = requests.post(url, json=payload, timeout=30)
    r.raise_for_status()
    print(r.json())
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
