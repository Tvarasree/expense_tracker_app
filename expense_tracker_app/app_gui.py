import tkinter as tk
from tkinter import messagebox
from expense_tracker import add_expense, set_budget, get_all_expenses, get_budget

# Window setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("450x600")
root.configure(bg="#f4f6f7")

# Header
tk.Label(root, text="💸 Expense Tracker", font=("Helvetica", 20, "bold"), bg="#f4f6f7", fg="#2c3e50").pack(pady=15)

# Budget Input
tk.Label(root, text="Set Budget", font=("Helvetica", 14, "bold"), bg="#f4f6f7", fg="#2c3e50").pack(pady=10)

tk.Label(root, text="Category:", bg="#f4f6f7").pack()
entry_budget_category = tk.Entry(root, width=30)
entry_budget_category.pack()

tk.Label(root, text="Budget Amount:", bg="#f4f6f7").pack()
entry_budget_amount = tk.Entry(root, width=30)
entry_budget_amount.pack()

def on_set_budget():
    category = entry_budget_category.get().strip()
    try:
        amount = float(entry_budget_amount.get().strip())
        set_budget(category, amount)
        messagebox.showinfo("Success", f"Budget set for '{category}'.")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for budget.")

tk.Button(root, text="Set Budget", command=on_set_budget, bg="#27ae60", fg="white", width=20).pack(pady=10)

# Expense Input
tk.Label(root, text="Add Expense", font=("Helvetica", 14, "bold"), bg="#f4f6f7", fg="#2c3e50").pack(pady=10)

tk.Label(root, text="Category:", bg="#f4f6f7").pack()
entry_expense_category = tk.Entry(root, width=30)
entry_expense_category.pack()

tk.Label(root, text="Amount:", bg="#f4f6f7").pack()
entry_expense_amount = tk.Entry(root, width=30)
entry_expense_amount.pack()

tk.Label(root, text="Month (YYYY-MM):", bg="#f4f6f7").pack()
entry_expense_month = tk.Entry(root, width=30)
entry_expense_month.pack()

def on_add_expense():
    category = entry_expense_category.get().strip()
    month = entry_expense_month.get().strip()
    try:
        amount = float(entry_expense_amount.get().strip())
        add_expense(category, amount, month)
        messagebox.showinfo("Success", f"Expense added for '{category}' in {month or 'current month'}.")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

tk.Button(root, text="Add Expense", command=on_add_expense, bg="#3498db", fg="white", width=20).pack(pady=10)

# Monthly Report
tk.Label(root, text="Full Report", font=("Helvetica", 14, "bold"), bg="#f4f6f7", fg="#2c3e50").pack(pady=10)

def show_report():
    report_text.delete("1.0", tk.END)
    records = get_all_expenses()
    if not records:
        report_text.insert(tk.END, "No expenses added yet.\n")
        return

    current_month = ""
    for month, cat, total in records:
        if month != current_month:
            report_text.insert(tk.END, f"\n📅 {month}\n" + "-"*30 + "\n")
            current_month = month
        budget = get_budget(cat)
        report_text.insert(tk.END, f"{cat} - Spent: ₹{total:.2f} / Budget: ₹{budget:.2f}\n")

tk.Button(root, text="Show Full Report", command=show_report, bg="#8e44ad", fg="white", width=25).pack(pady=5)
report_text = tk.Text(root, height=15, width=52, bg="white")
report_text.pack(pady=10)

root.mainloop()
