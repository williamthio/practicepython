import random

def get_user_number():
    numString = ""
    while not numString.isdigit() or len(numString) != 4:
        numString = input(">>> ")
    return numString

def get_computer_number():
    return str(random.randint(1000, 9999))

def count_cows_and_bulls(computer, user):
    cows = len(list(filter(lambda c: c[0] == c[1], zip(computer, user))))
    bulls = 4 - cows
    return cows, bulls

if __name__ == "__main__":
    print("Welcome to the Cows and Bulls Game!")
    print("Enter a number:")

    computer = get_computer_number()
    user = ""

    while user != computer:
        user = get_user_number()
        cows, bulls = count_cows_and_bulls(computer, user)
        print("{} cows, {} bulls".format(cows, bulls))

    print("Game over.")

