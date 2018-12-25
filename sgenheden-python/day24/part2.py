
from utils import read_input, count, selection_phase, attacking_phase


if __name__ == "__main__":

    lines = None
    inc = 100
    ceil = 2000
    for inc in [100, 10, 5, 1]:
        for boost in range(1, ceil+1, inc):
            groups, lines = read_input(boost=boost, lines=lines)
            nimmunes, ninfections = count(groups)
            while nimmunes > 0 and ninfections > 0:
                selection_phase(groups)
                try:
                    attacking_phase(groups)
                except:
                    break
                groups = [g for g in groups if g.units > 0]
                nimmunes, ninfections = count(groups)

            nimmunes, ninfections = count(groups)
            if nimmunes > 0 and ninfections == 0:
                print(f"There are {nimmunes} immune system units and {ninfections} "
                      f"infection units with boost {boost} searching with increment {inc}")
                break
        ceil = boost
