from Setup import Setup
from Game import Game
import sys

if __name__ == '__main__':
    ship_info = {}
    file = sys.argv[1]
    with open(file) as config:
        print(sys.argv)
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





