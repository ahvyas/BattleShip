from typing import Union

class Cell(object):
    def __init__(self, num_rows: int, num_cols: int) -> Union[str, int]:
        self.num_rows = num_rows
        self.num_cols = num_cols
        # Types of states of board
        self.empty = '*'
        self.hit = 'X'
        self.miss = 'O'
        #check if it's been fired upon
        self.check_occ = False
        self.ship_name = []

    def first_board_init(self):
        return self.empty

    def update_cell(self, board, row, column, ship_name, ship_size, orientation):
        # if orientation is vertical
        if orientation:
            for i in range(int(ship_size)):
                self.check_occ = True
                board[row+i][column] = ship_name[0]
            self.ship_name.append(ship_name)
        if not orientation:
            for j in range(int(ship_size)):
                self.check_occ = True
                board[row][column + j] = ship_name[0]
            self.ship_name.append(ship_name)
        return board

    def cell_update_move(self, x='*'):
        self.check_occ = True
        if x == 'hit':
            return self.hit, self.flag
        if x == 'miss':
            return self.miss, self.flag
