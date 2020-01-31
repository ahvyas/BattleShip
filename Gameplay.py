

class Gameplay(object):
    def __init__(self, p1_name, p1_board, p2_name, p2_board, num_rows, num_cols, turn = '1',  **ship_info):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.ship_info = ship_info
        self.p1 = p1_name
        self.p2 = p2_name
        
