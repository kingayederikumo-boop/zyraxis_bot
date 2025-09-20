from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import requests
import os

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={os.getenv('CRYPTOPANIC_API_KEY')}&public=true"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('results', [])[:5]
        message = "\n\n".join([f"{article['title']}\n{article['url']}" for article in articles])
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Failed to fetch news.")

news_handler = CommandHandler("news", news)