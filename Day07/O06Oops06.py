
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @staticmethod
    def calcAvg(runs, balls):
        avg = (runs / balls) * 100
        return f"{round(avg, 2)}"

ply1 = Player("Virat", 32)
ply1.get_details()

print("-" * 60)
ply1.runs = 168
ply1.balls = 130

print(f"Average :{Player.calcAvg(ply1.runs, ply1.balls)}")

