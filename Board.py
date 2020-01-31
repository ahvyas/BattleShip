from UpdateBoard import UpdateBoard
from Cell import Cell
from Ship import Ship


class Board(object):
    def __init__(self, num_rows: int, num_cols: int, **kwargs: dict) -> None:
        # rows and columns
        self.num_rows = num_rows
        self.num_cols = num_cols
        # initializes the board matrix
        self.b = []
        self.empty = '*'
        # self.hit = 'X'
        # self.miss = 'O'
        self.ship_info = kwargs
        self.cell = Cell(self.num_rows, self.num_cols)
        self.ship = None


    def initialize_board(self):
        # creates 2D matrix for our game
        self.b = [[self.cell.first_board_init() for i in range(self.num_rows)] for j in range(self.num_cols)]

        #Initial Board UI
        self.format_board(self.b)

        # returns the board for internal manipulation
        return self.b

    # creates output for and formats the board
    def format_board(self, board):
        print(end='  ')
        for hor_num in range(self.num_rows):
            print(str(hor_num), end=" ")
        print('')
        for index, num_row in enumerate(self.b):
            print(index, end=' ')
            print(*num_row, end='\n')

    def user_place_ship(self, ship_cols=None) -> None:
        # Acceptable orientation names
        valid_orientation_hori = ['h', 'hori', 'horiz', 'horizontal']
        valid_orientation_vert = ['v', 'vert', 'verti', 'vertical']

        # Turn the ship orientation into a boolean value, makes it easier to code later
        #True = Horizontal, False = Vertical
        def ship_orientation_bool(orientation_lingo: str) -> bool:
            if orientation_lingo in valid_orientation_vert:
                return True
            elif orientation_lingo in valid_orientation_hori:
                return False

        for ship_name, ship_size in self.ship_info.items():
            # calls the ship class
            # ship inputs
            while True:
                try:
                    ship_or_input = input('Please enter orientation for ship {}, size {}: '
                                          .format(ship_name, ship_size))
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
                ship_coord_input = input('Please enter the row, column for shipship {}, size {}: '
                                         .format(ship_name, ship_size))
                try:
                    ship_row_input, ship_col_input = ship_coord_input.split(',')
                except ValueError:
                    print(ship_coord_input + ' is not in the form x,y')
                    continue
                try:
                    ship_row_input = int(ship_row_input)
                except ValueError:
                    print('row: {} is not a valid value for row.\n It should be an integer between 0 '
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
                # Create the ship object
                self.ship = Ship(ship_name, ship_size, sb)

                if sb:
                    try:
                        if (ship_row_input + int(ship_size) - 1) not in range(self.num_rows):
                            raise ValueError
                    except ValueError:
                        print('Cannot place {} {}ly at {} because it would be out of bounds.'.
                              format(ship_name, ship_or_input, ship_coord_input))
                        continue

                    try:
                        Board = self.cell.update_cell(self.b, ship_row_input, ship_col_input,
                                                               ship_name, ship_size, sb)
                    except ValueError:
                        print('Cannot place {} {}ly at {} because it would overlap with {}'
                                  .format(ship_name, ship_or_input, ship_coord_input, Board))
                        continue

                if not sb:
                    try:
                        if (ship_col_input + int(ship_size) - 1) not in range(self.num_cols):
                            raise ValueError
                    except ValueError:
                        print('Cannot place {} {}ly at {} because it would be out of bounds.'.
                              format(ship_name, ship_or_input, ship_coord_input))
                        continue
                    try:
                        Board = self.cell.update_cell(self.b, ship_row_input, ship_col_input,
                                                               ship_name, ship_size, sb)
                    except ValueError:
                        print('Cannot place {} {}ly at {} because it would overlap with {}'
                                  .format(ship_name, ship_or_input, ship_coord_input, Board))
                        continue
                self.b = Board
                break
                # CellChange = Cell(self.num_rows, self.num_cols)
                # CellChange = CellChange.cell_update_move('hit')
                # return print(CellChange)
            self.format_board(self.b)
        return self.format_board(self.b)

    def update_board(self, user_move):
        ub = UpdateBoard()
        ub.update(user_move, self.b)


with open("configs/minor_game.txt") as config:
    size = config.readline()
    row, col = size.split()
    ship_info = {}
    for line in config:
        (key, val) = line.split()
        ship_info[key] = val

print(row, col, ship_info)

b = Board(int(row), int(col), **ship_info)
b.initialize_board()
b.user_place_ship()
