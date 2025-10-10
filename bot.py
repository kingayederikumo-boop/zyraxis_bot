import os
from dotenv import load_dotenv
load_dotenv()
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram_bot.handlers.chat_handler import register_chat_handlers
from telegram_bot.handlers.image_handler import register_image_handlers
from telegram_bot.handlers.vault_handler import register_vault_handlers
from telegram_bot.handlers.subscription_handler import register_subscription_handlers
from backend.utils.db import init_db

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise SystemExit('Set BOT_TOKEN in .env')

def main():
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', lambda update,ctx: update.message.reply_text("Hello! I'm ZyraXis.")))
    register_chat_handlers(app)
    register_image_handlers(app)
    register_vault_handlers(app)
    register_subscription_handlers(app)
    print('ZyraXis bot running...')
    app.run_polling()

if __name__ == '__main__':
    main()
