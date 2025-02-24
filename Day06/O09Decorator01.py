
def funLogger(fnc):

    def helper(x, y):
        print("My info logged in a service")
        res = fnc(x, y)
        print("My Info channel closed")
        print("-" * 60)
        return res
    return helper


@funLogger
def add(x, y):
    print("add func called....")
    return x + y
@funLogger
def sub(x,y):
    print("Substract Fun called....")
    return x - y


add(32, 83)

sub(80, 68)