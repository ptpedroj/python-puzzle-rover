__author__ = "ptpedroj"

from src.models.rover import Rover
from src.models.grid import Grid
from src.models.settings import Settings




if __name__ == "__main__":
    #Load input. In this case, it is just a static string. Can replace with something more dynamic later.
    input = (
        "5 5\n"
        "1 2 N\n"
        "LMLMLMLMM\n"
        "3 3 E\n"
        "MMRMMRMRRM\n"
    )
    print(input)

    # Initialize objects
    settings = Settings(input)


    # Execute moves
    rovers = map(lambda r: r.process_actions(), settings.rovers)

    # Report Results
    for rover in rovers:
        print(rover)