```python
import os
import requests
from telegram import LabeledPrice

--- Telegram Payments ---
def get_subscription_invoice(chat_id):
    title = "ZyraXis Premium Subscription"
    description = "Monthly access to premium features"
    payload = "premium-subscription"
    currency = "USD"
    prices = [LabeledPrice("Monthly Plan", 30000)]  # 300.00 USD cents = $300
    provider_token = os.getenv("TELEGRAM_PROVIDER_TOKEN")

    return {
        "chat_id": chat_id,
        "title": title,
        "description": description,
        "payload": payload,
        "provider_token": provider_token,
        "start_parameter": "subscribe",
        "currency": currency,
        "prices": prices,
    }

--- Flutterwave Integration ---
FLUTTERWAVE_SECRET_KEY = os.getenv("FLUTTERWAVE_SECRET_KEY")
FLUTTERWAVE_BASE_URL = "https://api.flutterwave.com/v3"

def create_flutterwave_payment(email, amount, tx_ref, redirect_url):
    headers = {
        "Authorization": f"Bearer {FLUTTERWAVE_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "tx_ref": tx_ref,
        "amount": amount,
        "currency": "USD",
        "redirect_url": redirect_url,
[9/21, 14:43] ChatGPT: "payment_options": "card",
        "customer": {
            "email": email
        },
        "customizations": {
            "title": "ZyraXis Premium",
            "description": "Monthly Premium Subscription"
        }
    }

    response = requests.post(
        f"{FLUTTERWAVE_BASE_URL}/payments",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
```
