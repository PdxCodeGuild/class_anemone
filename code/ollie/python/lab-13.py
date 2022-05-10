' Lab 13 - Tic Tac Toe '

#class Game:

def __repr__(board):

    print('-------')
    print('|' + board[1] + '|' + board[2] +'|' + board[3] + '|')
    print('-------')
    print('|' + board[4] + '|' + board[5] +'|' + board[6] + '|')
    print('-------')
    print('|' + board[7] + '|' + board[8] +'|' + board[9] + '|')
    print('-------')

test = ['', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
__repr__(test)