import re
import sys


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
        print(i)
        first = (False,) * len(lights)
        visited = set()
        queue = [(first, 0)]
        shouldEnd = False
        while queue:
            if shouldEnd:
                break
            item, count = queue.pop()
            visited.add(item)
            for button in buttons:
                newItem = list(item)
                for i in button:
                    newItem[i] = not newItem[i]
                new = tuple(newItem)
                if new in visited:
                    continue
                if lights == new:
                    res += count + 1
                    shouldEnd = True
                    break
                queue.insert(0, (new, count + 1))
    print(res)
