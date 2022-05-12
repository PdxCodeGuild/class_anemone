' Lab 13 - Tic Tac Toe '

class Player:
    pass


class Game:

    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __repr__(self):
        board = (f"""
        -------
        |{self.board[0]}|{self.board[1]}|{self.board[2]}|
        -------
        |{self.board[3]}|{self.board[4]}|{self.board[5]}|
        -------
        |{self.board[6]}|{self.board[7]}|{self.board[8]}|
        -------
        """)
        print(board)

tictactoe = Game()
print(tictactoe.__repr__)