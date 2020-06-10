import datetime

name = input("Name: ")
age = int(input("Age: "))
n = int(input("Number of copies: "))

now = datetime.datetime.now()
year = now.year - age + 100;
message = "Hi {}, you will be 100 years old in {}.\n".format(name, year)

print(message * n, end='')