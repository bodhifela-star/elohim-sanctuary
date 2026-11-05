import sqlite3
import hashlib
import os

DB_NAME = "elohim_sanctuary.db"

def hash_password(password):
    salt = b"elohim_salt_2026"
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            display_name TEXT NOT NULL,
            is_guardian INTEGER DEFAULT 0
        )
    ''')
    
    # Devotionals / Posts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            category TEXT NOT NULL,
            structure TEXT NOT NULL,
            amen_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Seed initial accounts if empty
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        users = [
            ('mom', hash_password('mom123'), 'Mom (Site Guardian)', 1),
            ('caleb', hash_password('caleb123'), 'Caleb of Judah', 0),
            ('hannah', hash_password('hannah123'), 'Hannah Grace', 0)
        ]
        cursor.executemany("INSERT INTO users (username, password_hash, display_name, is_guardian) VALUES (?, ?, ?, ?)", users)

    # Seed initial devotional post
    cursor.execute("SELECT COUNT(*) FROM posts")
    if cursor.fetchone()[0] == 0:
        posts = [
            ('mom', 'Eternal Foundations of Praise', 'Before the mountains were born, or ever you had formed the earth and the world, from everlasting to everlasting, you are Elohim.', "Mom's Devotionals", 'Mountains')
        ]
        cursor.executemany("INSERT INTO posts (username, title, content, category, structure) VALUES (?, ?, ?, ?, ?)", posts)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✨ Elohim's Sanctuary database initialized successfully.")
