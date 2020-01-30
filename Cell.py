class Cell(object):
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        # Types of states of board
        self.empty = '*'
        self.hit = 'X'
        self.miss = 'O'

    def firstboard_init(self, b: list) -> list:
        b = [[self.empty for i in range(self.num_rows)] for j in range(self.num_cols)]
        return b
