import json
import datetime

def print_keys(dictionary):
    for key in dictionary.keys():
        print(key)

def print_name_list(birthdays):
    print("We know the birthdays of:")
    print_keys(birthdays)

def load_birthdays():
    with open("birthdays.json", "r") as f:
        return json.load(f)

def save_birthdays(birthdays):
    with open("birthdays.json", "w") as f:
        json.dump(birthdays, f)

def get_action():
    action = ""
    while action not in ["add", "view", "quit"]:
        action = input("What do want to do? [add|view|quit]\n")
    return action

def validate_birthday(birthday):
    try:
        datetime.datetime.strptime(birthday, "%m/%d/%Y")
        return True
    except ValueError:
        return False

def get_birthday():
    birthday = ""
    while not validate_birthday(birthday):
        birthday = input("Scientist's birthday [MM/DD/YYYY]: ")
    return birthday

def user_add(birthdays):
    name = input("Scientist's name: ")
    birthday = get_birthday()
    birthdays[name] = birthday
    print_name_list(birthdays)

def user_view(birthdays):
    name = input("Who's birthday do you want to look up?\n")
    if name in birthdays:
        print("{}'s birthday is {}.".format(name, birthdays[name]))
    else:
        print("Sorry we don't know the birthday of {}.".format(name))

if __name__ == "__main__":
    birthdays = load_birthdays()

    print("Welcome to the birthday dictionary.")
    print_name_list(birthdays)
    
    action = ""
    while action != "quit":
        action = get_action()
        if action == "add":
            user_add(birthdays)
        elif action == "view":
            user_view(birthdays)
    
    save_birthdays(birthdays)
