
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'age': 35, 'runs': 120, 'oppnt': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'rahul'), ('age', 32), ('runs', 89), ('oppnt', 'Eng')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='Virat', age=30, runs=54, oppnt='WI')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD

# create
player = {'name': 'Sachin', 'age': 34, 'runs': 98, 'oppnt': 'WI'}
print(f'player :{player}')

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
# iterate through the dictionary - we get all keys

for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update  - modify, add new key val pair
print(f"player :{player}")
player['name'] = 'Tendulkar'
player['runs'] = 105

# add new key value
player['venue'] = 'sabina park'
player['year'] = 2003

print(f"player :{player}")

print("-" * 60)
# del

del player['oppnt']
del player['age']

print(f"player :{player}")

print("-" * 60)
print(dir(player))

