
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print('-' * 60)
t2 = (1, 2, 3.5, 4.2, 6+1j, 7-5j, 'eight', 'nine', True, False)
print(f"t2 :{t2}")
print(type(t2))

print('-' * 60)
t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print('-' * 60)
t4 = 10,
print(f"t4 :{t4}")
print(type(t4))

print('-' * 60)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print('-' * 60)
# tuples are immutable
t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")

# print(f"t1[2] :{t1[2]}")
# t1[2] = 300

l1 = list(t1)
print(f"l1 :{l1}")
l1[2] = 300

l1.extend([6, 7, 8])
print(f"l1 :{l1}")
print(type(l1))

t1 = tuple(l1)
print(f"t1 :{t1}")
print(type(t1))

print('-' * 60)
# print(dir(t1))  - count, index

t1 = (1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2)
print(f"t1 :{t1}")
print(type(t1))

print('-' * 60)
# count
print(f"1 :{t1.count(1)}")
print(f"2 :{t1.count(2)}")
print(f"3 :{t1.count(3)}")

print('-' * 60)
# index
print("first 3  :", t1.index(3))
print("second 3 :", t1.index(3, t1.index(3) + 1))
print("third 3  :", t1.index(3, t1.index(3, t1.index(3) + 1) + 1))

