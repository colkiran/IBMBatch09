

def bank_flow(fnc):         # HOF
    print("Logging into the Server......")
    print(fnc.__name__)
    fnc()                   # callback
    print("Logging out of the Server......")
    print("-" * 60)


def withDraw():
    print("Amount debitted from the account.....")

def deposit():
    print("Amount credited into the account.....")

def gift():
    print("Amount transferred.....")


bank_flow(withDraw)
bank_flow(deposit)
bank_flow(gift)

