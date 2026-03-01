import time
from datetime import datetime

def divider(char="─", width=48):
    print(char * width)

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading(message="Processing", duration=1.0, steps=10):
    print(f"  {message} ", end='', flush=True)
    for _ in range(steps):
        print(".", end='', flush=True)
        time.sleep(duration / steps)
    print(" Done.")

def format_inr(amount):
    return f"Rs.{amount:,.2f}"

def timestamp():
    return datetime.now().strftime("%d %b %Y  %H:%M:%S")

def mini_bar(value, max_value, width=20):
    if max_value <= 0:
        return "[" + "-" * width + "]"
    filled = int((value / max_value) * width)
    filled = max(0, min(filled, width))
    return "[" + "#" * filled + "-" * (width - filled) + "]"

ACCOUNTS = {
    "1234": {"pin": "0000", "name": "Sravan Kumar", "balance": 25000.0, "savings": 10000.0},
    "5678": {"pin": "1111", "name": "Praveen ", "balance": 800500.0, "savings": 13200.0},
}

DAILY_LIMIT = 50000.0
WITHDRAW_LIMIT = 20000.0
MAX_HISTORY = 10

def log(account, txn_type, amount, balance):
    account.setdefault("history", [])
    account["history"].append({
        "time": datetime.now().strftime("%d-%b %H:%M:%S"),
        "type": txn_type,
        "amount": amount,
        "balance": balance,
    })
    if len(account["history"]) > MAX_HISTORY:
        account["history"].pop(0)

def check_balance(account):
    total = account["balance"] + account["savings"]
    divider()
    print("  ACCOUNT SUMMARY")
    divider()
    print(f"  Account Holder  : {account['name']}")
    print(f"  As of           : {timestamp()}")
    divider("-")
    print(f"  Checking        : {format_inr(account['balance'])}")
    print(f"  Savings         : {format_inr(account['savings'])}")
    print(f"  Total           : {format_inr(total)}")
    divider("-")
    bar = mini_bar(account["balance"], total)
    print(f"  Checking share  : {bar}")
    divider()

def deposit(account, amount):
    if amount <= 0 or amount > DAILY_LIMIT:
        print("  ERROR: Invalid deposit amount.")
        return
    loading("Processing deposit")
    account["balance"] += amount
    log(account, "DEPOSIT", amount, account["balance"])
    print(f"\n  SUCCESS: {format_inr(amount)} deposited.")
    print(f"  New Balance: {format_inr(account['balance'])}")

def withdraw(account, amount):
    if amount <= 0 or amount > WITHDRAW_LIMIT:
        print("  ERROR: Invalid withdrawal amount.")
        return

    if amount > account["balance"]:
        shortfall = amount - account["balance"]
        if account["savings"] >= shortfall:
            choice = input(f"  Transfer {format_inr(shortfall)} from savings? (y/n): ").lower()
            if choice == "y":
                account["savings"] -= shortfall
                account["balance"] += shortfall
                log(account, "TRANSFER (SAV->CHK)", shortfall, account["balance"])
            else:
                return
        else:
            print("  ERROR: Insufficient funds.")
            return

    loading("Processing withdrawal")
    account["balance"] -= amount
    log(account, "WITHDRAWAL", amount, account["balance"])
    print(f"\n  SUCCESS: {format_inr(amount)} withdrawn.")
    print(f"  Remaining Balance: {format_inr(account['balance'])}")

def transfer(account):
    divider()
    print("  TRANSFER FUNDS")
    divider()

    target_id = input("  Enter recipient account number: ").strip()

    if target_id not in ACCOUNTS or target_id == account["_id"]:
        print("  ERROR: Invalid account.")
        return

    try:
        amount = float(input("  Amount (Rs.): "))
    except:
        print("  ERROR: Invalid amount.")
        return

    if amount <= 0 or amount > account["balance"]:
        print("  ERROR: Insufficient funds.")
        return

    target = ACCOUNTS[target_id]

    loading(f"Transferring to {target['name']}")
    account["balance"] -= amount
    target["balance"] += amount

    log(account, f"TRANSFER TO {target['name']}", amount, account["balance"])
    log(target, f"TRANSFER FROM {account['name']}", amount, target["balance"])

    print(f"\n  SUCCESS: {format_inr(amount)} sent.")
    print(f"  Balance: {format_inr(account['balance'])}")

def show_history(account):
    history = account.get("history", [])
    divider()
    print("  TRANSACTION HISTORY")
    divider()

    if not history:
        print("  No transactions yet.")
        return

    print(f"  {'DATE & TIME':<22}{'TYPE':<24}{'AMOUNT':>12}{'BALANCE':>12}")
    divider("-")

    for entry in reversed(history):
        print(
            f"  {entry['time']:<22}"
            f"{entry['type']:<24}"
            f"{format_inr(entry['amount']):>12}"
            f"{format_inr(entry['balance']):>12}"
        )
    divider()

def change_pin(account):
    current = input("  Current PIN: ")
    if current != account["pin"]:
        print("  ERROR: Incorrect PIN.")
        return

    new_pin = input("  New PIN: ")
    confirm = input("  Confirm PIN: ")

    if not new_pin.isdigit() or len(new_pin) != 4 or new_pin != confirm:
        print("  ERROR: Invalid PIN.")
        return

    account["pin"] = new_pin
    print("  SUCCESS: PIN changed.")

def login():
    divider("=")
    slow_print("  WELCOME TO NATIONAL BANK ATM")
    divider("=")
    print(timestamp())
    divider()

    for attempt in range(3):
        acc = input("\n  Account Number: ").strip()
        pin = input("  PIN           : ").strip()

        if acc in ACCOUNTS and ACCOUNTS[acc]["pin"] == pin:
            account = ACCOUNTS[acc]
            account["_id"] = acc
            loading("Verifying")
            print(f"\n  Welcome, {account['name']}!")
            return account

        print(f"  ERROR: Invalid credentials ({2-attempt} left)")

    print("\n  CARD BLOCKED.")
    return None

def main():
    account = login()
    if not account:
        return

    while True:
        divider("=")
        print(f"  MAIN MENU | {account['name']}")
        divider("=")
        print("  1. Check Balance")
        print("  2. Deposit")
        print("  3. Withdraw")
        print("  4. Transfer")
        print("  5. Transaction History")
        print("  6. Change PIN")
        print("  7. Exit")
        divider()

        choice = input("  Select option: ").strip()

        try:
            if choice == "1":
                check_balance(account)

            elif choice == "2":
                deposit(account, float(input("  Deposit Rs.: ")))

            elif choice == "3":
                withdraw(account, float(input("  Withdraw Rs.: ")))

            elif choice == "4":
                transfer(account)

            elif choice == "5":
                show_history(account)

            elif choice == "6":
                change_pin(account)

            elif choice == "7":
                divider("=")
                slow_print("  Thank you. Goodbye!")
                divider("=")
                break

            else:
                print("  ERROR: Invalid option.")

        except:
            print("  ERROR: Invalid input.")

if __name__ == "__main__":
    main()