import fileinput


def read_input():
    points = []
    for line in fileinput.input():
        coords = tuple(map(int,line.strip().split(',')))
        points.append(coords)
    return points


def dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])+abs(a[3]-b[3])


if __name__ == "__main__":
    points = read_input()

    # Initialization phase
    within = {point: set() for point in points}
    for i, point1 in enumerate(points):
        for point2 in points:
            if dist(point1, point2) <= 3:
                within[point1].add(point2)

    # Merge phase
    merged = True
    while merged:
        merged = False
        for point1 in points:
            if point1 not in within:
                continue
            for point2 in points:
                if point2 != point1 and point2 in within and within[point1].intersection(within[point2]):
                    merged = True
                    within[point1].update(within[point2])
                    del within[point2]
    print(f"Number of constellations are {len(within)}")
