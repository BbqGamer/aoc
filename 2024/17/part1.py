import re
import sys
from typing import NamedTuple


class State(NamedTuple):
    reg_a: int
    reg_b: int
    reg_c: int
    program: list[int]  # 3-bit numbers
    ip: int = 0


def parse(data: str) -> State:
    PATTERN = (
        r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([0-9,]+)"
    )
    m = re.match(PATTERN, data)
    if m is None:
        raise ValueError("Invalid input")
    reg_a, reg_b, reg_c, program = m.groups()
    return State(int(reg_a), int(reg_b), int(reg_c), list(map(int, program.split(","))))


if __name__ == "__main__":
    print(parse(sys.stdin.read()))
