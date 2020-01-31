from Board import Board
from player import Player
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

b1 = Board(int(row), int(col), **ship_info)
b2 = Board(int(row), int(col), **ship_info)
player1 = Player()

b1.initialize_board()
b1.user_place_ship()

