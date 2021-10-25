from enum import Enum
import numpy as np

class Situation(Enum):
    """
    Enum of the possible situations
    """
    _root = "data/input"

    CHARLESTON = f"{_root}/charleston_road.in"
    HIGHER = f"{_root}/lets_go_higher.in"
    OPERA = f"{_root}/opera.in"
    LONDRES = f"{_root}/rue_de_londres.in"

class Util:
    def __init__(self):
        pass

    def parse_in(input: Situation) -> dict:
        with open(input.value) as file:
            # Read numbers
            h, w, r = map(int, file.readline().split())
            pb, pr, b = map(int, file.readline().split())
            bx, by = map(int, file.readline().split())

            # Read grid
            grid = []
            for _ in range(h):
                grid.append([char for char in file.readline()[:-1]])

            np_array = np.array(grid)
        
        return {"dim": (h, w), "radius": r, "backbone_price": pb, "router_price": pr,
                "budget": b, "backbone_pos": (bx, by), "grid": np_array}

    def parse_out():
        pass


def main():
    out = Util.parse_in(Situation.CHARLESTON)
    print(out["grid"])

if __name__ == "__main__":
    main()
