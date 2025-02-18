
for i in range(5, 0, -1):
    print(" " * (6-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(2, 6):
    print(" " * (6-i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
