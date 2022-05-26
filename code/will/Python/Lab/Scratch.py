        
        #for i in range(3):
        #    row = self.board[i]
        #    if all(item == row[0] and item != " " for item in row):
        #        return 
        if self.board[0][0] == self.board[1][0] == self.board[2][0]== player.token:
            return player.token
        elif self.board[0][0] == self.board[0][1] == self.board[0][2]== player.token:
            return player.token
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]== player.token:
            return player.token
        elif self.board[1][0] == self.board[1][1] == self.board[1][2]== player.token:
            return player.token
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]== player.token:
            return player.token
        elif self.board[2][0] == self.board[1][1] == self.board[0][2]== player.token:
            return player.token
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]== player.token:
            return player.token
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]== player.token:
            return player.token

       
    def move(self, x, y, token):
    #    possible_moves = {1:(0,0), 2:(1,0),3:(2,0),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
        if self.board[y][x] != " ":
            return "This space is already taken"
        else:
            self.board[y][x] = token 