from Battleship.Cell import Cell



class Mask(object):
    def __init__(self, num_rows: int, num_cols: int, existing_board: object) -> None:
        # rows and columns
        self.num_rows = num_rows
        self.num_cols = num_cols
        # initializes the board matrix
        self.b = existing_board
        self.empty = '*'
        self.hit = 'X'
        self.miss = 'O'

        self.cell = Cell(self.num_rows, self.num_cols)

    def initialize_mask(self) -> None:
        # creates 2D matrix for our game
        self.b = [[self.cell.first_board_init() for i in range(self.num_rows)] for j in range(self.num_cols)]

    def format_mask(self) -> None:
        print(end='  ')
        for hor_num in range(self.num_rows):
            print(str(hor_num), end=" ")
        print('')
        for index, num_row in enumerate(self.b):
            print(index, end=' ')
            print(*num_row, end='\n')

    def update_mask(self, x: int, y: int, hit_or_miss: str) -> None:
        self.b[x][y] = hit_or_miss

