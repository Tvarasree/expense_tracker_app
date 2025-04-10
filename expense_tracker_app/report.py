from db import get_db_connection
from tabulate import tabulate

def generate_monthly_report(month):
    conn = get_db_connection()
    c = conn.cursor()

    c.execute("SELECT category, SUM(amount) FROM expenses WHERE date LIKE ? GROUP BY category", (f"{month}%",))
    expenses = c.fetchall()

    c.execute("SELECT category, amount FROM budgets WHERE month = ?", (month,))
    budgets = {row['category']: row['amount'] for row in c.fetchall()}

    print("\n📋 Spending Report")
    table = []
    for row in expenses:
        cat = row['category']
        spent = row['SUM(amount)']
        budget = budgets.get(cat, 0)
        remaining = budget - spent
        status = "Over Budget" if remaining < 0 else "Within Budget"
        table.append([cat, spent, budget, remaining, status])

    print(tabulate(table, headers=["Category", "Spent", "Budget", "Remaining", "Status"]))
    conn.close()
