from UpdateBoard import UpdateBoard

class Board(object):
    def __init__(self, num_rows: int, num_cols: int, **kwargs: dict) -> None:
        #rows and columns
        self.num_rows = num_rows
        self.num_cols = num_cols
        #initializes the board matrix
        self.b = []
        #Types of states of board
        self.empty = '*'
        self.hit = 'X'
        self.miss = 'O'
        ship_l = [F'{key}, {value}' for key, value in kwargs.items()]

    def initialize_board(self):
        #creates 2D matrix for our game
        self.b = [[self.empty for i in range(self.num_rows)] for j in range(self.num_cols)]

        #creates GUI for board
        print(end='  ')
        for hornum in range(self.num_rows):
            print(str(hornum), end=" ")
        print('')
        for index, self.num_rows in enumerate(self.b):
            print(index, end=' ')
            print(*self.num_rows, end='\n')
        return self.b


    def user_place_ship(self):
        pass


    def update_board(self):
        ub = UpdateBoard()
        ub.update(self.b)