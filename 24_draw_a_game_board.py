def get_vertical_separator(n):
    return "---".join(" " * (n + 1))

def get_horizontal_separator(n):
    return "   ".join("|" * (n + 1))

if __name__ == "__main__":
    board_size = int(input("Board size: "))
    lines = [get_vertical_separator(board_size)]

    for _ in range(board_size):
        lines.append(get_horizontal_separator(board_size))
        lines.append(get_vertical_separator(board_size))

    display = "\n".join(lines)

    print(display)
