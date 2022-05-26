import random

# print the game board
# tic-tac-toe board design

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"
         ]
player_one = "O"
current_player = "X"
winner = None
game_running = True


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("_________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("_________")
    print(board[6] + " | " + board[7] + " | " + board[8])


print_board(board)


# takes the player input
def player_input(board, player_one=None):
    user_input = int(input("Select a board spot 1-9: "))
    if board[user_input - 1] == "_":
        board[user_input - 1] = current_player
    else:
        print("Board spot already taken, please choose another spot.")
    if current_player != "X" and player_one != "O":
        print("that is not a valid space.")
    elif current_player == "X":
        player_one = "O"
    else:
        player_one = "X"


# checks horizontal
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
    else:
        return False


# check vertical
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
    else:
        return False


# check diagonal
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    else:
        return False


def check_win(board):
    global game_running
    if check_horizontal(board):
        print_board(board)
        print(f"The winner is {winner}!")
        game_running = False

    elif check_vertical(board):
        print_board(board)
        print(f"The winner is {winner}!")
        game_running = False

    elif check_diagonal(board):
        print_board(board)
        print(f"The winner is {winner}!")
        game_running = False


def check_tie(board):
    global game_running
    if "_" not in board:
        print_board(board)
        print("It is a tie!")
        game_running = False
    if "_" == board:
        print("Check board again.")


# switching players
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    if current_player != player_one:
        print("Undefined players: Pick either 'X' or 'O'. ")


def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switch_player()
        if player_one == "X":
            position = random.randint(0, 8)
        else:
            return False


while game_running:
    print_board(board)
    player_input(board)
    check_win(board)
    check_tie(board)
    switch_player()
    computer(board)
    check_win(board)
    check_tie(board)
