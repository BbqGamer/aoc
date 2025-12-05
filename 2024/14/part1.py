import re
import sys
from collections import defaultdict

PATTERN = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)\n"

robots = []
for match in re.findall(PATTERN, sys.stdin.read()):
    robots.append(list(map(int, match)))

lenx = max(robots, key=lambda r: r[0])[0] + 1
leny = max(robots, key=lambda r: r[1])[1] + 1

SECONDS = 100


def cycle1d(val, delta, length):
    neg = False
    if delta < 0:
        neg = True
        delta = -delta
        val = length - val

    to_boundary = length - val
    if to_boundary >= delta:
        newval = val + delta
    else:
        delta -= to_boundary
        newval = delta % length

    if neg:
        return (length - newval) % length
    return newval % length


def quadrant(x, y, lenx, leny):
    quad = 0
    if x == lenx // 2 or y == leny // 2:
        return -1
    if x > lenx // 2:
        quad += 1
    if y > leny // 2:
        quad += 2
    return quad


counter = defaultdict(lambda: 0)
for x, y, vx, vy in robots:
    newx, newy = cycle1d(x, vx * SECONDS, lenx), cycle1d(y, vy * SECONDS, leny)
    quad = quadrant(newx, newy, lenx, leny)
    counter[quad] += 1

part1 = 1
for k, v in counter.items():
    if k == -1:
        continue
    part1 *= v

print(part1)
