__author__ = "ptpedroj"

class Grid(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def can_move_north(self, y):
        return y < self.y

    def can_move_east(self, x):
        return x < self.x

    def can_move_south(self, y):
        return y > 0

    def can_move_west(self, x):
        return x > 0

    def __repr__(self):
        return f"Grid({self.x}, {self.y})"