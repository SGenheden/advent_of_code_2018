from utils import read_input, dist


if __name__ == "__main__":
    radii = read_input()

    removed = [False] * len(radii)
    while True:
        noutside = [0] * len(radii)
        for removedi, (coordi, ri) in zip(removed, radii.items()):
            if removedi:
                continue
            for j, (coordj, rj) in enumerate(radii.items()):
                if removed[j]:
                    continue
                if dist(coordi, coordj) > ri + rj:
                    noutside[j] += 1
        if sum(noutside) == 0:
            break
        maxn = max(noutside)
        removed = [r or n == maxn for r, n in zip(removed, noutside)]

    dists = [dist(c, (0,0,0)) - r
             for removedi, (c, r) in zip(removed, radii.items()) if not removedi]
    print(f"The distance to (0,0,0) is {max(dists)}")
