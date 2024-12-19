import sys
import time
from dataclasses import dataclass
from functools import cache
from pprint import pprint


@dataclass
class Trie:
    children: dict["str", "Trie"]
    terminal: bool = False


END = "$"


def parse(data: str):
    towels, desired = data.split("\n\n")
    towels = towels.split(", ")
    desired = desired.split("\n")

    trie = dict()
    tracked = {id(trie): trie}
    for towel in towels:
        cur = trie
        for c in towel:
            if c not in cur:
                cur[c] = dict()
                tracked[id(cur[c])] = cur[c]
            cur = cur[c]
        cur[END] = None

    return trie, tracked, desired


if __name__ == "__main__":
    trie, tracked, desired = parse(sys.stdin.read().strip())

    @cache
    def backtracking(cur_id, string):
        cur = tracked[cur_id]
        if not string:
            if END in cur:
                return 1
            return 0

        c = string[0]
        res = 0

        if END in cur and c in trie:
            res += backtracking(id(trie[c]), string[1:])

        if c in cur:
            res += backtracking(id(cur[c]), string[1:])

        return res

    count = 0
    for string in desired:
        res = backtracking(id(trie), string)
        count += res

    print("Part 2: ", count)
