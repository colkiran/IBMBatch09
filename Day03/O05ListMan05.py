"""
sort    -   sort will sort the original list
sorted  -   sorted will take a copy of the list, sorts it and returns it
"""

l1 = [8, 5, 10, 1, 9, 3, 2, 6, 7, 4]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending order  :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending order :{res_desc}")

print("-" * 60)

l1 = [8, 'zebra', 5, 'apple', 'yellow', 10, 'blue', 'white', 1, 'green', 'violet', 9, 'red', 'maroon', 3, 'pink', 2, 'orange', 'cat',  6, 'egg', 7, 'dog', 4, 'strawberry', 'frog', 129, 1459, 29, 261, 2301]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key = ascii)
print(f"res :{res}")

for i in range(0, len(res)):
    if type(res[i]) == int:
        print(i)
        break

print("-" * 60)
print(res[:i] + sorted(res[i:]))

print("-" * 60)
cities = ['thiruvananthapuram', 'pune', 'bangalore', 'delhi', 'chennai', 'vishakapatnam', 'mysore', 'ooty', 'hyderabad', 'mumbai', 'kolkata']

print(f"cities :{cities}")

print("-" * 60)
# sort the cities based on their length of name
res_asc = sorted(cities, key=len)
print(f"Ascending order :{res_asc}")

