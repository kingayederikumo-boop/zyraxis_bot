from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.db import is_premium_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if is_premium_user(user_id):
        await update.message.reply_text("Welcome back, Premium User!")
    else:
        await update.message.reply_text("Welcome! Use /buy to subscribe to premium features.")

auth_handler = CommandHandler("start", start)