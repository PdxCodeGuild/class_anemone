' Lab 13 - Tic Tac Toe '

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:

    def __init__(self):
        self.board = {0: ' ', 1: ' ',2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' '}

    def __repr__(self):
        board = (f"""
          1 2 3 
         -------
        1|{self.board[0]}|{self.board[1]}|{self.board[2]}|
         -------
        2|{self.board[3]}|{self.board[4]}|{self.board[5]}|
         -------
        3|{self.board[6]}|{self.board[7]}|{self.board[8]}|
         -------
        """)
        return board
    
    def move(self, x, y, player):
        x = input(f"""
        Where would you like to go?
        {print(Game.__repr__)}
        Choose a column (1-3, left-->right): """)
        y = input("And a row (1-3, top-->bottom): ")
        player = tuple(zip(x, y))
        return player

    def calc_winner(self):
        
        pass

    def is_full(self):
        for spaces in self.board:
            if any(space == ' ' for space in spaces):
                return False
            else:
                return True

tictactoe = print(Game())
tictactoe

