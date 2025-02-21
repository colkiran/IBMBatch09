
squares = [x ** 2 for x in range(1, 11)]
print(f"squares :{squares}")

print("-" * 60)

fruits = [
    ('apple', 285),
    ('orange', 120),
    ('grapes', 180),
    ('pineapple', 80),
    ('banana', 65),
    ('watermelon', 50),
    ('gauva', 150),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")

print('-' * 60)

price = ["fruit" for fruit in fruits]
print(f"price :{price}")

print('-' * 60)

price = [fruit for fruit in fruits]
print(f"price :{price}")

print('-' * 60)
price = [fruit[0] for fruit in fruits]
print(f"price :{price}")

print('-' * 60)
price = [fruit[1] for fruit in fruits]
print(f"price :{price}")

print('-' * 60)
price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")

print('-' * 60)
price = [fruit[1] * 0.75 for fruit in fruits]
print(f"price :{price}")

print('-' * 60)
expnsv_frts = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75]
               for fruit in fruits if fruit[1] > 100]
print(f"Expensive fruits :{expnsv_frts}")

print('-' * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

words = [word for word in sentence.split()]
print(f"words :{words}")

print('-' * 60)
words = [word for word in sentence.split() if word != 'the']
print(f"words :{words}")

print('-' * 60)
words = [word for word in sentence.split() if len(word) > 3]
print(f"words :{words}")

print('-' * 60)
boys = ['mike', 'john', 'peter', 'louis', 'richard']
girls = ['tina', 'grace', 'mary', 'anna', 'aliyah']

print(f"boys :{boys}")
print(f"girls :{girls}")

print('-' * 60)

combined = [(boy, girl) for boy in boys for girl in girls]
print(f"combined :{combined}")

print('-' * 60)
st = '1232342p1y2t3h4o5n678'
print(f"st :{st}")
res = [letter for letter in st if letter.isalpha()]
print(f"res :{res}")
