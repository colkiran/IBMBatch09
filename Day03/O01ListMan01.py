
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.0, 6.1, 7.8, 8.3, 9+2j, 10-3j, 'eleven', 'twelve', 'thirteen', 'fourteen', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
values = list(range(10, 32, 10))
print(f"values :{values}")

# upack a list
a, b, c = values
print(f"a = {a}, b = {b}, c = {c}")

values = list(range(10, 101, 10))
print(f"values :{values}")
# *c can accept more than one value
a, b, *c = values
print(f"a = {a}, b = {b}, c = {c}")

print("-" * 60)
a, *b, c = values
print(f"a = {a}, b = {b}, c = {c}")

print("-" * 60)
*a, b, c = values
print(f"a = {a}, b = {b}, c = {c}")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(f"len(lst3) :{len(lst3)}")
print(f"lst3 :{lst3}")

print("-" * 60)
lst4 = [*lst1, *lst2]
print(f"len(lst4) :{len(lst4)}")
print(f"lst4 :{lst4}")

print("-" * 60)
# enumerate

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"letters  :{letters}")

for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0],  "\t", letter[1])

print("-" * 60)
for index, letter in enumerate(letters):
    print(index, "\t", letter)

print("-" * 60)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 60)
for lst in mylist:
    print(lst)

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(f"{ind} \t {lst}")

print("-" * 60)
for ind, lst in enumerate(mylist):
    print(f"list({ind})")
    for idx, num in enumerate(lst):
        print(f" \t {idx} \t {num}")