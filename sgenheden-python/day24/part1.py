
from utils import read_input, count, selection_phase, attacking_phase


if __name__ == "__main__":
    groups, _ = read_input()
    nimmunes, ninfections = count(groups)
    while nimmunes > 0 and ninfections > 0:
        selection_phase(groups)
        attacking_phase(groups)
        groups = [g for g in groups if g.units > 0]
        nimmunes, ninfections = count(groups)

    nimmunes, ninfections = count(groups)
    print(f"There are {nimmunes} immune system units and {ninfections} infection units")
