' Lab 13 - Tic Tac Toe '

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:

    def __init__(self):                                                     # create empty board spaces
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
            ]

    def __repr__(self):                                                     # print the board
        board = print(f"""
          0 1 2 
         -------
        0|{self.board[0][0]}|{self.board[1][0]}|{self.board[2][0]}|
         -------
        1|{self.board[0][1]}|{self.board[1][1]}|{self.board[2][1]}|
         -------
        2|{self.board[0][2]}|{self.board[1][2]}|{self.board[2][2]}|
         -------
        """)
        return board
    
    def move(self, x, y, player):                                           # place piece on board given coords
        self.board[x][y] = player.token

    def calc_winner(self):                                                                             # calculate...
        if self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != ' ':       # horizontal wins...
            return True
        if self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != ' ':
            return True
        if self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != ' ':
            return True
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ':       # vertical wins...
            return True
        if self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != ' ':
            return True
        if self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != ' ':
            return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':       # and diagonal wins
            return True
        if self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[2][0] != ' ':
            return True
        else:
            return False
        
    def is_full(self):                                                      # figure out wether the board is full or not regardless of if there is a winner
        for i in self.board:
            for j in i:
                if j == ' ':
                    return False
        return True

    def is_game_over(self):                                                 # figure out if someone has won yet or the board is full
        if self.calc_winner():
            return True
        elif self.is_full():
            return True
        else:
            return False

def main():
    print("\n~*~ Tic Tac Toe ~*~\n")

    p1_name = input("Player 1 name: ").title()                              # set variables for names and tokens for both players
    p1_token = 'X'
    p1 = Player(p1_name, p1_token)

    p2_name = input("Player 2 name: ").title()
    p2_token = 'O'
    p2 = Player(p2_name, p2_token)

    tictactoe = Game()
    tictactoe.__repr__()

    while tictactoe.is_game_over() is False:                                # run this program until the game is over. For both players...
        p1_x = input(f"{p1.name}'s turn.\n\nPick a column (0-2): ")         # get their column...
        p1_y = input("And a row (0-2): ")                                   # and their row.
        tictactoe.move(int(p1_x), int(p1_y), p1)
        tictactoe.__repr__()                                                # print board with new piece
        if tictactoe.calc_winner():                                         # decide a winner or continue
            print(f"{p1.name} is the winner!")
            break
        if tictactoe.is_full():
            print("It's a draw.")
            break

        p2_x = input(f"{p2.name}'s turn.\n\nPick a column (0-2): ")
        p2_y = input("And a row (0-2): ")
        tictactoe.move(int(p2_x), int(p2_y), p2)
        tictactoe.__repr__()
        if tictactoe.calc_winner():
            print(f"{p2.name} is the winner!")
            break
        if tictactoe.is_full():
            print("It's a draw.")
            break

main()                                                                      # GAME ON! 