def check_balance(balance):
    print(f"Your current balance is: ₹{balance}")


def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds.")
        return balance
    return balance - amount

def main():
    balance = 1000  # starting balance

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance = deposit(balance, amount)
            print("Deposit successful.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            balance = withdraw(balance, amount)

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()