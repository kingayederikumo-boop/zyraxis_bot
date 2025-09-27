```python
import os
from telegram.ext import ApplicationBuilder
from handlers.news import news_handler
from handlers.prices import prices_handler
from handlers.ai_insights import ai_handler
from handlers.auth import auth_handler
from handlers.payments import payment_handler  # <-- now a list
from utils.db import init_db

Initialize the bot application
app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

Initialize the database
init_db()

Add handlers (payment_handler is a list of handlers)
app.add_handler(news_handler)
[9/27, 22:52] ChatGPT: app.add_handler(prices_handler)
app.add_handler(ai_handler)
app.add_handler(auth_handler)

for handler in payment_handler:
    app.add_handler(handler)

Start the bot
app.run_polling()
```
