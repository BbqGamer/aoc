import fileinput

grid = [list(map(int, line.strip())) for line in fileinput.input()]

trailheads = []
for y, row in enumerate(grid):
    for x, h in enumerate(row):
        if h == 0:
            trailheads.append((y, x))

count = 0
second_count = 0

for starty, startx in trailheads:
    reachable = set()
    ids = set()

    stack = [(starty, startx)]
    while stack:
        y, x = stack.pop()
        h = grid[y][x]
        if h == 9:
            reachable.add((y, x))
            second_count += 1
            continue

        if x > 0 and grid[y][x - 1] - h == 1:
            stack.append((y, x - 1))
        if y > 0 and grid[y - 1][x] - h == 1:
            stack.append((y - 1, x))
        if x < len(grid) - 1 and grid[y][x + 1] - h == 1:
            stack.append((y, x + 1))
        if y < len(grid[0]) - 1 and grid[y + 1][x] - h == 1:
            stack.append((y + 1, x))
    count += len(reachable)

print(count)
print(second_count)
