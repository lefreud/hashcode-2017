import numpy as np


class Building:
    def __init__(self, nb_rows: int, nb_columns: int, router_range: int, backbone_price: int, router_price: int, budget: int, backbone_pos: tuple, grid: np.ndarray):
        self.grid = grid
        self.nb_rows = nb_rows
        self.nb_columns = nb_columns
        self.router_range = router_range
        self.backbone_price = backbone_price
        self.router_price = router_price
        self.budget = budget
        self.backbone_pos = backbone_pos



