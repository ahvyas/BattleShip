from Cell import Cell
from typing import List, Any
from typing import Tuple


class Board(object):
    def __init__(self, num_rows: int, num_cols: int, existing_board: List = None, **kwargs: dict) -> None:
        # rows and columns
        self.num_rows = num_rows
        self.num_cols = num_cols
        # initializes the board matrix
        self.b = existing_board
        self.empty = '*'
        self.hit = 'X'
        self.miss = 'O'
        self.ship_info = kwargs
        self.ship_abb = None
        self.cell = Cell(self.num_rows, self.num_cols)

    def initialize_board(self) -> List:
        # creates 2D matrix for our game
        self.b = [[self.cell.first_board_init() for i in range(self.num_cols)] for j in range(self.num_rows)]

        #Initial Board UI
        self.format_board()

        # returns the board for internal manipulation

    def return_board(self) -> List:
        return self.b

    # creates output for and formats the board
    def format_board(self) -> None:
        print(end=' ')
        for hor_num in range(self.num_cols):
            print("", str(hor_num), end= "")
        print('')
        for index, num_row in enumerate(self.b):
            print(index, end=' ')
            print(*num_row, end='\n')

    def gen_valid_or(self, word: str) -> list:
        text = word[0::]
        l = [word[0]]
        for i in range(1, len(word) + 1):
            l.append(text[:i])
        return l

    #validates coordinates given by the user
    def coord_validate(self, board: list, ship_name: str, ship_size: int, row: int, col: int, sp: bool) -> bool:
        s_name = []
        while not sp:
            for i in range(ship_size):
                if board[row][col+i] != self.cell.first_board_init():
                    s_name.append(board[row][col+i])
            if len(s_name):
                s_name.sort()
                print('Cannot place {} horizontally at {}, {} because it would overlap with {}.'
                          .format(ship_name, row, col, *s_name))
                return False
            return True
        while sp:
            for j in range(ship_size):
                if board[row+j][col] != self.cell.first_board_init():
                    s_name.append(board[row+j][col])
                if len(s_name):
                    s_name.sort()
                    print('Cannot place {} vertically at {}, {} because it would overlap with {}.'
                          .format(ship_name, row, col, *s_name))
                    return False

            return True

    #allows user to place ship
    def user_place_ship(self, user_name: str) -> None:
        # Acceptable orientation names
        #valid_orientation_hori = self.gen_valid_or('horizontal')
        #valid_orientation_vert = self.gen_valid_or('vertical')
        valid_orientation_hori = 'horizontal'
        valid_orientation_vert = 'vertical'

        # Turn the ship orientation into a boolean value, makes it easier to code later
        #True = Vertical, False = Horizontal
        def ship_orientation_bool(orientation_lingo: str) -> bool:
            if orientation_lingo in valid_orientation_vert:
                return True
            elif orientation_lingo in valid_orientation_hori:
                return False

        for ship_name, ship_size in self.ship_info.items():
            #Ensures ships aren't placed on another
            ship_size = int(ship_size)
            # user ship input
            while True:
                try:
                    ship_or_input = input('{} enter horizontal or vertical for the orientation of {} which is {} long: '
                                          .format(user_name, ship_name, ship_size))
                    ship_or_input.strip()
                    if ship_or_input.lower() in valid_orientation_hori:
                        ship_or_input = 'horizontal'
                    elif ship_or_input.lower() in valid_orientation_vert:
                        ship_or_input = 'vertical'
                    else:
                        raise ValueError
                except ValueError:
                    print(ship_or_input + ' does not represent an Orientation')
                    continue
                #Asks the user to input coordinates
                ship_coord_input = input('{}, enter the starting position for your {} ship ,which is {} long, '
                                         'in the form row, column'.format(user_name, ship_name, ship_size))
                try:
                    ship_row_input, ship_col_input = ship_coord_input.split(',')
                except ValueError:
                    print(ship_coord_input + ' is not in the form x,y')
                    continue
                try:
                    ship_row_input = int(ship_row_input)
                except ValueError:
                    print('row: {} is not a valid value for row.\nIt should be an integer between 0 '
                          'and {}'.format(ship_row_input, self.num_rows - 1))
                    continue
                try:
                    ship_col_input = int(ship_col_input)
                except ValueError:
                    print('Column: {} is not a valid value for column.\n It should be an integer between 0 '
                          'and {}'.format(ship_col_input, self.num_cols - 1))
                    continue
                try:
                    if ship_col_input not in range(self.num_cols) or ship_row_input not in range(self.num_rows):
                        raise ValueError
                except ValueError:
                    print('Cannot place {} {}ly at {} because it would be out of bounds.'.
                          format(ship_name, ship_or_input, ship_coord_input))
                    continue

                # call the ship_orientation bool object
                sb = ship_orientation_bool(ship_or_input)
                try:
                    valid_placement = self.coord_validate(self.b, ship_name, ship_size, ship_row_input, ship_col_input, sb)
                except IndexError:
                    print('Cannot place {} {}ly at {} because it would end up out of bounds.'
                          .format(ship_name, ship_or_input, ship_coord_input))
                    continue
                if valid_placement:
                    self.b = self.cell.update_cell(self.b, ship_row_input, ship_col_input,
                                                           ship_name, ship_size, sb)

                elif not valid_placement:
                    continue

                break

            self.format_board()
        return self.b

    def get_result(self, x: int, y: int) -> Tuple[str, Any]:
        self.ship_abb = self.b[x][y]
        if self.b[x][y] == self.empty:  # Case for miss
            print('Miss')
            return self.miss, self.ship_abb
        else:  # Case for hit
            return self.hit, self.ship_abb

    def update_board(self, x: int, y: int, hit_or_miss: str) -> None:
        self.b[x][y] = hit_or_miss
