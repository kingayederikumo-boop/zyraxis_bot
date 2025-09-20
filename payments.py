from telegram import Update, LabeledPrice
from telegram.ext import CommandHandler, ContextTypes
import os

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prices = [LabeledPrice(label="Premium Subscription", amount=30000)]  # 300 stars
    await context.bot.send_invoice(
        chat_id=update.effective_chat.id,
        title="ZyraXis Premium",
        description="Monthly subscription for premium features.",
        payload="premium_subscription",
        provider_token=os.getenv("PAYMENT_PROVIDER_TOKEN"),
        currency="USD",
        prices=prices,
        start_parameter="premium-subscription",
    )

payment_handler = CommandHandler("buy", buy)