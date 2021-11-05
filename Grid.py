import numpy as np
from typing import *


class GridVisualizer:
    @staticmethod
    def visualize(spot_types_grid: np.ndarray, router_coverage_grid: Optional[np.ndarray] = None,
                  backbone_coverage_grid: Optional[np.ndarray] = None, initial_backbone: Tuple = None):
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
    background: #ff3a3a;
}
.backbone-covered {
    background: #2979ff;
}
.router-covered.backbone-covered {
    background: #945A9D;
}

</style>
</head>
<body>
"""
        for y in range(h):
            for x in range(w):
                classes = []
                if initial_backbone == (y, x):
                    spot_text = '<strong>b</strong>'
                else:
                    spot_text = spot_types_grid[y, x]
                if backbone_coverage_grid is not None and backbone_coverage_grid[y, x] == 1:
                    classes.append("backbone-covered")
                if router_coverage_grid is not None and router_coverage_grid[y, x] == 1:
                    classes.append("router-covered")
                classes = " ".join(classes)
                out += f"<span class=\"{classes}\">{spot_text}</span>"
            out += "<br>"

        out += """
        <br><br>
        <strong>Legend</strong><br><br>
        <span class='backbone-covered'>&nbsp&nbsp</span>: Backbone-covered<br><br>
        <span class='router-covered'>&nbsp&nbsp</span>: Router-covered<br><br>
        <span class='router-covered backbone-covered'>&nbsp&nbsp</span>: Router-covered AND Backbone-covered<br><br>
        </body>
        </html>
        """
        with open("test.html", "w") as f:
            f.write(out)


