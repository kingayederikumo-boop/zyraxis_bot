from telegram.ext import CommandHandler
from backend.utils.db import get_or_create_user, set_premium

def register_subscription_handlers(app):
    app.add_handler(CommandHandler('profile', profile_cmd))
    app.add_handler(CommandHandler('delete_account', delete_cmd))
    app.add_handler(CommandHandler('upgrade_demo', upgrade_demo))

async def profile_cmd(update, context):
    uid = update.effective_user.id
    u = get_or_create_user(uid)
    await update.message.reply_text(f"Profile: premium={bool(u.get('is_premium'))}")

async def delete_cmd(update, context):
    from backend.utils.db import clear_user_data
    clear_user_data(update.effective_user.id)
    await update.message.reply_text("Your data has been cleared.")

async def upgrade_demo(update, context):
    # demo command to set premium for testing
    set_premium(update.effective_user.id, True)
    await update.message.reply_text("Upgraded to premium (demo).")
