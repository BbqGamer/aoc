import re
from itertools import chain
from pathlib import Path


def parse_input(text):
    patterns = [x.strip() for x in text[0].strip().split(",")]
    designs = text[2:]
    return patterns, designs


def find_all_ways(patterns, design, memo):
    if not design:
        return 1
    if design in memo:
        return memo[design]
    result = 0
    for pattern in patterns:
        if design.startswith(pattern):
            result += find_all_ways(patterns, design[len(pattern) :], memo)
    memo[design] = result
    return result


file = Path(__file__).parent / "input.txt"
text = file.read_text().strip().splitlines()
patterns, designs = parse_input(text)
possible_count = 0
all_ways = 0
for design_i, design in enumerate(designs):
    possible_ways_to_do_this_design = find_all_ways(patterns, design, {})
    if possible_ways_to_do_this_design > 0:
        possible_count += 1
    all_ways += possible_ways_to_do_this_design
print(possible_count)
print(all_ways)
