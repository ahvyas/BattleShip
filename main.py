from Setup import Setup
from Game import Game

if __name__ == '__main__':
    pass

# Game setup
s = Setup()
rows, cols, ship_info, p1_name, p1_board, p2_name, p2_board = s.setup()


# Game begins
battle = Game(p1_name, p1_board, p2_name, p2_board, rows, cols, **ship_info)
battle.play()





