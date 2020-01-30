from Board import Board

class Ship(object):
    def __init__(self, name: str, size: int, orientation: bool) -> list:
        self.name = name
        self.size = size
        self.ortn = orientation

    def ship_loc(self, *args) -> list:
        l = []
        for i in range(self.size):
            l.append(args)
        return l

tst = Ship('ace', 2, False)
i = tst.ship_loc((3, 4), (5, 6))
print(i)