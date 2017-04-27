__author__ = "ptpedroj"

from src.models.grid import Grid
from src.models.rover import Rover

class Settings(object):
    def __init__(self, input):
        input_lines = input.split("\n")
        gridSettings = list(map(int, input_lines[0].split()))

        self.grid = Grid(*gridSettings)

        input_lines = input_lines[1:len(input_lines) - 1]

        self.rovers = self.get_rover_settings(input_lines)


    def get_rover_settings(self, input_lines):
        rovers = []
        if len(input_lines) % 2 == 0:
            rover_count = 0
            for i in range(0, len(input_lines), 2):
                rover_count += 1
                rover_data = input_lines[i].split()
                rover_actions = list(input_lines[i + 1])
                rovers.append(
                    Rover(
                        name = f"Rover {rover_count}",
                        x = int(rover_data[0]),
                        y = int(rover_data[1]),
                        direction = rover_data[2],
                        grid = self.grid,
                        actions = rover_actions
                    )
                )
            return rovers

        else:
            raise Exception("Input should have an odd number of lines, not even.")
