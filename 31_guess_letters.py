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

if __name__ == "__main__":
    word = random_line('sowpods.txt').strip()
    used = set()
    guessed = set()
    guessed_display = get_guessed_display(word, guessed)

    print("Welcome to Hangman!")
    print(guessed_display)

    while "_" in guessed_display:
        letter = get_letter()
        if letter in used:
            print("Letter {} is already used.".format(letter))
        elif letter not in word:
            print("Incorrect!")
        else:
            guessed.add(letter)
            guessed_display = get_guessed_display(word, guessed)
            print(guessed_display)
        used.add(letter)
