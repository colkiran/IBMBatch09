
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def CheckBalance(self):
        pass

    def withDraw(self):
        pass

    def Deposit(self):
        pass

class Savings(Account):

    def Deposit(self):
        print("Amout debitted into the account successfully....")

    def CheckBalance(self):
        print("Balance in the account is ######.##")

sav = Savings()
sav.Deposit()
sav.CheckBalance()
