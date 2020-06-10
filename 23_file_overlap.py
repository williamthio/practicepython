def get_numbers(filename):
    with open(filename, "r") as open_file:
        return [int(num) for num in open_file.read().split("\n")]

if __name__ == "__main__":
    prime_numbers = get_numbers("primenumbers.txt")
    happy_numbers = get_numbers("happynumbers.txt")
    print(list(set(prime_numbers) & set(happy_numbers)))
