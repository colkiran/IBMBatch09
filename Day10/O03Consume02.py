
import mypackage.mymodule as md
from mypackage.mymodule import greet, Player, outerFun


# print the variable
print(f"gname :{md.gname}")
print("-" * 60)

print(f"sports :{md.sports}")
print("-" * 60)

print(f"runs :{md.runs}")
print("-" * 60)

greet("Virat Kholi")
print("-" * 60)

ply1 = Player("Rohit", 38)
print(ply1)

print("-" * 60)
# outerfun is a decorator

@outerFun
def add(x, y):
    print(f"adding {x} and {y}")
    return x + y

@outerFun
def multiply(x, y):
    print(f"product of {x} and {y}")
    return x * y

add(38, 84)
multiply(12, 5)
