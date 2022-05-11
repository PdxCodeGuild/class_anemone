# ....Lab 13 ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

# player_one = Player('Merry', 'X')
# player_two = Player('Pippin', 'O')

# print(player_one.token)
# print(player_two.name)

class Game(Player):
    def __init__(self):
        self.board = [
            ['-', '-', '-'], # 0,0 0,1 0,2
            ['-', '-', '-'], # 1,0 1,1 1,2
            ['-', '-', '-']  # 2,0 2,1 2,2
        ]
        
        # print(self.board[1][2])

    def __repr__(self):
        row1 = '|'.join(self.board[0])
        row2 = '|'.join(self.board[1])
        row3 = '|'.join(self.board[2])
        board = row1 + '\n' + row2 + '\n' + row3
        return board
        # -|-|-
        # -|-|-
        # -|-|-

    def move(self, x, y, player):
        # x = int(input('Which row: '))
        # y = int(input('Which column: '))
        if self.board[x][y] != '-':
            print('Space already claimed...')
        else: self.board[x][y] = player.token

    def calc_winner(self, player):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == player.token:
            return player.token
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == player.token:
            return player.token
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == player.token:
            return player.token
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == player.token:
            return player.token
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == player.token:
            return player.token
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == player.token:
            return player.token
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == player.token:
            return player.token
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == player.token:
            return player.token
        else:
            return None

    def is_full(self):
        pass

    def is_game_over(self, player):
        return self.calc_winner(player) or self.is_full()

# ....TIC TAC TOE ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

while True:
    game = Game()
    print('Welcome to Tic Tac Toe')
    player_one = Player(input('Player One Name: '), input('Player One Token: '))
    player_two = Player(input('Player Two Name: '), input('Player Two Token: '))
    print(f'{player_one.name} is {player_one.token}')
    print(f'{player_two.name} is {player_two.token}')
    turn = 0
    while True:
        player = player_one if turn % 2 == 0 else player_two
        print(game.__repr__())
        x = int(input(f'{player.name}, which row: '))
        y = int(input(f'{player.name}, which column: '))
        game.move(x, y, player)
        if game.calc_winner(player) == player.token:
            print(game.__repr__())
            print(f'{player.name} has won the game!')
            break
        elif game.is_full() == True:
            print(game.__repr__())
            print('The game was a draw!')
            break
        turn += 1
    if game.is_game_over(player) == True:
        another_game = input('Would you like to play again? y/n ')
        if another_game == 'y':
            break
        elif another_game == 'n':
            False