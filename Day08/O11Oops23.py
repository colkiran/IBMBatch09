# duck types

class Manager:

    def doJob(self):
        print("Managers job......")


class Developer:

    def doJob(self):
        print("Developer job.....")


def BankFunJob(emps):
    print("Bank job started")
    for emp in emps:
        emp.doJob()
    print("Ending".center(60, "-"))
    print("-" * 60)

mike = Manager()
david = Developer()

BankFunJob([mike, david])
