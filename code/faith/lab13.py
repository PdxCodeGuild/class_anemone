class Player:
    def __init__(self, player, token):  
        self.token = token
        self.player = player

class Game:
    def __init__(self):  
        self.board = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',                                         
                      '7': ' ', '8': ' ', '9': ' '}
    
    def __repr__(self): 
        tac_board = f"{self.board['7']}|{self.board['8']}|{self.board['9']}\n{self.board['4']}|{self.board['5']}|{self.board['6']}\n{self.board['1']}|{self.board['2']}|{self.board['3']}"
        return tac_board
    
    def move(self, key, player): 
        self.board[key] = player.token
    
    def calc_winner(self, player):  
        if self.board['7'] == self.board['8'] == self.board['9'] == player.token:
            return player.token
        elif self.board['4'] == self.board['5'] == self.board['6'] == player.token:
            return player.token 
        elif self.board['1'] == self.board['2'] == self.board['3'] == player.token:
            return player.token 
        elif self.board['7'] == self.board['5'] == self.board['3'] == player.token:
            return player.token
        elif self.board['1'] == self.board['5'] == self.board['9'] == player.token:
            return player.token
        elif self.board['7'] == self.board['4'] == self.board['1'] == player.token:
            return player.token
        elif self.board['8'] == self.board['5'] == self.board['2'] == player.token:
            return player.token 
        elif self.board['9'] == self.board['6'] == self.board['3'] == player.token:
            return player.token 
        else:
            return None

    def is_full(self):  
        for key in self.board:
            if self.board[key] == ' ':
                return False
        return True

    def game_over(self, player):  
        if self.calc_winner(player):
            return True
        elif self.is_full():
            return True
        else:
            return False


def main():  
    print("Welcome to tic-tac-toe")

    
    player_one_token = "X"
    player_two_token = "O"


    player_one = input("Player 1 enter your name: ")
    player_two = input("Player 2 enter your name: ")
   

    player_1 = Player(player_one,player_one_token)
    player_2 = Player(player_two,player_two_token)
        
   
    complete_game = Game()
    complete_game.__repr__()

    while True:

       
        move_one = input(f"{player_1.player} enter your move: ")
        complete_game.move(move_one, player_1)
        print(complete_game.__repr__())

        if complete_game.game_over(player_1) == True:
            if complete_game.is_full() == True:
                print("Tie Game")
            elif complete_game.calc_winner(player_1):
                print(f"{player_1.player} wins!")
            break


        move_two = input(f"{player_2.player} enter your move: ")
        complete_game.move(move_two, player_2)
        print(complete_game.__repr__())

        if complete_game.game_over(player_2) == True:
            if complete_game.is_full() == True:
                print("Tie Game")
            elif complete_game.calc_winner(player_2):
                print(f"{player_2.player} wins!")
            break

main()