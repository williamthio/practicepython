import random

def random_line(filename):
    with open(filename, 'r') as f:
        line = next(f)
        for num, candidate_line in enumerate(f, 2):
            if random.randrange(num): 
                continue
            line = candidate_line
        return line

if __name__ == "__main__":
    print(random_line("sowpods.txt"))
