from Board import Board
from Mask import Mask
from Cell import Cell
from Ship import Ship
from typing import Tuple, List
import time


class Game(object):
    def __init__(self, p1_name, p1_board, p2_name, p2_board, num_rows, num_cols,  **ship_info) -> None:
        self.p1 = p1_name.upper()
        self.p2 = p2_name.upper()
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.p1_board = Board(int(num_rows), int(num_cols), p1_board, **ship_info)
        self.p2_board = Board(int(num_rows), int(num_cols), p2_board, **ship_info)
        self.mask1 = Mask(int(num_rows), int(num_cols), self.p1_board) # mask 1 is for player 2 to look at
        self.mask2 = Mask(int(num_rows), int(num_cols), self.p2_board) # mask 2 is for player 1 to look at
        self.mask1.initialize_mask()
        self.mask2.initialize_mask()
        self.cell = Cell(int(num_rows), int(num_cols))
        self.player_turn = True
        self.s = Ship(ship_info)
        self.ships = ship_info

    def play(self) -> None:
        print('Battle begins\n')
        p1_ship = self.s.new_dict()
        p2_ship = self.s.new_dict()
        while not self.someone_wins():

            # True - player 1's turn
            if self.player_turn:
                print('Attack Board')
                self.mask2.format_mask()
                print('Your Board')
                self.p1_board.format_board()
                x, y = self.ask_move(self.p1)

                if not self.check_move(x, y, self.p2_board.return_board()):
                    continue

                hit_or_miss, ship_abb = self.p2_board.get_result(x, y)
                if hit_or_miss == 'X':
                    ship_name = [name for name, size in p1_ship.items() if name.startswith(ship_abb)]
                    print("You hit {}'s {}".format(self.p2, *ship_name))
                    time.sleep(2)
                    p2_ship = self.s.update_ship(self.p2, p2_ship, ship_abb)
                    time.sleep(2)

                    if not p2_ship:
                        self.someone_wins(self.p1)
                        break
                self.mask2.update_mask(x, y, hit_or_miss)
                self.p2_board.update_board(x, y, hit_or_miss)
                self.mask2.format_mask()

            # False - player 2's turn
            if not self.player_turn:
                print('Attack Board')
                self.mask1.format_mask()
                print('Your Board')
                self.p2_board.format_board()
                x, y = self.ask_move(self.p2)

                if not self.check_move(x, y, self.p1_board.return_board()):
                    continue

                hit_or_miss, ship_abb = self.p1_board.get_result(x, y)
                if hit_or_miss == 'X':
                    ship_name = [name for name, size in p1_ship.items() if name.startswith(ship_abb)]
                    print("You hit {}'s {}".format(self.p1, *ship_name))
                    time.sleep(1)
                    p1_ship = self.s.update_ship(self.p1, p1_ship, ship_abb)

                    if not p1_ship:
                        self.someone_wins(self.p2)
                        break
                self.mask1.update_mask(x, y, hit_or_miss)
                self.p1_board.update_board(x, y, hit_or_miss)
                self.mask1.format_mask()

            # Switch player
            self.player_turn = not self.player_turn
            print('\n\n')

    def ask_move(self, name: str) -> Tuple[int, int]:
        while True:
            coor = input('General {}, where do you want to fire in x, y?'.format(name))
            coor = coor.strip()
            try:
                x, y = coor.split(',')
            except ValueError:
                print('{} is not a valid location.\n Enter the firing location in the form row, column'.format(coor))
                continue
            try:
                x = int(x.rstrip())
            except ValueError:
                print('Row should be an integer. {} is NOT an integer.'.format(x))
                continue
            try:
                y = int(y.lstrip())
            except ValueError:
                print('Column should be an integer. {} is NOT an integer.'.format(y))
                continue

            return x, y

    def check_move(self,x: int, y: int, board: List):
        try:
            if board[x][y] == 'X' or board[x][y] == 'O':
                print('You have already fired at {}, {}.'.format(x, y))
                return False
            else:
                return True
        except IndexError:
            print('{}, {} is not in bounds of our {} X {} board.'.format(x, y, self.num_rows, self.num_cols))
            return False

    def someone_wins(self, *winner_name: str) -> bool:
        if winner_name:
            print('Congratulations, General {} has won the game!'.format(*winner_name))
            return True

        return False
