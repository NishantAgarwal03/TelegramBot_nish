import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_telegram_message(text):
    """
    Send a message to a Telegram chat using the Bot API.
    """
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    if not token or not chat_id:
        print("Error: BOT_TOKEN or CHAT_ID not found in environment variables.")
        return False
        
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Message sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send message: {e}")
        return False
