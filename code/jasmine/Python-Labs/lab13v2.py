
## Tic Tac Toe Game Lab 13


from audioop import getsample


class Player:
<<<<<<< HEAD
    def _init_(self,name,token):
        self.name = name
=======
    def _init_(self,player_name,token):
        self.player_name = player_name
>>>>>>> 0dcac4f9f250e1793785b869e1907f960be613e2
        self.token = token

# game class
class Game:
<<<<<<< HEAD
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
=======
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

>>>>>>> 0dcac4f9f250e1793785b869e1907f960be613e2
