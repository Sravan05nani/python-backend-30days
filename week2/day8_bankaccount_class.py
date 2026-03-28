import datetime


class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.history = []

    def _log(self, action, amount=0):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"{time} - {action} ₹{amount}")

    def check_balance(self):
        print(f"\n💰 {self.owner}'s Balance: ₹{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Amount must be positive")
            return
        self.balance += amount
        self._log("Deposited", amount)
        print(f"✅ Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Amount must be positive")
            return
        if amount > self.balance:
            print("❌ Insufficient balance")
        else:
            self.balance -= amount
            self._log("Withdrew", amount)
            print(f"✅ Withdrew ₹{amount}")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("❌ Invalid amount")
            return
        if amount > self.balance:
            print("❌ Not enough balance")
        else:
            self.balance -= amount
            other_account.balance += amount
            self._log(f"Transferred to {other_account.owner}", amount)
            other_account._log(f"Received from {self.owner}", amount)
            print(f"🔁 Transferred ₹{amount} to {other_account.owner}")

    def show_history(self):
        print("\n📜 Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for record in self.history:
                print(record)

    def apply_interest(self, rate=5):
        interest = self.balance * rate / 100
        self.balance += interest
        self._log("Interest Added", interest)
        print(f"📈 Interest ₹{interest:.2f} added")


def authenticate(account):
    for _ in range(3):
        entered_pin = input("Enter PIN: ")
        if entered_pin == account.pin:
            return True
        print("❌ Wrong PIN")
    print("🚫 Too many failed attempts")
    return False


def main():
    acc1 = BankAccount("Nani", 1000, "1234")
    acc2 = BankAccount("Friend", 500, "0000")

    print("🏦 Welcome to SmartBank\n")

    if not authenticate(acc1):
        return

    while True:
        print("\n===== MENU =====")
        print("1️⃣ Check Balance")
        print("2️⃣ Deposit")
        print("3️⃣ Withdraw")
        print("4️⃣ Transfer")
        print("5️⃣ Transaction History")
        print("6️⃣ Add Interest")
        print("7️⃣ Exit")

        choice = input("Choose option: ")

        try:
            if choice == "1":
                acc1.check_balance()

            elif choice == "2":
                amount = float(input("Enter amount: "))
                acc1.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter amount: "))
                acc1.withdraw(amount)

            elif choice == "4":
                amount = float(input("Enter amount to transfer: "))
                acc1.transfer(acc2, amount)

            elif choice == "5":
                acc1.show_history()

            elif choice == "6":
                acc1.apply_interest()

            elif choice == "7":
                print("👋 Exiting... Bye!")
                break

            else:
                print("❌ Invalid choice")

        except ValueError:
            print("❌ Enter a valid number")


if __name__ == "__main__":
    main()