import random

exit = False

while not exit:
    num = random.randint(1, 9)
    print("New number generated.")

    while True:
        guessInput = ""

        while not guessInput.isdigit() and guessInput != "exit":
            guessInput = input("Guess a number: ")

        if guessInput == "exit":
            exit = True
            break

        guess = int(guessInput)
        
        if guess < num:
            print("Too low.")
        elif guess > num:
            print("Too high.")
        else:
            print("Exactly right!")
            break


