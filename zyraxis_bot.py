import os
import logging
from telegram import Update, LabeledPrice
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from pymongo import MongoClient

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment variables
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MONGO_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["zyraxis_bot"]
users_collection = db["users"]

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    users_collection.update_one(
        {"user_id": user.id},
        {"$set": {"username": user.username, "first_name": user.first_name}},
        upsert=True,
    )
    await update.message.reply_text(
        f"👋 Hello {user.first_name}, welcome to *ZyraXis*!\n\n"
        "🔥 Explore crypto insights and unlock premium content with Telegram Stars.",
        parse_mode="Markdown"
    )

# /premium command
async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prices = [LabeledPrice("Premium Access (1 Month)", 100)]  # 100 Stars = $1.00 equivalent
    await update.message.reply_invoice(
        title="ZyraXis Premium",
        description="Unlock premium crypto signals & tools.",
        payload="premium_subscription",
        provider_token="",  # Leave empty for Stars
        currency="XTR",     # XTR = Telegram Stars
        prices=prices,
    )

# Message handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 Type /premium to unlock premium features with Stars!"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("premium", premium))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()