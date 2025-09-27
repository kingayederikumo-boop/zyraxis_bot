```python
import psycopg2
import os

def init_db():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            is_premium BOOLEAN DEFAULT FALSE
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def is_premium_user(user_id):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("SELECT is_premium FROM users WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result and result[0]

def set_premium(user_id, value=True):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (user_id, is_premium)
        VALUES (%s, %s)
        ON CONFLICT (user_id) DO UPDATE SET is_premium = EXCLUDED.is_premium
    """, (user_id, value))
    conn.commit()
    cur.close()
    conn.close()
```
