import sqlite3

def get_db_connection():
    conn = sqlite3.connect('profiles.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_profiles_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS profiles (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            gender TEXT,
            gender_probability REAL,
            sample_size INTEGER,
            age INTEGER,
            age_group TEXT,
            country_id TEXT,
            country_probability REAL,
            created_at TEXT
        )''')
    conn.commit()
    conn.close()