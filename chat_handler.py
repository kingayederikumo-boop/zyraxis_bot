from telegram.ext import CommandHandler, MessageHandler, filters
from backend.utils.db import get_or_create_user, save_chat
from backend.utils.db import get_daily_counters, increment_counter
from backend.services.chat import get_chat_response

CHAT_LIMIT_FREE = 15

def register_chat_handlers(app):
    app.add_handler(CommandHandler('chat', chat_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

async def chat_cmd(update, context):
    await update.message.reply_text("Send me a message; free users have 15 replies/day.")

async def message_handler(update, context):
    user_id = update.effective_user.id
    get_or_create_user(user_id)
    # check premium
    conn_user = get_or_create_user(user_id)
    is_premium = bool(conn_user.get('is_premium'))
    counters = get_daily_counters(user_id)
    if (not is_premium) and counters['chats_today'] >= CHAT_LIMIT_FREE:
        return await update.message.reply_text("Daily chat limit reached (15). Upgrade for unlimited.")
    prompt = update.message.text
    await update.message.chat_action('typing')
    resp = get_chat_response(prompt)
    save_chat(user_id, prompt, resp)
    increment_counter(user_id, 'chats')
    await update.message.reply_text(resp)
