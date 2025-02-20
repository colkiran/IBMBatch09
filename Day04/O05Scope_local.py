
def fun(x):         # x is a local variable
    print(f"x inside fun :{x}")
    y = "hello world"       # y is also a local variable
    print(f"y inside fun :{y}")

fun(100)

print("-" * 60)
# print(f"x outside fun :{x}")
# print(f"y outside fun :{y}")
