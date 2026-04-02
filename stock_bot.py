import os
import requests
import yfinance as yf
from notifier import send_telegram_message
from utils import format_message

def run_stock_bot():
    """
    Fetch latest prices for specific stock tickers and send to Telegram.
    """
    tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
    stock_updates = []
    
    try:
        # Create a session with browser-like headers to avoid blocking
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        for ticker_name in tickers:
            ticker = yf.Ticker(ticker_name, session=session)
            # Use fast_info for more reliable price fetching
            price = ticker.fast_info['last_price']
            if price:
                stock_updates.append(f"{ticker_name}: \u20b9{price:,.2f}")
            else:
                stock_updates.append(f"{ticker_name}: Data unavailable")
        
        # Send message to Telegram
        content = "\n".join(stock_updates)
        message = format_message("Stock Market Updates", content)
        send_telegram_message(message)
        
    except Exception as e:
        print(f"Stock Bot error: {e}")

if __name__ == "__main__":
    run_stock_bot()
