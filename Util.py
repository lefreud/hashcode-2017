from enum import Enum
import numpy as np


class Situation(Enum):
    """
    Enum of the possible situations
    """
    _root = "data/input"
    TEST = f"{_root}/test.in"
    CHARLESTON = f"{_root}/charleston_road.in"
    HIGHER = f"{_root}/lets_go_higher.in"
    OPERA = f"{_root}/opera.in"
    LONDRES = f"{_root}/rue_de_londres.in"


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


def parse_out(backbone_cells: list[tuple], router_cells: list[tuple], filename: str):
    with open(f"data/output/{filename}", "w") as file:
        file.write(f"{len(backbone_cells)}\n")
        for cell in backbone_cells:
            file.write(f"{cell[0]} {cell[1]}\n")
        file.write(f"{len(router_cells)}\n")
        for cell in router_cells:
            file.write(f"{cell[0]} {cell[1]}\n")


def main():
    #out = parse_in(Situation.CHARLESTON)
    #print(out["grid"])

    backbone_cells = [(1, 1), (2, 2), (3, 3)]
    router_cells = [(1, 1), (2, 2), (3, 3)]

    parse_out(backbone_cells, router_cells, "charleston_road.out")


if __name__ == "__main__":
    main()
