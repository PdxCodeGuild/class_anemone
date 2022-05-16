class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.prompt = f'Player - { name } enter row and column [r,c]: '

    def get_move(self):
        message = input(self.prompt)
        row, col = [int(x) for x in message.split(',')]
        return row, col

    def __repr__(self):
        return self.name, self.token


class GameBoard:
    def __init__(self, size=3, blank_space='-'):
        self.size = size
        self.data = [[blank_space for _ in range(size)] for _ in range(size)]
        self.blank = blank_space
        self.move_count = 0

    def get_row(self, row):
        return self.data[row]

    def move(self, row, col, player):
        if self.data[row][col] == self.blank:
            self.data[row][col] = player.token
            self.move_count += 1
        else:
            print('\t\tspace has already been filled!!!')
    

#     def calc_winner(self):
#         return

#     def is_full(self):
#         return

#     def is_game_over(self):
#         return

class GameView:
    def __init__(self, board: GameBoard):
        self.board = board

    def __repr__(self):  # prints our pretty board output for user
        row_list = []
        for i in range(self.board.size):
            row = self.board.get_row(i)
            pretty_text = '|'.join(str(space) for space in row)
            row_list.append(pretty_text)
        return '\n'.join(row_list)


class GameControl:
    def __init__(self, players):
        self.players = players
        self.board = GameBoard()
        self.view = GameView(self.board)
        # TODO: Ends games when out of turns need win conditions
        self.move_count = 9
        self.index = 0

    def make_move(self):
        player = self.players[self.index]
        # alternates turns without using reverse allowing for n number of players (index + 1) % len(n_players)
        self.index = (self.index + 1) % 2
        row, col = player.get_move()
        self.board.move(row, col, player)
        self.move_count -= 1
        return self.move_count > 0

    def __repr__(self):
        return str(self.view)


players = [Player(name='Piccard', token='X'), Player(name='Q', token='O')]
game = GameControl(players=players)

while game.make_move():
    print(game)


