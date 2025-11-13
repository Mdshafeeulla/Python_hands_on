# Exercise 10: OOP – Encapsulation and Methods
#
# Private Attributes
# Implement a class BankAccount with private attribute balance
#
# Deposit Method
# Add a method to deposit funds into the account
#
# Withdrawal Method
# Create a withdrawal method ensuring balance never goes negative
#
# Balance Enquiry
# Implement a method to check the current account balance

class BankAccount():
    def __init__(self,name,balance = 0):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"The deposited amount is {amount}")
            print(f"The new balance is {self.__balance}")
        else:
            print("The amount must be greater than zero")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance :
            self.__balance -= amount
            print(f"The withdrawal amount is {amount}")
            print(f"The new balance is {self.__balance}")

    def inquiry(self):
        print(f"The Total balance is {self.__balance}")

Acc = BankAccount(name = "Shafi")
Acc.deposit(1000)

Acc.withdraw(500)

Acc.inquiry()
