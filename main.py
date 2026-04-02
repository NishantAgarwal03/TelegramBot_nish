import schedule
import time
from news_bot import run_news_bot
from cricket_bot import run_cricket_bot
from stock_bot import run_stock_bot

def main():
    print("Bot system started...")
    
    # --- News Bot Schedule (Every 2 hours) ---
    schedule.every(2).hours.do(run_news_bot)
    
    # --- Cricket Bot Schedule (8 AM, 6 PM, 8 PM, 10 PM) ---
    schedule.every().day.at("08:00").do(run_cricket_bot)
    schedule.every().day.at("18:00").do(run_cricket_bot)
    schedule.every().day.at("20:00").do(run_cricket_bot)
    schedule.every().day.at("22:00").do(run_cricket_bot)
    
    # --- Stock Bot Schedule (Daily at 4 PM) ---
    schedule.every().day.at("16:00").do(run_stock_bot)
    
    # Run the bots once at startup for verification and immediate updates
    print("Sending immediate updates...")
    run_news_bot()
    run_cricket_bot()
    run_stock_bot()

    while True:
        schedule.run_pending()
        time.sleep(60) # Check every minute

if __name__ == "__main__":
    main()
