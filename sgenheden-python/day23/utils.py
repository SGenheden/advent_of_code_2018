
import fileinput
import re


def dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])


def read_input():
    radii = {}
    for line in fileinput.input():
        m = re.match("pos=<(.+),(.+),(.+)>, r=(.+)", line.strip())
        intlst = [int(m.group(i)) for i in range(1,5)]
        radii[(intlst[0], intlst[1], intlst[2])] = intlst[3]
    return radii
