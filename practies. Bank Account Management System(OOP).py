# Bank Account Management System

from abc import ABC , abstractmethod

class Account(ABC):
    """Abstract base class. cannot be initialize directly."""

    @abstractmethod
    def deposite(self , amount):
        pass

    def withdraw(self , amount):
        pass

# Encapsulation

class BankAccount(Account):

    """A basic account. Balance is private and only changed via methods."""

    def __init__(self , __account_number , __account_name , balance):
        self.__account_number = account_number
        self.__account_name = acoount_name
        self.__balance = balance

    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount

        else:
            print("Deposit amount must be positive.")


    def withdraw(self , amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount

        else:
            print("withdraw failed: invalid amount or insufficient funds.")

    def get_balance(self):

        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def _update_balance(self , new_balance):

        self.__balance = new_balance

# Inheritance

class SavingAccount(BankAccount):

    def __init__(self , account_number , balance = 0 , interest_rate = 4):
        super().__init__(account_number , balance)
        self.interest_rate = interest_rate


    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        return interest


# Polymorphism 

class CurrentAccount(BankAccount):

    def __init__(self, account_number, account_name, balance, overdraft):
        super().__init__(account_number, account_name, balance)
        self.overdraft = overdraft

    def add_interest(self):
        print("Current Overdraft:", self.overdraft)


saving = SavingAccount("101", "Ayush", 10000, 4)
current = CurrentAccount("102", "Man", 15000, 5000)

SavingAccount.show()
CurrentAccount.show()