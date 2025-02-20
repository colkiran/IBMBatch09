
print('pop'.center(60,"-"))

emp1 = {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR', 'dept': 'MKT', 'salary': 110000}
print(f"emp1 :{emp1}")

print("-" * 60)

res = emp1.pop('age')
print(f"res :{res}")

res = emp1.pop('dept')
print(f"res :{res}")

# res = emp1.pop()
# print(f"res :{res}")

print(f"emp1 :{emp1}")

print("popitem".center(60, "-"))

emp1 = {'empid': 'EMP134', 'ename': 'Jack', 'age': 38, 'desig': 'MGR', 'dept': 'MKT', 'salary': 110000}
print(f"emp1 :{emp1}")

print("-" * 60)

res = emp1.popitem()
print(f"res :{res}")

res = emp1.popitem()
print(f"res :{res}")

print(f"emp1 :{emp1}")

# update, copy, clear