import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'app.db')
print(f"Checking database at: {db_path}")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables found:", tables)
    
    if ('users',) in tables:
        print("Users table exists. Checking count...")
        cursor.execute("SELECT count(*) FROM users")
        print(f"User count: {cursor.fetchone()[0]}")
    
    conn.close()
except Exception as e:
    print(f"Error: {e}")
