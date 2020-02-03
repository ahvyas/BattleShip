
class Player(object):
    def __init__(self, name: str = None):
        self.name = name

    def __str__(self):
        return self.name

    def return_name(self):
        return self.name

    def get_name_1(self) -> str:
        self.name1 = input('Player 1, please enter name:')
        print('Welcome to Battleship, General {}. Follow instructions to deploy your warships.'.format(self.name1.upper()))
        return self.name1

    def get_name_2(self) -> str:
        while True:
            self.name2 = input('Player 2, please enter name:')
            if self.name2.lower() == self.name1.lower():
                print('Name has been taken, please choose another name')
                continue
            break
        print('Welcome to Battleship, General {}. Follow instructions to deploy your warships.'.format(self.name2.upper()))
        return self.name2
