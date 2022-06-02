
## Tic Tac Toe Game Lab 13


from audioop import getsample


class Player:
    def _init_(self,player_name,token):
        self.player_name = player_name
        self.token = token

# game class
class Game:
    def _init_(self,board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"],
            ]):
        # each position on board empty. 9 slots
        self.board = board
    
    def _repr_(self):
        # print(self.board[0][0]+ "|" + self.board[0][1]+ "|" + self.board[0][2])
        # print(self.board[1][0]+ "|" + self.board[4]+ "|"+ self.board[5])
        # print(self.board[6]+ "|" + self.board[7]+ "|"+ self.board[8])
        for row in self.board:
            for slot in row:
                print(slot)
        return self.board
# board = Game()
# board._repr_()

