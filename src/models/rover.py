__author__ = "ptpedroj"

class Rover(object):
    def __init__(self, name, x, y, direction, grid):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.move_ops = {
            "N": lambda: Rover.move_north(self),
            "E": lambda: Rover.move_east(self),
            "S": lambda: Rover.move_south(self),
            "W": lambda: Rover.move_west(self)
        }


    @classmethod
    def execute_move(cls, self, move):
        pass


    @classmethod
    def turn_left(cls, self):
        pass


    @classmethod
    def turn_right(cls, self):
        pass


    @classmethod
    def move_north(cls, self):
        if self.grid.can_move_north(self.y):
            return cls(self.name, self.x, (self.y + 1), self.direction)
        else:
            raise Exception(f"Cannot move further North - {str(self)}")

    @classmethod
    def move_east(cls, self):
        if self.grid.can_move_east(self.y):
            return cls(self.name, (self.x + 1), self.y, self.direction)
        else:
            raise Exception(f"Cannot move further East - {str(self)}")

    @classmethod
    def move_south(cls, self):
        if self.grid.can_move_south(self.y):
            return cls(self.name, self.x, (self.y - 1), self.direction)
        else:
            raise Exception(f"Cannot move further South - {str(self)}")

    @classmethod
    def move_west(cls, self):
        if self.grid.can_move_west(self.y):
            return cls(self.name, (self.x - 1), self.y, self.direction)
        else:
            raise Exception(f"Cannot move further West - {str(self)}")



    def __str__(self):
        return f"Rover {self.name}: ({self.x}, {self.y}, {self.direction}) - Grid: ({self.grid.x}, {self.grid.y})"
