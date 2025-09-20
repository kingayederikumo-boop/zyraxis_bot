from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def ai_insight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if prompt:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("Please provide a prompt for AI insights.")

ai_handler = CommandHandler("ai", ai_insight)