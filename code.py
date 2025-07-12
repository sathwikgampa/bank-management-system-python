# Simple Bank Management System in Python

class BankAccount:
    def __init__(self, name, acc_number):
        self.name = name
        self.acc_number = acc_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.acc_number}")
        print(f"Available Balance: ₹{self.balance:.2f}")

# Main Menu
def main():
    print("=== Welcome to Simple Bank Management System ===")
    name = input("Enter account holder's name: ")
    acc_number = input("Enter account number: ")
    account = BankAccount(name, acc_number)

    while True:
        print("\n------ Menu ------")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            account.display_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Thank you for using the Bank Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

# Run the program
if __name__ == "__main__":
    main()
