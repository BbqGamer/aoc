import pytest

from part2 import BOX, WALL, can_box_move, move_boxes, parse

EXAMPLE = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""


"""
VISUALIED STARTING STATE:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############
"""

GRID, DIRS, ROBOT = parse(EXAMPLE)


def test_can_box_move():
    assert can_box_move(GRID, complex(3, 9), -1j)
    assert can_box_move(GRID, complex(3, 8), -1j)

    assert can_box_move(GRID, complex(3, 7), 1)
    assert can_box_move(GRID, complex(3, 6), 1)

    assert can_box_move(GRID, complex(3, 7), 1j)
    assert can_box_move(GRID, complex(3, 6), 1j)

    assert can_box_move(GRID, complex(4, 7), -1)
    assert can_box_move(GRID, complex(4, 6), -1)


def test_move_boxes_left():
    grid = GRID.copy()
    assert 3 + 9j not in grid
    assert grid[3 + 8j] == BOX

    move_boxes(3 + 9j, -1j, grid)
    assert 3 + 9j not in grid
    assert 3 + 8j not in grid

    assert grid[3 + 7j] == BOX
    assert 3 + 6j not in grid

    assert grid[3 + 5j] == BOX


def test_move_boxes_right():
    grid = GRID.copy()
    assert grid[3 + 6j] == BOX
    assert 3 + 7j not in grid
    move_boxes(3 + 6j, 1j, grid)

    assert 3 + 6j not in grid
    assert grid[3 + 7j] == BOX

    assert 3 + 8j not in grid

    assert grid[3 + 9j] == BOX
    assert 3 + 10j not in grid


@pytest.mark.parametrize("x", [0, 1j])
def test_move_boxes_up(x):
    grid = GRID.copy()
    assert grid[4 + 6j] == BOX
    assert 4 + 7j not in grid

    move_boxes(4 + 6j + x, -1, grid)

    assert 4 + 6j not in grid
    assert 4 + 7j not in grid

    assert grid[3 + 6j] == BOX
    assert 3 + 7j not in grid

    assert grid[2 + 6j] == BOX
    assert 2 + 7j not in grid


@pytest.mark.parametrize("x", [0, 1j])
def test_can_bo_move_into_wall(x):
    box = 1 + 1j
    grid = {
        1 + 0j: WALL,
        box: BOX,
        1j: WALL,
        2 + 2j: WALL,
        1 + 3j: WALL,
    }
    assert not can_box_move(grid, box + x, -1j)
    assert not can_box_move(grid, box + x, 1j)
    assert not can_box_move(grid, box + x, 1)
    assert not can_box_move(grid, box + x, -1)
