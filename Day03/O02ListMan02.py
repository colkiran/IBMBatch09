
# CRUD
# create
l1 = list(range(1, 11))
print(f"l1 :{l1}")

print("-" * 60)
# read

# indexing
print(f"l1[2] :{l1[2]}")
print(f"l1[6] :{l1[6]}")
print(f"l1[-1] :{l1[-1]}")

print("-" * 60)
# iterate through the list

for i in l1:
    print(i, end=" ")
print()

print("-" * 60)

for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

print("-" * 60)
# update - modify, add new values
print(f"l1 :{l1}")

# modify
print(f"l1[2] :{l1[2]}")
l1[2] = 300

print(f"l1[6] :{l1[6]}")
l1[6] = 789

print(f"l1 :{l1}")

# add new value
print(f"l1[4] :{l1[4]}")
l1[4] = 450

print(f"l1[8] :{l1[8]}")
l1[8] = 750

print(f"l1 :{l1}")

print("-" * 60)
# lists are static
# delete
print(f"l1 :{l1}")
del l1[4]
del l1[-1]

print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))
