__author__ = "ptpedroj"

class Rover(object):
    move_ops = None
    action_ops = None
    turn_left_ops = None
    turn_right_ops = None

    def __init__(self, name, x, y, direction, grid, actions):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.actions = actions

        if not Rover.move_ops:
            Rover.move_ops = {
                "N": Rover.move_north,
                "E": Rover.move_east,
                "S": Rover.move_south,
                "W": Rover.move_west
            }

        if not Rover.action_ops:
            Rover.action_ops = {
                "L": Rover.turn_left,
                "M": Rover.move,
                "R": Rover.turn_right
            }

        if not Rover.turn_left_ops:
            Rover.turn_left_ops = {
                "N": "W",
                "E": "N",
                "S": "E",
                "W": "S"
            }

        if not Rover.turn_right_ops:
            Rover.turn_right_ops = {
                "N": "E",
                "E": "S",
                "S": "W",
                "W": "N"
            }


    def process_actions(self):
        rover = self
        for action in self.actions:
            rover = rover.perform_action(action)
        return rover


    def perform_action(self, action):
        return Rover.action_ops[action](self)

    @classmethod
    def move(cls, self):
        return Rover.move_ops[self.direction](self)

    @classmethod
    def turn_left(cls, self):
        return cls(self.name, self.x, self.y, Rover.turn_left_ops[self.direction], self.grid, self.actions)

    @classmethod
    def turn_right(cls, self):
        return cls(self.name, self.x, self.y, Rover.turn_right_ops[self.direction], self.grid, self.actions)


    @classmethod
    def move_north(cls, self):
        if self.grid.can_move_north(self.y):
            return cls(self.name, self.x, (self.y + 1), self.direction, self.grid, self.actions)
        else:
            raise Exception(f"Cannot move further North - {repr(self)}")

    @classmethod
    def move_east(cls, self):
        if self.grid.can_move_east(self.y):
            return cls(self.name, (self.x + 1), self.y, self.direction, self.grid, self.actions)
        else:
            raise Exception(f"Cannot move further East - {repr(self)}")

    @classmethod
    def move_south(cls, self):
        if self.grid.can_move_south(self.y):
            return cls(self.name, self.x, (self.y - 1), self.direction, self.grid, self.actions)
        else:
            raise Exception(f"Cannot move further South - {repr(self)}")

    @classmethod
    def move_west(cls, self):
        if self.grid.can_move_west(self.y):
            return cls(self.name, (self.x - 1), self.y, self.direction, self.grid, self.actions)
        else:
            raise Exception(f"Cannot move further West - {repr(self)}")


    def __str__(self):
        return f"{self.x} {self.y} {self.direction}"

    def __repr__(self):
        return f"Rover({self.name}, ({self.x}, {self.y}, '{self.direction}', Grid({self.grid.x}, {self.grid.y}), {self.actions})"