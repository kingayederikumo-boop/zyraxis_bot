# ZyraXis Telegram Bot 🤖

ZyraXis is a powerful Telegram bot that provides:
- 📰 Real-time crypto news updates
- 💰 Live coin price tracking
- 📊 AI-powered coin analysis
- 🔒 Premium features via Telegram Stars
- 🧠 Custom crypto insights (OpenAI-powered)

---

## Features

### 🆓 Free Features:
- Basic crypto news (CryptoPanic API)
- Coin price lookups (CoinGecko API)
- Help and about commands

### ⭐ Premium Features:
- AI-generated coin analysis
- Deep crypto insights with ChatGPT
- Portfolio tracking (coming soon)
- Advanced notifications
- Premium access via Telegram Stars (300/month)

---

## Tech Stack

- Python 3.10+
- pyTelegramBotAPI
- PostgreSQL (Railway-hosted)
- OpenAI API
- CryptoPanic API
- Deployed on Railway

---

## Environment Variables

Create a `.env` file with the following keys:

```env
BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
CRYPTOPANIC_API_KEY=your_cryptopanic_api_key
DATABASE_URL=your_postgresql_database_url