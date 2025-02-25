
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


emp1 = Employee('steeve', 34)
print(emp1)

print("-" * 60)
print(len(emp1))

print("-" * 60)
print([e1 for e1 in emp1])
