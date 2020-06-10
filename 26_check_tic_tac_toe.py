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

if __name__ == "__main__":
    test_cases = [([[2, 2, 0], [2, 1, 0], [2, 1, 1]], 2),
                  ([[1, 2, 0], [2, 1, 0], [2, 1, 1]], 1),
                  ([[0, 1, 0], [2, 1, 0], [2, 1, 1]], 1),
                  ([[1, 2, 0], [2, 1, 0], [2, 1, 2]], 0),
                  ([[1, 2, 0], [2, 1, 0], [2, 1, 0]], 0)]
    for i, case in enumerate(test_cases):
        result = check_winner(case[0]) == case[1]
        print("Case {}: {}".format(i + 1, result))
