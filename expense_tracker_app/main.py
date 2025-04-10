from db import setup_database
from expense_tracker import add_expense, set_budget
from report import generate_monthly_report

def main():
    setup_database()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. Set Budget")
        print("3. Show Monthly Report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, amount)

        elif choice == '2':
            month = input("Enter month (YYYY-MM): ")
            category = input("Enter category: ")
            amount = float(input("Enter monthly budget: "))
            set_budget(month, category, amount)

        elif choice == '3':
            month = input("Enter month (YYYY-MM): ")
            generate_monthly_report(month)

        elif choice == '4':
            break

        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
