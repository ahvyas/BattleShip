import time


class Ship(object):
    def __init__(self, ship_list: dict):
        self.ship_list = ship_list

    def new_dict(self) -> dict:
        new_dict = {name: size for name, size in self.ship_list.items()}
        return new_dict

    def update_ship(self, p_name: str, s_list: dict, ship_first_letter: str) -> dict:
        s = s_list
        for name, size in s.items():
            size = int(size)
            if str(name).startswith(ship_first_letter):
                updated_size = int(s[name])
                updated_size -= 1
                if updated_size < 1:
                    print("You destroyed {}'s {}\n".format(p_name, name))
                    time.sleep(1)
                    s.pop(name)
                    return s
                s[name] = updated_size
                return s
