import numpy as np

import Util
from Grid import GridVisualizer
from Util import parse_in, Situation

def main():
    parsing_result = parse_in(Situation.CHARLESTON)
    grid = parsing_result["grid"]

    router_coverage_grid = np.zeros(grid.shape)
    router_coverage_grid[0, :] = 1
    backbone_coverage_grid = np.zeros(grid.shape)
    backbone_coverage_grid[:, 0] = 1

    GridVisualizer.visualize(grid, router_coverage_grid, backbone_coverage_grid)


if __name__ == '__main__':
    main()

