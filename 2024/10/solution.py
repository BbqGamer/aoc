import fileinput

grid = [list(map(int, line.strip())) for line in fileinput.input()]

trailheads = []
for y, row in enumerate(grid):
    for x, h in enumerate(row):
        if h == 0:
            trailheads.append((y, x))

part1 = 0
part2 = 0

for starty, startx in trailheads:
    reachable = set()
    ids = set()

    stack = [(starty, startx)]
    while stack:
        y, x = stack.pop()
        h = grid[y][x]
        if h == 9:
            reachable.add((y, x))
            part2 += 1
            continue

        for dx in [-1, 1]:
            for dy in [-1, 1]:
                nx = x + dx
                ny = y + dy
                if (
                    nx >= 0
                    and ny >= 0
                    and nx < len(grid)
                    and ny < len(grid[0])
                    and grid[ny][nx] - h == 1
                ):
                    stack.append((ny, nx))
    part1 += len(reachable)

print(part1)
print(part2)
