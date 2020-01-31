from Board import Board
from Cell import Cell

class Gameplay(object):
    def __init__(self, p1_name, p1_board, p2_name, p2_board, num_rows, num_cols,  **ship_info):
        self.ship_info = ship_info
        self.p1 = p1_name
        self.p2 = p2_name

        self.p1_board = Board(int(num_rows), int(num_cols), p1_board, **ship_info)
        self.p2_board = Board(int(num_rows), int(num_cols), p2_board, **ship_info)
        self.player_turn = True

    def play(self):
        print('Below are player placed boards')
        self.p1_board.format_board(self.p2_board)
        self.p2_board.format_board(self.p2_board)
        while not self.someone_wins():
            if self.player_turn:
                self.p1_board.format_board(self.p2_board)
                self.ask_move()
                self.make_move(self.p1, self.p1_board)
        # Player1 turn if true, player2 turn if
        player_turn = not player_turn

    def ask_move(self):
        coor = input('Where do you want to fire in x, y? ')
        return coor
    def someone_wins(self):
        return False





