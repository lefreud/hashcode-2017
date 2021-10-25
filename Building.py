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

    def calculer_score(self, liste_routers: list[tuple], liste_backbones: list[tuple]) -> int:
        return 1000*len(self.liste_targets) + self.budget - len(liste_backbones)*self.cout_backbones - len(liste_routers)*self.cout_routers