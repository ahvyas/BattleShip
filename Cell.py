class Cell(object):
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        # Types of states of board
        self.empty = '*'
        self.hit = 'X'
        self.miss = 'O'

    def firstboard_init(self):
        return self.empty

    def cell_update_move(self, x='*'):
        if x == 'hit':
            return self.hit
        if x == 'miss':
            return self.miss
        return self.empty
