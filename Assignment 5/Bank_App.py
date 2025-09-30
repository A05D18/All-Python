"""Create Bank App with Transaction class
Create Method withdraw_from_account(account : Account)  and deposit_to_account(account : Account)
These methods will return the new balance after deposite/withdraw"""

from Account import account


class Transaction:
    @staticmethod
    def withdraw_from_account(acc: account):
        try:
            amount = float(input("\nEnter the amount to withdraw: "))
            if amount <= 0:
                return "Amount must be positive"
            result = acc.withdraw(amount)
            return f"New balance: {result}"
        except ValueError:
            return "Invalid amount entered"

    @staticmethod
    def deposit_to_account(acc: account):
        try:
            amount = int(input("\nEnter the amount to deposit: "))
            if amount <= 0:
                return "Amount must be positive"
            result = acc.deposit(amount)
            return f"New balance: {result}"
        except ValueError:
            return "Invalid amount entered"
