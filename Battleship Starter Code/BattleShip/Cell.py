class Cell(object):
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.empty = '*'
        #check if it's been fired upon
        self.check_occ = False
        self.ship_name = []

    def first_board_init(self) -> str:
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
