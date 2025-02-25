
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return Employee("Noname", self.salary + other.salary)
        # return self.salary + other.salary

    def __sub__(self, other):
        return Employee("Noname", self.salary - other.salary)

    def __mul__(self, other):
        return Employee("Noname", self.salary * other.salary)

    def __truediv__(self, other):
        return Employee("Noname", self.salary / other.salary)

    def __floordiv__(self, other):
        return Employee("Noname", self.salary // other.salary)


emp1 = Employee("Louis", 150)
emp2 = Employee('Mark', 100)

print(emp1)
print("-" * 60)
print(emp2)

print("-" * 60)
print(f"add :{emp1 + emp2}")

print("-" * 60)
print(f"sub :{emp1 - emp2}")

print("-" * 60)
print(f"mul :{emp1 * emp2}")

print("-" * 60)
print(f"div :{emp1 / emp2}")

print("-" * 60)
print(f"flr_div :{emp1 // emp2}")

print("-" * 60)
emp3 = Employee("Harry", 250)
emp4 = Employee("Mike", 175)

print(f"emp1 + emp2 + emp3 + emp4 = {emp1 + emp2 + emp3 + emp4}")
