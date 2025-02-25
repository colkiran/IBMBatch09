class Player:           # Pascal Casing

    def get_runs(self):
        print("runs.....")

sachin = Player()           # calls the constructor (default constructor)
sachin.get_runs()

print("-" * 60)
print(type(sachin))
print(sachin.__class__)

print("-" * 60)
# object is the base class of all classes that we create
print(f"isinstance(sachin, Player) :{isinstance(sachin, Player)}")
print(f"isinstance(sachin, object) :{isinstance(sachin, object)}")
print(f"isinstance('sachin', str)                :{isinstance(sachin, str)}")



