import sys

IN = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<
v>>v<<"""

OUT = 10092


def test_part1():
    assert part1(IN) == OUT


def part1(data: str):
    pass


WALL = 0
BOX = 1


DIR_MAP = {"<": -1j, "^": -1, ">": 1j, "v": 1}


def parse(data: str):
    grid2d, dirs = data.split("\n\n")
    robot = -1

    grid = dict()
    for i, row in enumerate(grid2d.split("\n")):
        for j, c in enumerate(row):
            comp = complex(i, j)
            if c == "#":
                grid[comp] = WALL
            elif c == "O":
                grid[comp] = BOX
            elif c == "@":
                robot = comp

    dirs = [DIR_MAP[d] for d in dirs.replace("\n", "")]

    assert robot != -1
    return grid, dirs, robot


def render(grid, robot):
    for i in range(10):
        for j in range(10):
            c = complex(i, j)
            if c == robot:
                print("@", end="")
            elif c not in grid:
                print(".", end="")
            elif grid[c] == WALL:
                print("#", end="")
            else:
                print("0", end="")
        print()


if __name__ == "__main__":
    data = sys.stdin.read()
    grid, dirs, robot = parse(data)

    for it, d in enumerate(dirs):
        new = robot + d
        if new not in grid:
            robot = new
            continue

        cur = new
        while cur in grid and grid[cur] == BOX:
            cur += d

        if cur not in grid:
            robot = new
            del grid[new]
            grid[cur] = BOX

    result = 0
    for c in grid:
        if grid[c] == BOX:
            result += c.real * 100 + c.imag

    print(result)
