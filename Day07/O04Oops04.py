"""
self - will have the name of the object that called the method

instance variables are stored in a dictionary __dict__, the dictionary is present in the object

"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized.....")

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 35)
ply1.get_details()

print("-" * 60)

ply2 = Player("Rahul", 32)
ply2.get_details()

print("-" * 60)
print(f"ply1 :{ply1.__dict__}")
print(f"ply2 :{ply2.__dict__}")

print("-" * 60)
ply2.runs = 60
print(f"ply2 :{ply2.__dict__}")
print(f"ply1 :{ply1.__dict__}")
