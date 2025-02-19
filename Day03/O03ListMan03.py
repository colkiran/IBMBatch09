
print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

# print 10, 11 and 12
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("{:-^60}".format("extend"))
l1 = list(range(2, 11, 2))
print(f"l1 :{l1}")

l1.extend([12, 14, 16, 18])
print(f"l1 :{l1}")

l1.extend([20])
print(f"l1 :{l1}")

print("insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

l1.insert(25, 6)
print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

# pop function returns the value that was removed from the list
res = l1.pop(4)
print(f"res :{res}")

res = l1.pop(-1)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 2, 2, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2 ,2, 2, 2]

print(f"l1 :{l1}")

print("-" * 60)
# remove 3
l1.remove(3)
print(f"l1 :{l1}")

print("-" * 60)
while 2 in l1:
    l1.remove(2)

print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

