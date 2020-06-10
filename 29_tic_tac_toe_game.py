def is_valid_coord(user_input):
    return (len(user_input) == 3 and 
            user_input[1] == ',' and 
            '1' <= user_input[0] <= '3' and 
            '1' <= user_input[2] <= '3')

def get_coord():
    user_input = ""
    while not is_valid_coord(user_input):
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

def check_winner(game):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2]:
            return game[i][0]
        elif game[0][i] == game[1][i] == game[2][i]:
            return game[0][i]
    if game[0][0] == game[1][1] == game[2][2]:
        return game[0][0]
    elif game[0][2] == game[1][1] == game[2][0]:
        return game[0][2]
    return 0

def get_play_again():
    play_again = ""
    while play_again not in ["yes", "no"]:
        play_again = input("Play again [yes|no]: ")
    return play_again

def new_game():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    is_player_one = True
    move_count = 0
    winner = 0

    while move_count < 9 and winner == 0:
        move_count += 1

        print_game(game)

        if is_player_one:
            print("Player 1.")
        else:
            print("Player 2.")

        coord = get_coord()
        while game[coord[0]][coord[1]] != 0:
            coord = get_coord()

        game[coord[0]][coord[1]] = 1 if is_player_one else 2

        is_player_one = not is_player_one
        winner = check_winner(game)

    print_game(game)

    if winner == 0:
        print("Draw.")
    else:
        print("Player {} wins.".format(winner))

    return winner

if __name__ == "__main__":
    player_one_score = 0
    player_two_score = 0
    play_again = "yes"

    while play_again == "yes":
        winner = new_game()    

        if winner == 1:
            player_one_score += 1
        elif winner == 2:
            player_two_score += 1

        print("\nPlayer 1 score: {}".format(player_one_score))
        print("Player 2 score: {}".format(player_two_score))
        play_again = get_play_again()
