import os
import requests
from notifier import send_telegram_message
from utils import format_message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def run_cricket_bot():
    """
    Fetch current match updates using CricketData.org API.
    """
    # API key from https://cricketdata.org/
    api_key = os.getenv("CRICKET_API_KEY")
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={api_key}&offset=0"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("status") == "success":
            matches = data.get("data", [])
            if not matches:
                return
                
            match_updates = []
            for match in matches[:5]: # Send top 5 live/recent matches
                name = match.get("name", "Unknown Match")
                status = match.get("status", "Match Status Unknown")
                update = f"{name} \u2192 {status}"
                match_updates.append(update)
            
            # Send message to Telegram
            content = "\n".join(match_updates)
            message = format_message("Cricket Match Updates", content)
            send_telegram_message(message)
        else:
            print(f"Error fetching cricket data: {data.get('reason')}")
            
    except Exception as e:
        print(f"Cricket Bot error: {e}")

if __name__ == "__main__":
    run_cricket_bot()
