from Board import Board
from Mask import Mask
from Cell import Cell

from typing import List

class Game(object):
    def __init__(self, p1_name, p1_board, p2_name, p2_board, num_rows, num_cols,  **ship_info) -> None:
        self.ship_info = ship_info
        self.p1 = p1_name
        self.p2 = p2_name

        self.p1_board = Board(int(num_rows), int(num_cols), p1_board, **ship_info)
        self.p2_board = Board(int(num_rows), int(num_cols), p2_board, **ship_info)
        self.mask1 = Mask(int(num_rows), int(num_cols), **ship_info) # mask 1 is for player 2 to look at
        self.mask2 = Mask(int(num_rows), int(num_cols), **ship_info) # mask 2 is for player 1 to look at
        self.mask1.initialize_mask()
        self.mask2.initialize_mask()
        self.cell = Cell(int(num_rows), int(num_cols))
        self.player_turn = True


    def play(self) -> None:
        print('Battle begins\n')
        while not self.someone_wins():
            # True - player 1's turn
            if self.player_turn:
                self.mask2.format_mask()
                x, y = self.ask_move(self.p1)

                if not self.check_move(x, y, self.p2_board.return_board()):
                    continue

                hit_or_miss = self.p2_board.get_result(x,y)
                self.mask2.update_mask(x, y, hit_or_miss)
                self.p2_board.update_board(x, y, hit_or_miss)
                self.mask2.format_mask()

            # False - player 2's turn
            if not self.player_turn:
                self.mask1.format_mask()
                x, y = self.ask_move(self.p2)

                if not self.check_move(x, y, self.p1_board.return_board()):
                    continue

                hit_or_miss = self.p1_board.get_result(x, y)
                self.mask1.update_mask(x, y, hit_or_miss)
                self.p1_board.update_board(x, y, hit_or_miss)
                self.mask1.format_mask()

            # Switch player
            self.player_turn = not self.player_turn
            print('\n\n')


    def ask_move(self,name: str):
        print('General', name.upper())
        coor = input('Where do you want to fire in x, y? ')
        coor = coor.strip()
        x, y = coor.split(',')
        x = int(x.rstrip())
        y = int(y.lstrip())
        return x, y

    def check_move(self,x: int, y: int, board: List):
        try:
            if board[x][y] == 'X':
                print('Fired and missed, ')
                return False
            elif board[x][y] == 'O':
                print('Fired and hit')
                return False
            else:
                return True
        except:
            print('Enter a valid coordinate!')
            return False



    def someone_wins(self):

        return False





