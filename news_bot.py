import os
import requests
from notifier import send_telegram_message
from summarizer import summarize_text
from utils import format_message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def run_news_bot():
    """
    Fetch top 5 news headlines from News API and send to Telegram.
    """
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("status") == "ok":
            articles = data.get("articles", [])[:5]
            
            # Combine all headlines into a single text for summarization
            full_text = "\n".join([a['title'] + ". " + (a['description'] if a['description'] else "") for a in articles])
            
            # Summarize using BART
            summary = summarize_text(full_text)
            
            # Format and send to Telegram
            message = format_message("Latest News Headlines (India)", summary)
            send_telegram_message(message)
        else:
            print(f"Error fetching news: {data.get('message')}")
            
    except Exception as e:
        print(f"News Bot error: {e}")

if __name__ == "__main__":
    run_news_bot()
