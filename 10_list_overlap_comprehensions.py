import random

a = random.sample(range(1, 100), random.randint(1, 20))
b = random.sample(range(1, 100), random.randint(1, 20))

print([x for x in set(a) if x in b])
