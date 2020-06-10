import random

a = [random.randint(1, 100) for x in range(1, random.randint(1, 20))]
b = [random.randint(1, 100) for x in range(1, random.randint(1, 20))]

print(list(set(a) & set(b)))
