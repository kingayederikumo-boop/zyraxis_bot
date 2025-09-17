```python
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pymongo import MongoClient
from dotenv import load_dotenv

Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv(8203477255:AAHgniik-6DWIcdsBoa0D1xh5yC41MLksMo)
MONGO_URI = os.getenv(mongodb+srv://kingayederikumo_db_user:qHRKFqvPxBZNX7qo@cluster0.xfuuajm.mongodb.net/zyraxis-db?retryWrites=true&w=majority&appName=Cluster0)

Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["zyraxis_bot"]
users_collection = db["users"]

Helper functions
def get_user(user_id):
    user = users_collection.find_one({"user_id": user_id})
    if not user:
        user = {"user_id": user_id, "stars": 0, "premium": False}
        users_collection.insert_one(user)
    return user

def update_stars(user_id, amount):
[9/18, 00:12] ChatGPT: users_collection.update_one({"user_id": user_id}, {"inc": "stars": amount)

def set_premium(user_id):
    users_collection.update_one("user_id": user_id, "set": {"premium": True}})

Bot commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    get_user(user_id)
    await update.message.reply_text("👋 Welcome to ZyraXis! Use /earn to collect stars and /balance to check your stars.")

async def earn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    update_stars(user_id, 10)
    await update.message.reply_text("✨ You earned 10 stars!")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    stars = user.get("stars", 0)
    premium = user.get("premium", False)
    msg = f"⭐ Stars: {stars}\n🔒 Premium: {'Yes' if premium else 'No'}"
    await update.message.reply_text(msg)

async def premium(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    if user["stars"] >= 100:
        update_stars(user_id, -100)
        set_premium(user_id)
        await update.message.reply_text("✅ You are now a premium user!")
    else:
[9/18, 00:12] ChatGPT: await update.message.reply_text("❌ You need at least 100 stars to unlock premium.")

Main app
if _name_ == "_main_":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("earn", earn))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("premium", premium))

    print("🤖 ZyraXis Bot is running...")
    app.run_polling()