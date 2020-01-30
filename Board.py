from UpdateBoard import UpdateBoard
from Cell import Cell


class Board(object):
    def __init__(self, num_rows: int, num_cols: int, **kwargs: dict) -> None:
        # rows and columns
        self.num_rows = num_rows
        self.num_cols = num_cols
        # initializes the board matrix
        self.b = []
        #self.empty = '*'
        #self.hit = 'X'
        #self.miss = 'O'
        self.ship_info = kwargs

    def initialize_board(self):
        # creates 2D matrix for our game
        init_cell = Cell(self.num_rows, self.num_cols)
        self.b = [[init_cell.firstboard_init() for i in range(self.num_rows)] for j in range(self.num_cols)]

        # creates output for and formats the board
        print(end='  ')
        for hor_num in range(self.num_rows):
            print(str(hor_num), end=" ")
        print('')
        for index, num_row in enumerate(self.b):
            print(index, end=' ')
            print(*num_row, end='\n')

        # returns the board for internal manipulation
        return self.b

    def user_place_ship(self, ship_cols=None) -> None:
        #Acceptable orientation names
        valid_orientation_hori = ['h', 'hori', 'horiz', 'horizontal']
        valid_orientation_vert = ['v', 'vert', 'verti', 'vertical']

        for ship, ship_size in self.ship_info.items():
            #ship inputs
            """while True:
                try:
                    ship_or_input = str(input('Please enter orientation for ship ' + ship + ': '))
                    if ship_or_input.lower() not in valid_orientation_hori and ship_or_input.lower() \
                                                                        not in valid_orientation_vert:
                        print(ship_or_input + ' does not represent an Orientation')
                        continue
                except:
                    print(ship_or_input + ' does not represent an Orientation')
                try:
                    ship_coord_input = str(input('Please enter the row, column for ship ' + ship + ': '))
                    ship_row_input, ship_col_input = ship_coord_input.split(',')
                    ship_row_input = int(ship_row_input)
                    ship_col_input = int(ship_col_input)
                    if ship_row_input not in range(self.num_rows):
                        print('row: {} is not a valid value for row.\n It should be an integer between 0 '
                              'and {}'.format(ship_row_input, self.num_rows - 1))
                        continue
                    if ship_col_input not in range(self.num_cols):
                        print('Column: {} is not a valid value for column.\n It should be an integer between 0 '
                              'and {}'.format(ship_col_input, self.num_cols - 1))
                        continue
                except:
                    print('Either row or col is not an integer')
                    continue
                """
                

                #Turn the ship orientation into a boolean value, makes it easier to code later
                def ship_orientation_bool(orientation_lingo: str) -> bool:
                    if orientation_lingo in valid_orientation_vert:
                        return True
                    elif orientation_lingo in valid_orientation_hori:
                        return False

                #call the ship_orientation bool object
                s = ship_orientation_bool(ship_or_input)

                #CellChange = Cell(self.num_rows, self.num_cols)
                #CellChange = CellChange.cell_update_move('hit')
                #return print(CellChange)

                return





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