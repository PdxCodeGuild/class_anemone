#Lab13: Tic Tac Toe

from multiprocessing.dummy import current_process


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __empty_board_function(self):
        board = []
        for x in range(3):
            board.append([])
            for y in range(3):
                board[x].append(' ')
        return board
    
    def __init__(self):
        self.board = self.__empty_board_function()

    def __repr__(self):
        for x in self.board:
            looks_good = "|".join(x)
            print (looks_good)

    def move(self, row, column, player):
        
        token_spaces = {

            "top" : 0,
            "middle" : 1,
            "bottom" : 2,

            "left" : 0,
            "center" : 1,
            "right" : 2,
        }

        x = token_spaces[row]
        y = token_spaces[column]

        self.board[x][y] = player.token

    def calc_winner(self, player):
        if self.board[0][0] and self.board[0][1] and self.board[0][2] == player.token:
            print(f"{player.name} wins!")
        elif self.board[1][0] and self.board[1][1] and self.board[1][2] == player.token:
            print(f"{player.name} wins!")
        elif self.board[2][0] and self.board[2][1] and self.board[2][2] == player.token:
            print(f"{player.name} wins!")
        elif self.board[0][0] and self.board[1][0] and self.board[2][0] == player.token:
            print(f"{player.name} wins!")
        elif self.board [0][1] and self.board[1][1] and self.board[2][1] == player.token:
            print(f"{player.name} wins!")
        elif self.board[0][2] and self.board[1][2] and self.board[2][2] == player.token:
            print(f"{player.name} wins!")
        elif self.board[0][0] and self.board[1][1] and self.board[2][2] == player.token:
            print(f"{player.name} wins!")
        elif self.board[2][0] and self.board[1][1] and self.board[0][2] == player.token:
            print(f"{player.name} wins!")

    def is_full(self):
        #NOT WORKING ):
        for x in self.board:
            if x == '':
                return True
            else:
                return False

    def is_game_over(self):
    
        print ("GAME OVER.")





tictactoe = Game()
tictactoe.__repr__()
print ('Welcome to Tic Tac Toe!')
while True:
    player1_name = input("Enter player 1 name: ")
    player1_token = input('Pick "x" or "o": ').lower()

    player2_name = input("Enter player 2 name: ")
    player2_token = "o" if player1_token == "x" else "x"

    player1 = Player(player1_name, player1_token)
    player2 = Player(player2_name, player2_token)
    
    move_counter = 0
    while True:
        current_player = player1 if move_counter % 2 == 0 else player2
        move_counter += 1
        print(f"It's {current_player.name}'s turn!\n")

        row = input("Which row (top/middle/bottom) do you want your mark in? ")
        column = input("Which column (left/center/right) do you want your mark in? ")
        tictactoe.move(row, column, current_player)
        tictactoe.__repr__()

        tictactoe.is_full()
    