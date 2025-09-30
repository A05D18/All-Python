"""Create SavingsAccount as sub class of account - additional field (type - personal/corporate etc)
implement withdraw and deposit such that
- maximum upto 1 lakh can be deposited in an account at a time
- Min balance 5000 must be maintained while withdrawal (if type = corporate you withdraw full amount = balance)"""

from Account import account


class SavingsAccount(account):
    def __init__(self, acc_id, name, balance, acctype="saving"):
        super().__init__(acc_id, name, balance)
        self.acctype = acctype
        self.min_balance = 5000
        self.max_limit = 100000

    def withdraw(self, amount):
        if self.acctype == "savings":
            if self.balance > self.min_balance and self.balance - amount > self.min_balance:
                return self.balance - amount
            else:
                return f"Low balance cannot withdraw,balance is: {self.balance}"
        elif self.acctype == "corporate":
            if self.balance - amount > 0:
                return self.balance - amount
            else:
                return f"Low balance you can withdraw upto: {self.balance}"
        else:
            return "Invalid account type"

    def deposit(self, amount):
        if amount <= self.max_limit:
            return self.balance + amount
        else:
            return f"Cannot deposit more than {self.max_limit} at a time"
