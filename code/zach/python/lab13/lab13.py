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

    # creates list of indices that needed for a win condition rows, cols, and diags
    def win_indices(self):
        # winning rows
        for row in range(self.size):
            yield [(row, col) for col in range(self.size)]
        # winning columns
        for col in range(self.size):
            yield [(row, col) for row in range(self.size)]
        # winning diagonals
        # * Top Left to Bottom Right
        yield[[i, i] for i in range(self.size)]
        # * Top Right to Bottom Left
        yield [(i, self.size-1-i) for i in range(self.size)]

    def calc_winner(self, player):
        n = len(self.data)
        for indices in self.win_indices():
            # if all winning indices are same player token return true
            if all(self.data[row][col] == player.token for row, col in indices):
                return True, print('we have a winner')
        return False
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
        self.board.calc_winner(player)
        return self.move_count > 0

    def __repr__(self):
        return str(self.view)


players = [Player(name='Piccard', token='X'), Player(name='Q', token='O')]
game = GameControl(players=players)

while game.make_move():
    print(game)
