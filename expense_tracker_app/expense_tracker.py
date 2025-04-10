import sqlite3
from datetime import datetime

# Database setup
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        month TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL UNIQUE,
        amount REAL NOT NULL
    )
''')

conn.commit()

import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category TEXT,
                        amount REAL,
                        month TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
                        category TEXT PRIMARY KEY,
                        amount REAL)''')
    conn.commit()
    conn.close()

def set_budget(category, amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO budgets (category, amount) VALUES (?, ?)", (category, amount))
    conn.commit()
    conn.close()

def add_expense(category, amount, month):
    if not category or amount <= 0 or not month:
        raise ValueError("Invalid input for expense.")
    
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (category, amount, month) VALUES (?, ?, ?)", (category, amount, month))
    conn.commit()
    conn.close()

def get_budget(category):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT amount FROM budgets WHERE category = ?", (category,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0.0

def get_all_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT month, category, SUM(amount) FROM expenses GROUP BY month, category ORDER BY month")
    records = cursor.fetchall()
    conn.close()
    return records

