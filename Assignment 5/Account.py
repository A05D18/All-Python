"""Q.2 Create an Account class Heirarchy
Account with super class (acc_id, name, balance)
methods - withdraw and deposit"""
from abc import ABC, abstractmethod


class account(ABC):
    def __init__(self, acc_id: int, name: str, balance: float):
        self.acc_id = acc_id
        self.name = name
        self.balance = balance

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass
