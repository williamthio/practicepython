from collections import defaultdict

def get_category(line):
    tokens = line.split("/")
    return "/".join(tokens[2:-1])

if __name__ == "__main__":
    lines = []
    with open("Training_01.txt", "r") as open_file:
        lines = open_file.read().split("\n")

    d = defaultdict(int)    
    for line in lines:
        if len(line) == 0:
            continue
        category = get_category(line)
        d[category] += 1

    print(d.items())
