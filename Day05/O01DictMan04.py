# emp = {
#     'emp1': {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR', 'dept': 'MKT', 'salary': 110000},
#     'emp2': {'empid': 'EMP223', 'ename': 'Grace', 'age': 30, 'desig': 'TL', 'dept': 'finance', 'salary': 125000},
#     'emp3': {'empid': 'EMP333', 'ename': 'John', 'age': 26, 'desig': 'SE', 'dept': 'IT', 'salary': 85000}
# }


print("update".center(60, "-"))
emp1 =  {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR',  'salary': 110000}
emp2 = {'empid': 'EMP223', 'ename': 'Grace', 'age': 30,  'dept': 'finance', 'salary': 125000}

print(f"emp1 :{emp1}")
print("-" * 60)

print(f"emp2 :{emp2}")

print("-" * 60)
emp1.update(emp2)
print(f"emp1 :{emp1}")

print("copy".center(60, "-"))
emp1 =  {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR'}

print(f"emp1 before :{emp1}")

# copy the dictionary emp1 to emp2
emp2 = emp1       # shallow copy - we share the address with the data

print(f"emp2 after :{emp2}")
emp2['dept'] = 'Finance'
emp2['salary'] = 145000

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 60)

emp1 =  {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR'}
print(f"emp1 before :{emp1}")

# copy emp1 to emp2
emp2 = emp1.copy()      # deep copy - only data gets copied
print(f"emp2 before :{emp2}")

emp2['dept'] = 'Finance'
emp2['salary'] = 145000

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 60)
emp1 =  {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': {'wipro': 'FT', 'ibm': 'FE', 'Benz': 'TL'}}
print(f"emp1 before :{emp1}")

# copy emp1 to emp2
emp2 = emp1.copy()      # deep copy - only data gets copied
print(f"emp2 before :{emp2}")

emp2['desig']['TCS'] = 'FM'
emp2['desig']['CTS'] = 'SM'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 60)
emp1 =  {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': {'wipro': 'FT', 'ibm': 'FE', 'Benz': 'TL'}}
print(f"emp1 before :{emp1}")

# copy emp1 to emp2
from copy import deepcopy
emp2 = deepcopy(emp1)     # deep copy - only data gets copied
print(f"emp2 before :{emp2}")

emp2['desig']['TCS'] = 'FM'
emp2['desig']['CTS'] = 'SM'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("clear".center(60, "-"))

emp1 =  {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': {'wipro': 'FT', 'ibm': 'FE', 'Benz': 'TL'}}
print(f"emp1 before :{emp1}")

print("-" * 60)
emp1.clear()

print(f"emp1 :{emp1}")

