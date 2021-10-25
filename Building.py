import numpy as np


class Building:
    def __init__(self, data: dict):
        self.grid = data['grid']
        self.nb_rows, self.nb_columns = data['dim']
        self.router_range = data['radius']
        self.backbone_price = data['backbone_price']
        self.router_price = data['router_price']
        self.budget = data['budget']
        self.backbone_pos = data['backbone_pos']

    def calculer_score(self, liste_routers: list[tuple], liste_backbones: list[tuple]) -> int:
        return 1000*len(self.liste_targets) + self.budget - len(liste_backbones)*self.cout_backbones - len(liste_routers)*self.cout_routers
