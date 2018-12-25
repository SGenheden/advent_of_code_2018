
from utils import read_input, define_grid


if __name__ == "__main__":
    depth, targetx, targety = read_input()
    print(depth, targetx, targety)
    grid = define_grid(targetx, targety, depth)
    print(grid.shape)
    for row in grid.T:
        print("".join([str(c) for c in row]))
    print(f"The total risk level is {grid.sum()}")
