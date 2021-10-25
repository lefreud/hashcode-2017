import numpy as np
from matplotlib.colors import ListedColormap
from typing import *

custom_color_map = ListedColormap(["black", "white", "brown", "yellow", "green", "blue"])


class GridVisualizer:
    @staticmethod
    def visualize(spot_types_grid: np.ndarray, router_coverage_grid: Optional[np.ndarray] = None,
                  backbone_coverage_grid: Optional[np.ndarray] = None):
        h, w = spot_types_grid.shape
        out = ""
        out += """
        <html>
        <head>
<style>
body {
  font-family: Courier new;
}
.router-covered {
    background: chartreuse;
}
.backbone-covered {
    background: aqua;
}

</style>
</head>
<body>
"""
        for y in range(h):
            for x in range(w):
                classes = []
                if backbone_coverage_grid is not None and backbone_coverage_grid[y, x] == 1:
                    classes.append("backbone-covered")
                elif router_coverage_grid is not None and router_coverage_grid[y, x] == 1:
                    classes.append("router-covered")
                classes = " ".join(classes)
                out += f"<span class=\"{classes}\">{spot_types_grid[y, x]}</span>"
            out += "<br>"

        out += """
        </body>
        </html>
        """
        with open("test.html", "w") as f:
            f.write(out)


