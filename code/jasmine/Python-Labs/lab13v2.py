
## Tic Tac Toe Game Lab 13


from audioop import getsample


class Player:
    def _init_(self,name,token):
        self.name = name
        self.token = token

# game class
class Game:
    def _init_(self):
        # each position on board empty. 9 slots
        self.board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"],
            ]
    def _repr_(self):
        print(self.board[0]+ "|" + self.board[1]+ "|" + self.board[2])
        print(self.board[3]+ "|" + self.board[4]+ "|"+ self.board[5])
        print(self.board[6]+ "|" + self.board[7]+ "|"+ self.board[8])

board = Game()