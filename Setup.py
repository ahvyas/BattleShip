from Board import Board
from Player import Player

def setup():
    with open("configs/minor_game.txt") as config:
        size = config.readline()
        row, col = size.split()
        ship_info = {}
        for line in config:
            (key, val) = line.split()
            ship_info[key] = val

    print('Board dimension:',row, 'x', col+'\n', ship_info)

    b1 = Board(int(row), int(col), **ship_info)
    player1 = Player()
    p1_name = player1.get_name_1()
    b1.initialize_board()
    p1_board = b1.user_place_ship()

    b2 = Board(int(row), int(col), **ship_info)
    player2 = Player()
    p2_name = player1.get_name_2()
    b2.initialize_board()
    p2_board = b2.user_place_ship()

    return row, col, ship_info, p1_name, p1_board, p2_name, p2_board
