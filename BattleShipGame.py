from Board import Board
from Cell import Cell
from Player import Player


class GamePlayLoop(object):
    def __init__(self, num_rows: int, num_cols: int, *kwargs):
        self.b = Board(num_rows, num_cols, *kwargs)
        self.Players = [Player() for _ in range(2)]

    def player_turn(self):
        while True:
            try:
                usr_input = input('Enter location you want to fire in the form row, column: ')
                usr_row, usr_col = int(usr_input.split(','))
            except ValueError:
                pass
