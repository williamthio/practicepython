def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def get_integer(help_text="Give me a number: "):
    num = ""
    while not num.isdigit():
        num = input(help_text)
    return int(num)

num = get_integer()
if is_prime(num):
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))
