# ZyraXis

ZyraXis — Telegram AI assistant + Vault mini-app.

Contents:
- backend/         -> Flask API + services
- telegram_bot/    -> Telegram bot (python-telegram-bot)
- mini_app/        -> Static mini-app (HTML/CSS/JS)

Quick start:
1. Copy `.env.example` -> `.env` and fill values.
2. From project root:
   pip install -r backend/requirements.txt
3. Initialize DB:
   python backend/scripts/init_db.py
4. Run mini app server:
   python backend/app.py
5. In another terminal run bot:
   python telegram_bot/bot.py

Deploy: Replit / Railway / Render (set env vars).
