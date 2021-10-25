import numpy as np
from Grid import GridVisualizer


def main():
    spot_types_grid = np.array([['#', '.'], ['#', '-']])
    router_coverage_grid = np.zeros((2, 2))
    router_coverage_grid[0, 0] = 1
    backbone_coverage_grid = np.zeros((2, 2))
    backbone_coverage_grid[0, 0] = 1
    backbone_coverage_grid[1, 0] = 1
    GridVisualizer.visualize(spot_types_grid, router_coverage_grid, backbone_coverage_grid)


if __name__ == '__main__':
    main()

