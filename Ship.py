class Ship(object):
    def __init__(self, name: str, size: int, orientation: bool) -> list:
        self.name = name
        self.size = size
        #True is vertical, False is horizontal
        self.ortn = None

    def ship_loc(self, *args) -> list:
        l = []
        for i in range(self.size):
            l.append(args)
        return l