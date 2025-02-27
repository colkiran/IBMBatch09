
class Employee:

    def __init__(self, name):
        self.__name = name
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular JS', 'React JS']

    def __str__(self):
        return self.__name + " - " + " ".join([str(v) for v in self.tech])

emp1 = Employee("Jack")
print(emp1)
print("-" * 60)

# print(emp1.__name)
# print(emp1.__dict__)
emp1._Employee__name = "Mark"
print(emp1)

