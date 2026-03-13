import json
import datetime

FILE = "expenses.json"


def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)


expenses = load_expenses()


def add_expense():
    desc = input("Description: ")
    category = input("Category (Food/Travel/Shopping/Other): ")

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid number.")
        return

    date = str(datetime.date.today())

    expense = {
        "desc": desc,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense saved.")


def view_expenses():

    if not expenses:
        print("No expenses yet.")
        return

    print("\n--- Expenses ---")

    for i, exp in enumerate(expenses):
        print(
            f"{i+1}. {exp['date']} | {exp['desc']} | {exp['category']} | ₹{exp['amount']}"
        )


def delete_expense():

    view_expenses()

    try:
        index = int(input("Enter expense number to delete: ")) - 1
        expenses.pop(index)
        save_expenses(expenses)
        print("Deleted.")
    except:
        print("Invalid selection.")


def total_spent():

    total = sum(exp["amount"] for exp in expenses)

    print(f"\nTotal spent: ₹{total}")


def category_summary():

    summary = {}

    for exp in expenses:

        cat = exp["category"]
        amt = exp["amount"]

        summary[cat] = summary.get(cat, 0) + amt

    print("\n--- Category Spending ---")

    for cat, amount in summary.items():
        print(f"{cat}: ₹{amount}")


def spending_chart():

    summary = {}

    for exp in expenses:

        cat = exp["category"]
        amt = exp["amount"]

        summary[cat] = summary.get(cat, 0) + amt

    print("\n--- Spending Chart ---")

    for cat, amount in summary.items():
        bar = "█" * int(amount / 50)
        print(f"{cat:<10} {bar} ₹{amount}")


def search_expense():

    keyword = input("Search keyword: ").lower()

    found = False

    for exp in expenses:

        if keyword in exp["desc"].lower():

            print(
                f"{exp['date']} | {exp['desc']} | {exp['category']} | ₹{exp['amount']}"
            )
            found = True

    if not found:
        print("No matching expenses.")


def main():

    while True:

        print("\n==== Expense Tracker ====")
        print("1 Add Expense")
        print("2 View Expenses")
        print("3 Delete Expense")
        print("4 Total Spent")
        print("5 Category Summary")
        print("6 Spending Chart")
        print("7 Search Expense")
        print("8 Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            total_spent()

        elif choice == "5":
            category_summary()

        elif choice == "6":
            spending_chart()

        elif choice == "7":
            search_expense()

        elif choice == "8":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()