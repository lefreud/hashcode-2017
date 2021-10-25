import Util
from Building import Building


def main():
    out = Util.parse_in(Util.Situation.CHARLESTON)
    building = Building(out)


if __name__ == "__main__":
    main()
