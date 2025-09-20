# utils/helpers.py

from datetime import datetime
import logging

def format_price_data(symbol: str, price: float, change_24h: float) -> str:
    arrow = "🔺" if change_24h >= 0 else "🔻"
    return (
        f"📈 *{symbol.upper()} Price Info:*\n"
        f"Price: ${price:.2f}\n"
        f"24h Change: {arrow} {abs(change_24h):.2f}%"
    )

def format_news_article(article: dict) -> str:
    title = article.get("title", "No Title")
    link = article.get("url", "#")
    return f"📰 [{title}]({link})"

def is_premium(user_data: dict) -> bool:
    return user_data.get("is_premium", False)

def log_error(error: Exception):
    logging.error(f"❌ Error: {str(error)}")

def get_current_timestamp() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")