
from utils import read_input, dist


if __name__ == "__main__":
    radii = read_input()
    maxr = max([r for _, r in radii.items()])
    coord_max = [c for c, r in radii.items() if r == maxr][0]
    inrange = 0
    for coordi, ri in radii.items():
        if dist(coordi, coord_max) <= maxr:
            inrange +=1
    print(f"There are {inrange} of the nanobot with the strongest signal radius")
