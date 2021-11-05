import Util
from Building import Building
from Grid import GridVisualizer


def main():
    out = Util.parse_in(Util.Situation.TEST)
    building = Building(out)

    score, router_cells, backbone_cells = building.algo(building.targets, [], [])
    building.update_router_and_connection_grid(router_cells, backbone_cells)
    Util.parse_out(backbone_cells, router_cells, 'charleston.out')
    GridVisualizer.visualize(building.grid, building.router_coverage_grid, building.connection_coverage_grid,
                             out["backbone_pos"])

if __name__ == "__main__":
    main()
