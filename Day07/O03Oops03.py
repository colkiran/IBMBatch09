
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 35
        print("Player Initialized.....")

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")

    def __del__(self):
        print("object destroyed.....")

ply1 = Player()
ply1.get_details()

print("-" * 60)

ply2 = Player()
ply2.name = "Rahul"
ply2.age =  32
ply2.get_details()

print("-" * 60)
del ply1

print("-" * 60)