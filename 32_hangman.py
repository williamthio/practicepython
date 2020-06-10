import random

def random_line(filename):
    with open(filename, 'r') as f:
        line = next(f)
        for num, candidate_line in enumerate(f, 2):
            if random.randrange(num): 
                continue
            line = candidate_line
        return line

def get_letter():
    letter = "1"
    while len(letter) != 1 or letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letter = input("Guess your letter: ").upper()
    return letter

def get_guessed_display(word, guessed):
    return " ".join([c if c in guessed else "_" for c in word])

def get_hangman_display(incorrect_count):
    return ("     ____\n"
            "     |  |\n"
            "     {0}  |\n"
            "    {2}{1}{3} |\n"
            "    {4} {5} |\n"
            "    =====").format("O" if incorrect_count > 0 else " ",
                    "|" if incorrect_count > 1 else " ", 
                    "/" if incorrect_count > 2 else " ", 
                    "\\" if incorrect_count > 3 else " ", 
                    "/" if incorrect_count > 4 else " ", 
                    "\\" if incorrect_count > 5 else " ")

def get_play_again():
    play_again = ""
    while play_again not in ["yes", "no"]:
        play_again = input("Play again [yes|no]: ")
    return play_again

def new_game():
    word = random_line('sowpods.txt').strip()
    used = set()
    guessed = set()
    guessed_display = get_guessed_display(word, guessed)
    incorrect_count = 0

    print(guessed_display)

    while "_" in guessed_display and incorrect_count < 6:
        letter = get_letter()
        if letter in used:
            print("Letter {} is already used.".format(letter))
        elif letter not in word:
            incorrect_count += 1
            print(get_hangman_display(incorrect_count))
            print("Incorrect!")
        else:
            guessed.add(letter)
            guessed_display = get_guessed_display(word, guessed)
            print(guessed_display)
        used.add(letter)

if __name__ == "__main__":
    print("Welcome to Hangman!")
    play_again = "yes"
    while play_again == "yes":
        new_game()
        play_again = get_play_again()
