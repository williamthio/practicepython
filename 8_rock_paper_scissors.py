moves = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

winner = None
while winner == None:
    moveOne, moveTwo = "", ""

    while moveOne not in moves:
        moveOne = input("Player 1 [rock|paper|scissors]: ")
    while moveTwo not in moves:
        moveTwo = input("Player 2 [rock|paper|scissors]: ")

    if moves[moveOne] == moveTwo:
        winner = "Player 1"
    elif moves[moveTwo] == moveOne:
        winner = "Player 2"

print("Congratulations! {} wins the game.".format(winner))    
