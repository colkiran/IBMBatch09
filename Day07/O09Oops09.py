"""
overloading comparison operators

1. overload == operator (mandatory)
2. overload any one comparison operator (>)

we can use a decorator @total_ordering that will automatically overload all comparison operators
"""
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    # type conversion operator
    def __str__(self):
        return f"Name is {self.name}\nAge is {self.salary}"


    # this will automatically over load !=  not equal to also
    def __eq__(self, other):
        return self.salary == other.salary

    # this will automatically over load < less than also
    def __gt__(self, other):
        return self.salary > other.salary



emp1 = Employee('Jack', 35000)
print(emp1)

print("-" * 60)

emp2 = Employee("Tom", 36000)
print(emp2)

print("-" * 60)

if (emp1 != emp2):
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is  equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
if (emp1 < emp2):
    print("{}'s salary of {} is less than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is greater than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
print(emp1 >= emp2)
print(emp1 <= emp2)
