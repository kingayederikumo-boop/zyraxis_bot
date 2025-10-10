from backend.utils.db import add_payment, set_premium

def handle_payment_webhook(payload: dict):
    provider = payload.get('provider')
    pid = payload.get('provider_id')
    tid = payload.get('telegram_id')
    status = payload.get('status')
    if not (provider and pid and tid and status):
        return False
    add_payment(tid, provider, pid, status)
    if status == 'paid':
        set_premium(tid, True)
        return True
    return False
