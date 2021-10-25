import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

custom_color_map = ListedColormap(["black", "white", "brown", "yellow", "green", "blue"])


class GridVisualizer:
    @staticmethod
    def visualize(spot_types_grid: np.ndarray, router_coverage_grid: np.ndarray, backbone_coverage_grid: np.ndarray):
        h, w = spot_types_grid.shape

        image = np.zeros((h * 3, w * 3))

        spot_types_grid_adapted = np.zeros((h, w))
        spot_types_grid_adapted[spot_types_grid == '#'] = 2 # wall = brown
        spot_types_grid_adapted[spot_types_grid == '.'] = 3 # target = yellow
        spot_types_grid_adapted[spot_types_grid == '-'] = 0 # void = black

        image[::3, ::3] = spot_types_grid_adapted
        image[::3, 1::3] = router_coverage_grid * 4
        image[1::3, ::3] = backbone_coverage_grid * 5

        # borders
        image[::, 2::3] = 1
        image[2::3, ::] = 1

        # display
        plt.figure(figsize=(h * 3, w * 3))
        plt.imshow(image, cmap=custom_color_map)
        plt.show()


