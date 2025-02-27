
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's job.......")

class Developer(Employee):

    def doJob(self):
        print("Coding job......")


def BankFunJob(emp):
    print("Bank job started.....")
    emp.doJob()
    print("Bank job ended......")
    print("-" * 60)

mike = Manager()
david = Developer()

BankFunJob(mike)
print("-" * 60)

BankFunJob(david)
