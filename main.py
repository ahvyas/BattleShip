from Setup import setup
from Gameplay import Gameplay

if __name__ == '__main__':
    pass

# Game setup
rows, cols, ship_info, p1_name, p1_board, p2_name, p2_board = setup()

# Game begins
while not someone_wins():
    Gameplay(p1_name, p1_board, p2_name, p2_board, rows, cols, play_turn, **ship_info)
    play_turn = Turn()






