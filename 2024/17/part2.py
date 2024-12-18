import re
import sys


def iteration(a):
    b = a & 7
    b = b ^ 5
    c = a >> b
    b = b ^ 6
    b = b ^ c
    return b & 7


def test_iteration():
    A = 47792830
    EXP = [2, 1, 3, 0, 5, 2, 3, 7, 1]
    for exp in EXP:
        assert iteration(A) == exp
        A >>= 3


def parse(data: str) -> list[int]:
    PATTERN = (
        r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([0-9,]+)"
    )
    m = re.match(PATTERN, data)
    if m is None:
        raise ValueError("Invalid input")
    return list(map(int, m.group(4).split(",")))


if __name__ == "__main__":
    program = parse(sys.stdin.read())

    def solve(current, i):
        if i < 0:
            return tuple()

        current <<= 3
        for j in range(8):
            candidate = current + j
            res = iteration(candidate)
            if res == program[i]:
                rest = solve(candidate, i - 1)
                if rest is not None:
                    return (j,) + rest
        else:
            return None

    triples = solve(0, len(program) - 1)
    if triples is not None:
        res = 0
        for triple in triples:
            res <<= 3
            res += triple
        print(res)
    else:
        print("Not found")
