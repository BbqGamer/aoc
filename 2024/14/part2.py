import re
import sys
import time

import numpy as np

PATTERN = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)\n"

robots = []
for match in re.findall(PATTERN, sys.stdin.read()):
    robots.append(list(map(int, match)))
robots = np.array(robots)

lenx = max(robots, key=lambda r: r[0])[0] + 1
leny = max(robots, key=lambda r: r[1])[1] + 1
midx = lenx // 2
midy = leny // 2


def render(robots):
    grid = [["." for _ in range(lenx)] for _ in range(leny)]
    for x, y, _, _ in robots:
        grid[y][x] = "#"
    return "\n".join("".join(row) for row in grid)


def dist(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


def chaos(robots):
    xcenter, ycenter, _, _ = np.mean(robots, axis=0)
    score = 0
    for x, y, _, _ in robots:
        score += dist(x, y, xcenter, ycenter)
    return score


best = float("inf")
it = 0
while True:
    for i in range(len(robots)):
        x, y, vx, vy = robots[i]
        robots[i][0] = (x + vx) % lenx
        robots[i][1] = (y + vy) % leny

    score = chaos(robots)
    if score < best:
        print(it)
        best = score
        print(score)
        print(render(robots))
    it += 1
