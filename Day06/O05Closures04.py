
def fun(*args):
    print(args)
    print(*args)            # unpack
    print("-" * 60)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)

print("-" * 60)

def sum(x, y):
    print(f"sum of {x} and {y}")
    return x + y

def diff(x, y):
    print(f"difference of {x} and {y}")
    return x - y

def outerFun(fnc):
    logInfo = "logging into the server...."
    def helper(*args):
        print(logInfo)
        print(fnc(*args))           # call back
        print("-" * 60)

    return helper

sumLogger = outerFun(sum)
sumLogger(10, 20)

diffLogger = outerFun(diff)
diffLogger(80, 38)

