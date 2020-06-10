def is_valid(user_input):
    return (len(user_input) == 3 and 
            user_input[1] == ',' and 
            '1' <= user_input[0] <= '3' and 
            '1' <= user_input[2] <= '3')

def get_coordinate():
    user_input = ""
    while not is_valid(user_input):
        user_input = input("Move [row,col]: ")
    tokens = user_input.strip().split(',')
    return int(tokens[0]) - 1, int(tokens[1]) - 1

def print_game(game):
    chars = [' ', 'X', 'O']
    display = "\n --- --- --- \n"
    for row in game:
        row_display = [chars[i] for i in row]
        display += "| {} | {} | {} |\n".format(*row_display)
        display += " --- --- --- \n";
    print(display)

if __name__ == "__main__":
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    is_player_one = True
    move_count = 0

    while move_count < 9:
        move_count += 1

        print_game(game)

        if is_player_one:
            print("Player 1.")
        else:
            print("Player 2.")

        coord = get_coordinate()
        while game[coord[0]][coord[1]] != 0:
            coord = get_coordinate()

        game[coord[0]][coord[1]] = 1 if is_player_one else 2

        is_player_one = not is_player_one
    
    print_game(game)
    print("Game over.")
