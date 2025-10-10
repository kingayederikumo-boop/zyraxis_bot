# backend/app.py  -- Flask server for mini-app + simple webhook/test endpoints
import os
from flask import Flask, send_from_directory, jsonify, request
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__),'..','.env'))
from backend.utils.db import init_db, get_history, get_images, clear_user_data
from backend.routes.subscription_routes import handle_payment_webhook

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
MINI_APP_FOLDER = os.path.join(APP_ROOT, 'mini_app')

app = Flask(__name__, static_folder=MINI_APP_FOLDER, static_url_path='/mini_app')

# init DB on app start
init_db()

# serve mini app files
@app.route('/mini_app/<path:path>')
def serve_mini(path):
    return send_from_directory(MINI_APP_FOLDER, path)

@app.route('/api/history', methods=['GET'])
def api_history():
    tid = int(os.getenv('DEMO_TELEGRAM_ID', '0'))
    if not tid:
        return jsonify([]), 200
    return jsonify(get_history(tid)), 200

@app.route('/api/images', methods=['GET'])
def api_images():
    tid = int(os.getenv('DEMO_TELEGRAM_ID', '0'))
    if not tid:
        return jsonify([]), 200
    return jsonify(get_images(tid)), 200

@app.route('/api/delete_account', methods=['POST'])
def api_delete():
    tid = int(os.getenv('DEMO_TELEGRAM_ID','0'))
    if not tid:
        return jsonify({'ok': True})
    clear_user_data(tid)
    return jsonify({'ok': True})

# Payment webhook endpoint (provider should POST here)
@app.route('/webhook/payment', methods=['POST'])
def payment_webhook():
    data = request.get_json() or {}
    ok = handle_payment_webhook(data)
    return jsonify({'ok': ok}), (200 if ok else 400)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
