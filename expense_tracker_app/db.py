import sqlite3

def get_db_connection():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            month TEXT,
            category TEXT,
            amount REAL,
            PRIMARY KEY(month, category)
        )
    ''')

    conn.commit()
    conn.close()
