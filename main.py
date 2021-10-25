import Util
from Building import Building


def main():
    out = Util.parse_in(Util.Situation.CHARLESTON)
    building = Building(out)

    score, router_cells, backbone_cells = building.algo(building.targets, [], [])

    Util.parse_out(backbone_cells, router_cells, 'charleston.out')


if __name__ == "__main__":
    main()
