from Board import Board
from Player import Player


class Setup(object):
    def __init__(self):
        self.row = None
        self.col = None
        self.ship_info = {}
        self.p1_name = None
        self.p1_board = None
        self.p2_name = None
        self.p2_board = None

    def setup(self):
        with open("configs/minor_game.txt") as config:
            size = config.readline()
            self.row, self.col = size.split()
            for line in config:
                (key, val) = line.split()
                self.ship_info[key] = val

        print('Board dimension:', self.row, 'x', self.col+'\n', self.ship_info)

        b1 = Board(int(self.row), int(self.col), **self.ship_info)
        player1 = Player()
        p1_name = player1.get_name_1()
        b1.initialize_board()
        p1_board = b1.user_place_ship()

        b2 = Board(int(self.row), int(self.col), **self.ship_info)
        player2 = Player()
        p2_name = player2.get_name_2(p1_name)
        b2.initialize_board()
        p2_board = b2.user_place_ship()

        print('Warship deployment completed.\n\n')
        return self.row, self.col, self.ship_info, p1_name, p1_board, p2_name, p2_board
