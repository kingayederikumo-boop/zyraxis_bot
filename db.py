# backend/utils/db.py
import sqlite3
from datetime import datetime, date
import os
DB = os.getenv('SQLITE_DB', 'zyraxis.db')

def get_conn():
    conn = sqlite3.connect(DB, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn(); c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, telegram_id INTEGER UNIQUE, is_premium INTEGER DEFAULT 0, created_at TEXT
    );''')
    c.execute('''CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY, telegram_id INTEGER, prompt TEXT, response TEXT, created_at TEXT
    );''')
    c.execute('''CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY, telegram_id INTEGER, url TEXT, prompt TEXT, created_at TEXT
    );''')
    c.execute('''CREATE TABLE IF NOT EXISTS counters (
        id INTEGER PRIMARY KEY, telegram_id INTEGER, date TEXT, chats INTEGER DEFAULT 0, images INTEGER DEFAULT 0
    );''')
    c.execute('''CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY, telegram_id INTEGER, provider TEXT, provider_id TEXT, status TEXT, created_at TEXT
    );''')
    conn.commit(); conn.close()
