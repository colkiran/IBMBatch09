
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'dotnet', 'sqlserver', 'Angular JS', 'React JS', 'Ext JS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val


emp1 = Employee("John", 60000)
print(emp1)

print("-" * 60)
print([e1 for e1 in emp1])

print("-" * 60)
emp1.append('Python')
print([e1 for e1 in emp1])

print("-" * 60)
res = emp1[2]
print(f"res :{res}")

print("-" * 60)
emp1[0] = 'C#'
print([e1 for e1 in emp1])
