
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = '1 yr'

    def eat(self):
        print("Animals eat.....")


class Bird(Animal):

    def fly(self):
        print("Birds fly....")

class Fish(Animal):

    def swim(self):
        print("Fishes swim....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)

dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 60)
print(f"Cuckoo :{cuckoo.__dict__}")
print(f"Dolphin L{dolphin.__dict__}")
