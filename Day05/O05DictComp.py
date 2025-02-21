
dict1 = {'a': 1,'b': 2, 'c': 3,'d': 4}
print(f"dict1 :{dict1}")

lst2 = {1, 2, 3, 4, 5}
lst1 = [x ** 2 for x in lst2]
print(f"lst1 :{lst1}")

print("-" * 60)
dict2 = {item for item in dict1}
print(f"dict2 :{dict2}")

print("-" * 60)
dict3 = {item for item in dict1.keys()}
print(f"dict3 :{dict3}")

print("-" * 60)
dict4 = {item for item in dict1.values()}
print(f"dict4 :{dict4}")

print("-" * 60)
dict5 = {item for item in dict1.items()}
print(f"dict5 :{dict5}")

print("-" * 60)
dict6 = {k: v for k, v in dict1.items()}
print(f"dict6 :{dict6}")

print("-" * 60)
dict7 = {k: v * 2 for k, v in dict1.items()}
print(f"dict7 :{dict7}")

print("-" * 60)
dict8 = {v * 2: k for k, v in dict1.items()}
print(f"dict8 :{dict8}")

print("-" * 60)
boys = ['mike', 'john', 'peter', 'louis', 'richard']
girls = ['tina', 'grace', 'mary', 'anna', 'aliyah']
dict9 = dict(zip(boys, girls))
print(f"dict9 :{dict9}")

print("-" * 60)
print(list(zip(boys, girls)))

print("-" * 60)
squares = {x: x ** 2 for x in range(1, 11)}
print(f"squares :{squares}")

print("-" * 60)
squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(f"squares :{squares}")

print("-" * 60)
squares = {x: x ** 2 for x in range(1, 11) if x > 5 if x % 2 == 0}
print(f"squares :{squares}")

print("-" * 60)
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"players :{players}")

print("-" * 60)
print(f"Sachin  :{players['sachin']}")

print("-" * 60)
print(f"Sachin :{sum(players['sachin'])}")

print("-" * 60)
res = {k: sum(v) for k, v in players.items()}
print(f"res :{res}")

print("-" * 60)

score = {k: (lambda scores: sum(scores) / len(scores)) (v)
         for k, v in players.items()}
print(f"score :{score}")

print("-" * 60)
scores  = [score for score in players.values()]
print(f"scores :{scores}")

print("-" * 60)
scores = [scr for score in players.values() for scr in score if scr >= 200]
print(f"scores :{scores}")

print("-" * 60)
scores  = {name: [scr for scr in score if scr >= 200]
           for name, score in players.items()}
print(f"scores :{scores}")
