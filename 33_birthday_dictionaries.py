def print_keys(dictionary):
    for key in dictionary.keys():
        print(key)

if __name__ == "__main__":
    birthdays = {"Albert Einstein": "03/14/1879",
                 "Benjamin Franklin": "01/17/1706",
                 "Ada Lovelace": "12/10/1815"}

    print("Welcome to the birthday dictionary. We know the birthdays of:")
    print_keys(birthdays)

    name = input("Who's birthday do you want to look up?\n")

    if name in birthdays:
        print("{}'s birthday is {}.".format(name, birthdays[name]))
    else:
        print("Sorry we don't know the birthday of {}.".format(name))
