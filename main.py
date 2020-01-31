from Board import Board
from Player import Player

if __name__ == '__main__':
    pass

with open("configs/minor_game.txt") as config:
    size = config.readline()
    row, col = size.split()
    ship_info = {}
    for line in config:
        (key, val) = line.split()
        ship_info[key] = val

print('Board dimension:',row, 'x', col+'\n', ship_info)

# Game setup
b1 = Board(int(row), int(col), **ship_info)
player1 = Player()
player1_name = player1.get_name_1()
b1.initialize_board()
b1.user_place_ship()

b2 = Board(int(row), int(col), **ship_info)
player2 = Player()
player2_name = player1.get_name_2()
b2.initialize_board()
b2.user_place_ship()

# Game begins





