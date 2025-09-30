"""Create CurrentAccount as sub class of account
implement withdraw and deposit such that
- maximum upto 2 lakh can be deposited in an account at a time
- Min balance 10000 must be maintained while withdrawal"""

from Account import account


class CurrentAccount(account):
    def __init__(self, acc_id, name, balance,  acctype="saving"):
        super().__init__(acc_id, name, balance)
        self.acctype = acctype
        self.min_balance = 10000
        self.max_limit = 200000

    def withdraw(self, amount):
        if self.balance > self.min_balance and self.balance - amount > self.min_balance:
            return self.balance - amount
        else:
            return f"You can withdraw upto {self.balance-self.min_balance}"

    def deposit(self,amount):
        if amount <= self.max_limit:
            return self.balance + amount
        else:
            return f"Cannot deposit more than {self.max_limit} at a time"
