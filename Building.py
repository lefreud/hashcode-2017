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
        self.targets = []
        self.walls = []
        self.create_liste_targets_and_mur()

    def create_liste_targets_and_mur(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == ".":
                    self.targets.append((i,j))
                elif self.grid[i][j] == "#":
                    self.walls.append((i,j))

    def calculer_score(self, liste_routers: list[tuple], liste_backbones: list[tuple]) -> int:
        return 1000*len(self.targets) + self.budget - len(liste_backbones)*self.cout_backbones - len(liste_routers)*self.cout_routers

    def algo(self, targets, liste_routeur, liste_connection):
        if len(targets) == 0 :
            score = self.calculer_score(liste_routeur, liste_connection)
            return [score, liste_routeur, liste_connection]
        score_max = -1
        best_list_routeur = []
        best_list_connection = []
        for target in targets:
            connections_temp = self.calculer_liaison_routeur(target, liste_connection)
            liste_connection_temp = liste_connection
            liste_connection_temp.extends(connections_temp)
            liste_routeur_temp = liste_routeur
            liste_routeur_temp.append(target)
            targets_diminuer = self.diminuer_grid(target, targets)
            score_temp, liste_routeur, liste_connection = self.algo(targets_diminuer, liste_routeur_temp, liste_connection_temp)
            if score_temp < score_max:
                score_max = score_temp
                best_list_connection = liste_connection_temp
                best_list_routeur = liste_routeur_temp

        return [score_max, best_list_routeur, best_list_connection]

    def calculer_liaison_routeur(self, target, liste_connection):
        #TODO

    def diminuer_grid(self, new_target, targets):
        targets_temp = targets
        for target in targets_temp:
            if abs(new_target[0] - target[0]) <= self.router_range and abs(new_target[1] - target[1]) <= self.router_range:
                if self.check_if_wall(target, new_target):
                    targets_temp.remove(target)
        return targets_temp


    def check_if_wall(self, target, router_pos):
        for wall in self.walls:
            if min(router_pos[0],target[0]) <= wall[0] <= max(router_pos[0],target[0]) and min(router_pos[1],target[1]) <= wall[1] <= max(router_pos[1],target[1]):
                return True
        return False