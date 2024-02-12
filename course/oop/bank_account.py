
from typing import Self

class BankAccount:

    def __init__(self, name:str='John', balance:float=1000):
        self.name = name
        self.balance = balance

    def deposit(self, amount:float):
        self.balance += amount

    def withdraw(self, amount:float):
        if amount > self.balance:
            raise Exception('Vous n\'avez passez sur le compte')
        else:
            self.balance -= amount

    def transfer(self, other:Self, amount:float):
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self) -> str:
        return f'Titulaire : {self.name} - Solde : {self.balance}'
    
    @staticmethod
    def get_class_name():
        return 'BankAccount'

if __name__ == '__main__':
    john_account = BankAccount()
    marie_account = BankAccount('Marie', 2200)
    print(BankAccount.get_class_name())