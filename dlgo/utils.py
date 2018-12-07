from . import gotypes

import string

COLS = string.ascii_uppercase[:-6]
STONE_TO_CHAR = {
        None: '.',
        gotypes.Player.black: 'x',
        gotypes.Player.white: 'o'}


def print_move(player, move):
    if move.is_pass:
        move_str = 'passes'
    elif move.is_resign:
        move_str = 'resigns'
    else:
        move_str = '%s%d' % (COLS[move.point.col -1], move.point.row)
    print(f'{player} {move_str}')

def print_board(board):
    for row in range(board.num_rows, 0, -1):
        line = []
        for col in range(1,board.num_col +1):
            stone = board.get(gotypes.Point(row=row,col=col))
            line.append(STONE_TO_CHAR[stone])
        print('{row} {''.join(line)}')
    print('   {COLS[:board.num_cols]}')













