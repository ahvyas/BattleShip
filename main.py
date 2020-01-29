from Board import Board
if __name__ == '__main__':
    pass

with open("configs/minor_game.txt") as config:
    size = config.readline()
    row, col = size.split()
    ship_info={}
    for line in config:
        (key, val) = line.split()
        ship_info[key] = val

print(row, col, ship_info)
b = Board(int(row), int(col), **ship_info)
b.initialize_board()
