class Plane:
    def __init__(self, colour, uid):
        self.colour = colour
        self.uid = uid
        self.total_distance = 0
    def __repr__(self):
        return_string = ""
        colour_map = {"r":"\33[38;5;196m","g":"\33[38;5;46m","y":"\33[38;5;226m","b":"\33[38;5;51m","n":"\33[38;5;201m"}
        return_string += colour_map[self.colour]
        return_string += f"{self.uid}✈️"
        return return_string