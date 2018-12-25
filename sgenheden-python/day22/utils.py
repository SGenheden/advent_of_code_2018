
import fileinput

import numpy as np


def read_input():
    lines = [line.strip() for line in fileinput.input()]
    depth = int(lines[0].split(": ")[1])
    target = lines[1].split(": ")[1]
    targetx, targety = list(map(int, target.split(",")))
    return depth, targetx, targety


def geological_index(x, y, grid):
    if x == 0 and y == 0:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return grid[x-1, y]*grid[x,y-1]


def calc_erosion_level(targetx, targety, depth, grid):

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if x == targetx and y == targety:
                geo_index = 0
            else:
                geo_index = geological_index(x, y, grid)
            grid[x, y] = (geo_index + depth) % 20183


def define_grid(targetx, targety, depth, padding=0):

    grid = np.zeros([targetx+1+padding, targety+1+padding], dtype=int)
    erosion_level = np.zeros([targetx+1+padding, targety+1+padding], dtype=int)
    calc_erosion_level(targetx, targety, depth, erosion_level)
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if erosion_level[x, y] % 3 == 0:
                grid[x, y] = '0'
            elif erosion_level[x, y] % 3 == 1:
                grid[x, y] = '1'
            elif erosion_level[x, y] % 3 == 2:
                grid[x, y] = '2'
    return grid
