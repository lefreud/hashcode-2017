import numpy as np
import math
import Util


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

        self.router_coverage_grid = np.zeros(self.grid.shape)

        self.connection_coverage_grid = np.zeros(self.grid.shape)

    def create_liste_targets_and_mur(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == ".":
                    self.targets.append((i,j))
                elif self.grid[i][j] == "#":
                    self.walls.append((i,j))

    def calculer_score(self, liste_routers: list[tuple], liste_backbones: list[tuple]) -> int:
        return 1000*len(self.targets) + self.budget - len(liste_backbones)*self.backbone_price - len(liste_routers)*self.router_price

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

    def calculer_liaison_routeur(self, target: tuple, liste_connection: list[tuple]) -> list[tuple]:
        min_distance = math.inf
        for connection in liste_connection:
            distance = self.get_distance_liaison(connection, target)
            if self.get_distance_liaison(target, connection) < min_distance:
                start = connection
                min_distance = distance

        if self.get_distance_liaison(target, self.backbone_pos) < min_distance:
            start = self.backbone_pos

        return self.get_path(start, target)

    def get_distance_liaison(self, start:tuple, target:tuple):
        diago_distance = min(abs(start[0] - target[0]), abs(start[1] - target[1]))
        straight_distance = max(abs(start[0] - target[0]), abs(start[1] - target[1])) - diago_distance
        return diago_distance + straight_distance

    def get_path(self, start: tuple, target: tuple):
        # Diago
        diago_distance = min(abs(start[0] - target[0]), abs(start[1] - target[1]))
        path_positions = []

        if target[0] > start[0]:
            step_y = 1
        else:
            step_y = -1
        if target[1] > start[1]:
            step_x = 1
        else:
            step_x = -1

        for i in range(1, diago_distance):
            path_positions.append((start[0] + step_y * i, start[1] + step_x * i))

        # Straight
        position_after_diago = (start[0] + diago_distance * step_y, start[1] + diago_distance * step_x)
        if target[0] == position_after_diago[0]:
            step_y = 0
        elif target[1] == position_after_diago[1]:
            step_x = 0

        straight_distance = max(abs(start[0] - target[0]), abs(start[1] - target[1])) - diago_distance
        for i in range(straight_distance + 1):
            path_positions.append((position_after_diago[0] + step_y * i, position_after_diago[1] + step_x * i))
        return path_positions

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

    def update_router_and_connection_grid(self, liste_connection, liste_router):
        for connection in liste_connection:
            self.connection_coverage_grid[connection[0], connection[1]] = 1
        for router in liste_router:
            self.router_coverage_grid[router[0], router[1]] = 1


if __name__ == "__main__":
    b = Building(Util.parse_in(Util.Situation.CHARLESTON))
    print(b.calculer_liaison_routeur((0,0), []))
    #print(b.backbone_pos)
    #print(b.get_distance_liaison((0,0), (120,90)))

