class Player(object):
    def __init__(self):
        self.name1 = None
        self.name2 = None

    def __str__(self):
        return self.name1, self.name2

    def get_name_1(self) -> str:
        self.name1 = input('Player 1 please enter your name: ')
        print("{}'s Placement Board".format(self.name1))
        return self.name1

    def get_name_2(self, name1: str) -> str:
        while True:
            self.name2 = input('Player 2 please enter your name: ')
            if self.name2.lower() == name1.lower():
                print('Someone is already using {} for their name.\nPlease choose another name.'.format(name1))
                continue
            break
        print("{}'s Placement Board".format(self.name2))
        return self.name2
