n=0
for i in range(50, 151):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        n += 1
        print(i, end=" ")

print(f"\nThere are {n} prime numbers between 150 and 50")
