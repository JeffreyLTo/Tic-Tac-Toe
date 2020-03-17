

#define Board
def print_board(zero, one, two, three, four, five, six, seven, eight, nine):
    print("\t\t|\t\t  |")
    print("\t" + one + "\t|\t" + two + "\t""  |  " + three)
    print("\t\t|\t\t  |")
    print("----------------------------")
    print("\t\t|\t\t  |")
    print("\t" + four + "\t|\t" + five + "\t  |  " + six)
    print("\t\t|\t\t  |")
    print("----------------------------")
    print("\t\t|\t\t  |")
    print("\t" + seven + "\t|\t" + eight + "\t  |  " + nine)
    print("\t\t|\t\t  |")


# Define win check
def winchk(player, board):
    if board[1] == player and board[2] == player and board[3] == player:
        return True
    elif board[4] == player and board[5] == player and board[6] == player:
        return True
    elif board[7] == player and board[8] == player and board[9] == player:
        return True
    elif board[1] == player and board[7] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[3] == player and board[6] == player and board[9] == player:
        return True
    elif board[1] == player and board[5] == player and board[9] == player:
        return True
    elif board[3] == player and board[5] == player and board[7] == player:
        return True
    else:
        return False



# Define the player
player2 = None
player1 = input("Player 1 please pick a marker: X or O")
while player1.lower() != "x" and player1.lower() != "o":
    print("Please enter a valid value")
    player1 = input("Please pick a marker: X or O")


if player1.lower() == 'x':
    print("Player 2 will be o")
    player2 = 'o'
else:
    print("Player 2 will be x")
    player2 = 'x'

#player 1 to start
activePlayer = player1


# define board
b = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']



# boolean to check for winner
winner = False

while not winner:
    # Define position to play
    position = int(input("Please enter a number from 1-9"))
    while (position not in range(1, 10)) or (b[position] == 'x' or b[position] == 'o'):
        print("Please enter a number from 1 to 9")
        position = int(input("Please enter a number from 1-9"))

    if activePlayer == player1:
        b[position] = player1
        position = None
        winner = winchk(activePlayer, b)
        if(winner):
            print("Player 1 Wins")
            break
        activePlayer = player2
    else:
        b[position] = player2
        position = None
        winner = winchk(activePlayer, b)
        if(winner):
            print("Player 2 Wins")
            break
        activePlayer = player1

    print_board(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9])


