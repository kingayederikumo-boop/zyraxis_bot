import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ==============================
# 🔹 Insert your Bot Token here
# ==============================
BOT_TOKEN = "8203477255:AAHgniik-6DWIcdsBoa0D1xh5yC41MLksMo"

# ==============================
# 🔹 Enable Logging
# ==============================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ==============================
# 🔹 Commands
# ==============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to *ZyraXis*, your futuristic crypto companion!\n\n"
        "Type /price <symbol> to get live prices.\n"
        "Example: `/price BTC`"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Available Commands:\n"
        "/start - Welcome message\n"
        "/help - Show this menu\n"
        "/price <symbol> - Get crypto price\n"
        "/about - Info about ZyraXis"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ *ZyraXis* is a futuristic Telegram bot built for crypto lovers.\n"
        "Stay updated with real-time market data 📊."
    )

# ==============================
# 🔹 Crypto Price Function
# ==============================
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Usage: /price BTC")
        return

    symbol = context.args[0].upper()
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd"

    try:
        response = requests.get(url).json()
        if symbol.lower() in response:
            usd_price = response[symbol.lower()]["usd"]
            await update.message.reply_text(f"💰 {symbol} Price: *${usd_price}*")
        else:
            await update.message.reply_text("❌ Symbol not found. Try again.")
    except Exception as e:
        await update.message.reply_text("⚠️ Error fetching data. Please try later.")
        logger.error(f"Price fetch error: {e}")

# ==============================
# 🔹 Main Function
# ==============================
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("price", price))

    app.run_polling()

if __name__ == "__main__":
    main()