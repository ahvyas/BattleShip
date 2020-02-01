from Setup import setup
from Gameplay import Gameplay

if __name__ == '__main__':
    pass

# Game setup
rows, cols, ship_info, p1_name, p1_board, p2_name, p2_board = setup()


# Game begins
battle = Gameplay(p1_name, p1_board, p2_name, p2_board, rows, cols, **ship_info)
battle.play()





