from telegram.ext import CommandHandler
import os
WEB_APP_URL = os.getenv('WEB_APP_URL', 'https://example.com/mini_app/index.html')
def register_vault_handlers(app):
    app.add_handler(CommandHandler('vault', vault_cmd))

async def vault_cmd(update, context):
    await update.message.reply_text(f'Open the Vault mini-app: {WEB_APP_URL}')
