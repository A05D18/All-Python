"""Creare user class with user interface that gives 2 menu options
1. Deposit
2. Withdraw"""
from Bank_App import Transaction
from Account import account
from Savings_account import SavingsAccount
from Current_account import CurrentAccount


class user:
    def __init__(self, acc: account):
        self.acc = acc

    def display_menu(self):
        print("\n=== Banking Menu ===")
        print(f"Account ID: {self.acc.acc_id}, Name: {self.acc.name}, Type: {self.acc.acctype}")
        print(f"Current Balance: {self.acc.balance}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-3): "))
                match choice:
                    case 1:
                        print(Transaction.deposit_to_account(self.acc))
                    case 2:
                        print(Transaction.withdraw_from_account(self.acc))
                    case 3:
                        print("Thank you for using the banking system!")
                        exit()
                    case _:
                        print("Invalid choice. Please select 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")


# Main program to demonstrate functionality
if __name__ == "__main__":
    # # Create a SavingsAccount (personal)
    # savings_acc = SavingsAccount(123, "Amar", 10000.00, "savings")
    # user1 = user(savings_acc)
    # print("Starting Savings Account:")
    # user1.run()
    #
    # # Create a SavingsAccount (corporate)
    # corporate_acc = SavingsAccount(124, "Dhundiraj", 20000.00, "corporate")
    # user2 = user(corporate_acc)
    # print("\nStarting Corporate Savings Account:")
    # user2.run()

    # Create a CurrentAccount
    current_acc = CurrentAccount(125, "Pratham", 15000.00, "current")
    user3 = user(current_acc)
    print("\nStarting Current Account:")
    user3.run()
