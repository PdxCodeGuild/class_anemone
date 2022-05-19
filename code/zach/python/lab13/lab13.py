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
                return True, print(f'\n\t\twe have a winner\n\t\tCongrats { player.name }')
        return False

    def is_full(self):
        for row in self.data:
            for space in row:
                if space == '-':
                    return False
        print('\n\t\tBoard is Full.')
        return True

    def is_game_over(self, player):
        if self.is_full() or self.calc_winner(player):
            print('\n\t\tGame Over!!!')
            return True
        return False


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
        self.move_count = 10
        self.index = 0

    def make_move(self):
        player = self.players[self.index]
        # alternates turns without using reverse allowing for n number of players (index + 1) % len(n_players)
        self.index = (self.index + 1) % 2
        row, col = player.get_move()
        self.board.move(row, col, player)
        self.move_count -= 1
        if self.board.is_game_over(player):
            return False
        return True

    def __repr__(self):
        return str(self.view)


def main():
    rematch = 'r'
    t1 = 'X'
    t2 = 'O'
    p1 = input(f'Player { t1 } enter name: ')
    p2 = input(f'Player { t2 } enter name: ')

    while rematch == 'r':
        players = [Player(name=p1, token=t1), Player(name=p2, token=t2)]
        game = GameControl(players=players)

        while game.make_move():
            print(game)
        print(game)
        rematch = input('[r]ematch? ')


if __name__ == '__main__':
    main()
