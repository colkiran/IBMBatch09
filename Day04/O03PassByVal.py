
# pass by value - data type - immutable data

def fun(x):
    print(f"x inside before :{x}")
    x += 50
    print(f"x inside after  :{x}")

y = 10
print(f"y before :{y}")

fun(y)

print(f"y after :{y}")
