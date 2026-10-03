# PulseBot - 3-in-1 Automated Telegram Bot 🚀

PulseBot is a production-ready automation suite that sends scheduled updates for **News**, **Cricket Scores**, and **Stock Prices** directly to your Telegram chat.

## 📰 Features
1.  **News Bot**: Fetches top 5 Indian headlines every 2 hours and provides an AI-powered summary using the BART model.
2.  **Cricket Bot**: Tracks live match updates at fixed intervals (8 AM, 6 PM, 8 PM, 10 PM IST).
3.  **Stock Bot**: Delivers daily prices for RELIANCE, TCS, and INFY at 4:00 PM IST.

---

## 🛠️ Setup Instructions (Local)

### 1. Prerequisites
- Python 3.8+ installed.
- A Telegram account.

### 2. Get Your API Keys
- **Telegram**: Chat with [@BotFather](https://t.me/botfather) to create a bot and get a `BOT_TOKEN`. Chat with [@userinfobot](https://t.me/userinfobot) to get your `CHAT_ID`.
- **NewsAPI**: Register at [newsapi.org](https://newsapi.org) for a free key.
- **CricketData**: Register at [cricketdata.org](https://cricketdata.org) for a free key.

### 3. Installation
```powershell
# Clone the repository
# git clone <your-repo-url>
# cd PulseBot

# Install dependencies
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory (or copy `.env.example`) and fill in your keys:
```text
NEWS_API_KEY=your_key
CRICKET_API_KEY=your_key
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

### 5. Run it!
```powershell
python main.py
```

---

## ☁️ Deployment (Railway)

PulseBot is designed to run 24/7 on [Railway](https://railway.app).

1.  Push this code to your **GitHub** repository.
2.  On Railway, create a **New Project** and link your GitHub repo.
3.  Add the 4 environment variables from your `.env` file to the **Variables** tab on Railway.
4.  Railway will detect the `Procfile` and start the `worker` automatically.

---

## 🏗️ Project Structure
- `main.py`: The orchestrator and scheduler.
- `news_bot.py`, `cricket_bot.py`, `stock_bot.py`: Individual bot logic.
- `summarizer.py`: Uses Hugging Face `transformers` for AI summarization.
- `notifier.py`: Shared Telegram notification module.
- `utils.py`: Message formatting utilities.

---

## 📜 Requirements
- `requests`
- `transformers`
- `torch`
- `python-dotenv`
- `schedule`
- `yfinance`

---

## 🤝 Contributing
Feel free to fork this project and add more bots!

Stay sharp. 🔥

## Support

[Donate](https://drive.google.com/file/d/14KBkEcr6j4KaxDHcHyejdYlFDt4GjR6O/view?usp=drive_link)
