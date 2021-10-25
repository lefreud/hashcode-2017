import numpy as np

class Algo:
    def algo(self, grid, targets, radius, liste_routeur, liste_connection, backbone):
        if len(targets) == 0 :
            cout = calculerCout()
            return [liste_connection, liste_routeur, cout]
        for target in targets:
            connections_temp = calculerLiaisonRouteur(target, liste_connection, backbone)
            liste_connection.extends(connections_temp)
            liste_routeur.append(target)
            grid_diminuer = diminuerGrid(grid, target, radius)
            cout_temp, liste_connection, liste_routeur = algo(grid_diminuer, targets, radius, )


        return {"routeur": liste_routeur, "fil": liste_connection}


    def updateCouverture(self, grid):
        etat_grid = np.zeros((grid.size(), grid[0].size()))
        for colonne  in range(grid.size()):
            for ligne in range(grid[colonne].size()):
                if grid[colonne][ligne] == ".":
                    etat_grid[colonne][ligne] = 0
                elif grid[colonne][ligne] == "-"

    def calculerCaseCouverte(self, grid, pos, radius):
        for i in range(radius):
            for j in range(radius):
                if

