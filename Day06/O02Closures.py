
def outerFun():
    gname = "Sachin"

    def innerFun():

        print("Hello World")
        print(f"Greetings Mr.{gname}")

    return innerFun

outerFun()()            # calls the innerfun

print("-" * 60)
import math
print(math.__name__)
print(outerFun.__name__)
print(outerFun().__name__)

print("-" * 60)
inref = outerFun()
# after few lines of code
print("Hello World \n" * 5)

print("-" * 60)
inref()         # calls the innerFun
