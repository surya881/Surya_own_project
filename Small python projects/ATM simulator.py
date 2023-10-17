class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance


def main():
    atm = ATM()

    print("Welcome to the ATM")
    print("------------------")

    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            balance = atm.check_balance()
            print("Your balance is: ${:.2f}".format(balance))
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            balance = atm.deposit(amount)
            print("Deposited ${:.2f}".format(amount))
            print("Your new balance is: ${:.2f}".format(balance))
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            balance = atm.withdraw(amount)
            if isinstance(balance, str):
                print(balance)
            else:
                print("Withdrawn ${:.2f}".format(amount))
                print("Your new balance is: ${:.2f}".format(balance))
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    print("Thank you for using the ATM!")


if __name__ == '__main__':
    main()