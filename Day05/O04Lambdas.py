
def add(x, y):
    return x + y

# res = add(10, 20)
# print(f"res :{res}")

a = add

res = a(20, 40)
print(f"res :{res}")

print('-' * 60)
# result_of_exp = lambda v1, v2, v3... : expression

b = lambda x, y: x + y
res = b(90, 100)
print(f"res :{res}")

print('-' * 60)
# lambdas are best used with - map, filter and reduce functions
l1 = list(range(1, 10))
print(f"l1 :{l1}")

squares = list(map(lambda x : x ** 2, l1))

print(f"squares :{squares}")

expenses = [5000, 10000, 8500, 50000, 35000, 145000, 60000, 350000,
            600000]
# convert the expenses from rupees to USD's

USD = list(map(lambda x : round(x/85, 3), expenses))
print(USD)

print('-' * 60)
# filter
l1 = list(range(1, 31))
print(f"l1 :{l1}")
print('-' * 60)

res = list(filter(lambda x : x % 3 == 0, l1))
print(f"res :{res}")

print('-' * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print('-' * 60)
words = list(filter(lambda x: len(x) == 3, sentence.split()))
print(f"words :{words}")

print('-' * 60)
words = list(filter(lambda x: x != 'the', sentence.split()))
print(f"words :{words}")

print('-' * 60)
# reduce
from functools import reduce
l1 = [5, 8, 4, 7, 1, 9, 3, 10, 6, 2]
print(f"l1 :{l1}")

res = reduce(lambda x, y : x if x > y else y, l1 )
print(f"res :{res}")

res = reduce(lambda x, y : x + y, l1)
print(f"res :{res}")
