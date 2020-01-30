from Board import Board
from Cell import Cell

class GamePlayLoop(object):
    def __init__(self, num_rows: int, num_cols: int, *kwargs):
        self.b = Board(num_rows, num_cols, *kwargs)