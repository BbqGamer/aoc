import sys

WALL = 0
BOX = 1


DIR_MAP = {"<": complex(0, -1), "^": complex(-1, 0), ">": 1j, "v": 1}


def parse(data: str):
    grid2d, dirs = data.split("\n\n")
    robot = -1

    grid = dict()
    for i, row in enumerate(grid2d.split("\n")):
        for j, c in enumerate(row):
            comp = complex(i, j * 2)
            if c == "#":
                grid[comp] = WALL
                grid[comp + 1j] = WALL
            elif c == "O":
                grid[comp] = BOX
            elif c == "@":
                robot = comp

    dirs = [DIR_MAP[d] for d in dirs.replace("\n", "")]

    assert robot != -1
    return grid, dirs, robot


def render(grid, robot):
    for i in range(10):
        for j in range(20):
            c = complex(i, j)
            if c == robot:
                print("@", end="")
            elif c not in grid:
                if c - 1j in grid and grid[c - 1j] == BOX:
                    print("]", end="")
                else:
                    print(".", end="")
            elif grid[c] == WALL:
                print("#", end="")
            else:
                print("[", end="")
        print()


def can_box_move(c, d, grid):
    boxpos = get_box(c, grid)
    assert boxpos is not None

    newpos = boxpos + d
    if is_wall(newpos, grid) or is_wall(newpos + 1j, grid):
        return False

    if d.real == 0:
        to_check = newpos
        if d.imag == 1:
            to_check += 1j
        return empty(to_check, grid) or can_box_move(to_check, d, grid)
    else:
        if empty(newpos, grid) and empty(newpos + 1j, grid):
            return True
        for x in [0, 1j]:
            tomovepos = get_box(newpos + x, grid)
            if tomovepos is None:
                continue

            if not can_box_move(tomovepos, d, grid):
                return False
        return True


def empty(c, grid):
    return c not in grid and not (c - 1j in grid and grid[c - 1j] == BOX)


def is_wall(c, grid):
    return c in grid and grid[c] == WALL


def get_box(c, grid):
    if c in grid and grid[c] == BOX:
        return c
    if c - 1j in grid and grid[c - 1j] == BOX:
        return c - 1j
    return None


def move_boxes(c, d, grid):
    boxpos = get_box(c, grid)
    if boxpos is None:
        return

    newpos = boxpos + d
    if d.real == 0:
        tomovepos = newpos
        if d.imag == 1:
            tomovepos += 1j
        move_boxes(tomovepos, d, grid)
    else:
        for x in [0, 1j]:
            tomovepos = newpos + x
            move_boxes(tomovepos, d, grid)

    grid[newpos] = BOX
    del grid[boxpos]


if __name__ == "__main__":
    data = sys.stdin.read()
    grid, dirs, robot = parse(data)

    for it, d in enumerate(dirs):
        new = robot + d
        if empty(new, grid):
            robot = new
            continue

        if is_wall(new, grid):
            continue

        if can_box_move(new, d, grid):
            move_boxes(new, d, grid)
            robot = new

    result = 0
    for c in grid:
        if grid[c] == BOX:
            result += c.real * 100 + c.imag

    print(result)
