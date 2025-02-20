
glbX = 100

def fun(x):                 # x is a local variable
    global glbX             # do not assing any value in this line
    print(f"x :{x}")
    glbX = 500
    print(f"glbX inside fun :{glbX}")



print(f"before the function call :{glbX}")

fun(10)

print(f"After the function call :{glbX}")
