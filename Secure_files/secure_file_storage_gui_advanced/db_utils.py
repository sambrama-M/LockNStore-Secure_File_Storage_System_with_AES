import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("filedata.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        action TEXT,
        hash TEXT,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()

def log_file(filename, action, file_hash):
    conn = sqlite3.connect("filedata.db")
    conn.execute("INSERT INTO files (filename, action, hash, timestamp) VALUES (?, ?, ?, ?)",
                 (filename, action, file_hash, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def fetch_logs():
    conn = sqlite3.connect("filedata.db")
    cursor = conn.execute("SELECT filename, action, hash, timestamp FROM files")
    rows = cursor.fetchall()
    conn.close()
    return rows