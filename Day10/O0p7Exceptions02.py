

class TooTiny(Exception):
    pass

class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

try:
    age = int(input("Enter the age :"))

    if age < 7:
        raise TooTiny("The person is too tiny to cast his vote....")
    elif age < 18:
        raise TooYoung("The person is too young to cast the vote...")
    elif age > 100:
        raise TooOld("The person os too old to cast the vote...")
except TooTiny as t:
    print(t.__class__)
    print(t)

except TooYoung as y:
    print(y.__class__)
    print(y)
except TooOld as o:
    print(o.__class__)
    print(o)
else:
    print("You can cast your vote....")

finally:
    print("Completed the task of voting.....")

