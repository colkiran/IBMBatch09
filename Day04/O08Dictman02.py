
# keys
print("keys".center(60, "-"))
d1 = {1:'a', 2 :'b' , 3: 'c', 4: 'd' ,5:'f'}
print(f"d1 :{d1}")

print("-" * 60)
ky = d1.keys()
print(f"Keys :{ky}")

print("-" * 60)
for ky in d1.keys():
    print(ky, "=>", d1[ky])

print("values".center(60, "-"))
player = {'name': 'Sachin', 'age': 35, 'runs': 89, 'oppnt': 'WI'}
print(f"player :{player}")

print("-" * 60)
vl = player.values()
print(f"values :{vl}")

print("items".center(60, "-"))
# items is a combination of keys and values

emp = {
    'emp1': {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR', 'dept': 'MKT', 'salary': 110000},
    'emp2': {'empid': 'EMP223', 'ename': 'Grace', 'age': 30, 'desig': 'TL', 'dept': 'finance', 'salary': 125000},
    'emp3': {'empid': 'EMP333', 'ename': 'John', 'age': 26, 'desig': 'SE', 'dept': 'IT', 'salary': 85000}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(v))
    print("-" * 60)

print("get".center(60, "-"))

emp1 = {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR', 'dept': 'MKT', 'salary': 110000}
print(f"emp1 :{emp1}")
# print(type(emp1))

print("-" * 60)
print(f"Name        :{emp1.get('ename', 'Invalid Key, Please enter a valid key')}")
print(f"Designation :{emp1.get('desg', 'Invalid Key, Please enter a valid key')}")

print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cities :{cities}")

print("-" * 60)
res1 = dict.fromkeys(cities)               # values will be None
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 24)
print(f"res :{res2}")

print("setdefault".center(60, "-"))
# setdefualt - will only add new key, value. will not modify the existing one

emp1 = {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR', 'dept': 'MKT', 'salary': 110000}
print(f"emp1 :{emp1}")

print("-" * 60)
# modifying
emp1.setdefault('ename',  'Mitchel')
emp1.setdefault('desig', 'PM')

# add new
emp1.setdefault('city',  'Johanesberg')
emp1.setdefault('exp',  '14 yrs')

print(f"emp1 :{emp1}")



