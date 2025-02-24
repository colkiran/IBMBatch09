
def funLogger(fnc):

    def helper():
        print("My Info logged in a service")
        fnc()
        print("My Info logger Channer closed....")

    return helper

def normalFun():
    print("Call me as Normal Function")

print("-" * 60)

funLogger(normalFun)        # no output

print("-" * 60)

funLogger(normalFun)()

print("-" * 60)
res_fun = funLogger(normalFun)
res_fun()

print("-" * 60)
print("-" * 60)
# normalFun before the equals is the name of the variable
normalFun = funLogger(normalFun)
normalFun()         # calls the helper function

print("-" * 60)

@funLogger              # basicFun = funLogger(basicFun)
def basicFun():
    print("I should be called as BASIC")

# basicFun = funLogger(basicFun)
# basicFun()

basicFun()