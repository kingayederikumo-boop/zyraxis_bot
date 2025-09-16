import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Get the bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to *ZyraXis*! \n\n"
        "Your futuristic crypto companion.\n\n"
        "Type /help to see what I can do."
    )

# Command: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *ZyraXis Commands:*\n\n"
        "/start - Begin your journey\n"
        "/help - Show this help message\n"
        "/crypto - Get the latest crypto update\n"
        "/about - Learn more about ZyraXis"
    )

# Command: /crypto (placeholder for now)
async def crypto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Crypto updates coming soon! Stay tuned..."
    )

# Command: /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ *ZyraXis* is your futuristic AI crypto companion.\n"
        "She evolves with you — powerful, insightful, and always learning."
    )

# Main function
def main():
    # Make sure the token exists
    if not TOKEN:
        raise ValueError("No BOT_TOKEN found! Set it in your environment variables.")

    app = Application.builder().token(TOKEN).build()

    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("crypto", crypto))
    app.add_handler(CommandHandler("about", about))

    # Run bot
    app.run_polling()

if __name__ == "__main__":
    main()