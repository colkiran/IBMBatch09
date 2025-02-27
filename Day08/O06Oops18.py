
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10


    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def __init__(self):         # overriding the parent class Ctor
        super().__init__()      # calls the parent class Ctor
        print("Bird Ctor....")
        self.b = 20

    def fly(self):
        print("Birds Fly......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)
print(f"cuckoo :{cuckoo.__dict__}")
