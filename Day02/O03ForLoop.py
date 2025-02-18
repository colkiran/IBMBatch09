
for i in range(1, 11):
    print(i, end=" ")
print()             # prints a new line

print(f"after :{i}")

print("-" * 60)

for j in range(i, 0, -1):
    print(j, end=" ")
print()

print("-" * 60)

for i in range(1, 31):
    # if i > 20:
    #     break               # exit the iteration
    if i % 2 == 0:
        continue            # skip the iteration
    print(i, end=" ")
else:
    print("\nCompleted generation of numbers.....")

