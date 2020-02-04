from Battleship.Setup import Setup
from Battleship.Game import Game
import sys

if __name__ == '__main__':
    config_file = sys.argv[1]
    ship_info = {}
    with open(config_file) as config:
        size = config.readline()
        row, col = size.split()
        for line in config:
            (key, val) = line.split()
            ship_info[key] = val
        s = Setup(row, col, ship_info)

    # Game setup
    rows, cols, ship_info, p1_name, p1_board, p2_name, p2_board = s.setup()

    # Game begins
    battle = Game(p1_name, p1_board, p2_name, p2_board, rows, cols, **ship_info)
    battle.play()





