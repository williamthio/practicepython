import random

characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

password_type = ""
while password_type not in ["weak", "strong"]:
    password_type = input("Password type: ")

if password_type == "weak":
    n = random.randint(1, 2)
    print("".join(random.sample(words, n)))
else:
    n = int(input("Password length: "))
    print("".join([random.choice(characters) for x in range(n)]))
