```python
import os
from telegram import Update, LabeledPrice
from telegram.ext import CallbackContext, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters

Command to start premium subscription purchase
async def start_premium(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    title = "ZyraXis Premium Subscription"
    description = "Monthly access to premium features"
    payload = "premium-subscription"
    currency = "USD"
    prices = [LabeledPrice("Monthly Plan", 30000)]  # $300.00 in cents

    provider_token = os.getenv("TELEGRAM_PROVIDER_TOKEN")
    if not provider_token:
        await update.message.reply_text("Payment provider token not set.")
        return

    await context.bot.send_invoice(
        chat_id=chat_id,
        title=title,
        description=description,
        payload=payload,
        provider_token=provider_token,
        start_parameter="subscribe",
        currency=currency,
        prices=prices,
        need_name=True,
        need_email=True
    )

Pre-checkout handler: confirm checkout
async def precheckout_callback(update: Update, context: CallbackContext):
    query = update.pre_checkout_query
[9/27, 22:52] ChatGPT: # Always approve pre-checkout query for now
    await query.answer(ok=True)

Successful payment handler
async def successful_payment_callback(update: Update, context: CallbackContext):
    user = update.effective_user
    # Mark user as premium in your DB here
    # Example: context.bot_data['db'].set_premium(user.id, True)

    await update.message.reply_text(
        f"Thank you for your payment, {user.first_name}! Your ZyraXis Premium subscription is now active."
    )

Handlers grouped to export
payment_handler = [
    CommandHandler("premium", start_premium),
    PreCheckoutQueryHandler(precheckout_callback),
    MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback)
]
