
# pass by reference - data - list - mutable

def fun(lst):
    print(f"lst inside before :{lst}")
    lst.extend(['richard', 'adam', 'Micheal'])
    print(f"lst inside after :{lst}")

l1 = ['peter', 'kevin', 'keith', 'steve']

print(f"before calling fun l1 :{l1}")

fun(l1)

print(f"after calling fun l1 :{l1}")