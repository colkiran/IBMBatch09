
# Magic Number

def fact(x):
    x = int(x)
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x-1)


for i in range(1, 50000):
    x = str(i)
    res = 0
    for j in x:
        res += fact(j)
    if int(x) == res:
        print(x, " ")
