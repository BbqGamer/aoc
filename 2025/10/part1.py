import re
import sys

import z3


def parse_line(line: str):
    """
    Parse a line like:
      "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    Returns (pattern, list_of_parenthesis_groups_as_lists_of_ints, list_from_braces)
    """
    line = line.strip()
    pattern_m = re.search(r"\[([^\]]+)\]", line)

    pattern = []
    if pattern_m:
        pattern = [True if x == "#" else False for x in pattern_m.group(1)]

    paren_groups = re.findall(r"\(([^)]*)\)", line)
    paren_lists: list[list[int]] = []
    for g in paren_groups:
        g = g.strip()
        if g == "":
            paren_lists.append([])
        else:
            paren_lists.append(
                tuple(int(x.strip()) for x in g.split(",") if x.strip() != "")
            )

    brace_m = re.search(r"\{([^}]*)\}", line)
    brace_list: list[int] = []
    if brace_m:
        s = brace_m.group(1).strip()
        if s:
            brace_list = [int(x.strip()) for x in s.split(",") if x.strip() != ""]

    return tuple(pattern), tuple(paren_lists), tuple(brace_list)


def parse_stream(lines):
    """
    Yield parsed tuples for each non-empty line from an iterable of lines.
    """
    for line in lines:
        line = line.strip()
        if not line:
            continue
        yield parse_line(line)


if __name__ == "__main__":
    res = 0
    for i, (lights, buttons, joltage) in enumerate(parse_stream(sys.stdin.readlines())):
        B = [z3.Bool(f"b{b}") for b in range(len(buttons))]
        equations = []
        for j, light in enumerate(lights):
            equation = 0
            for b, button in enumerate(buttons):
                if j in button:
                    equation += z3.If(B[b], 1, 0)
            equations.append((equation % 2) == int(light))
        s = z3.Optimize()
        s.add(equations)
        s.minimize(z3.Sum([z3.If(b, 1, 0) for b in B]))
        if s.check() == z3.sat:
            m = s.model()
            button_sum = sum(1 for b in B if z3.is_true(m[b]))
            res += button_sum
        else:
            print("unsat")
    print(res)
