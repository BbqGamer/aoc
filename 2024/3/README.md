## Solution
```bash
# Part1:
grep -oP "mul\(\d+,\d+\)" input.txt | awk -f prog.awk
# Part2:
grep -oP "mul\(\d+,\d+\)|do\(\)|don't\(\)" input.txt | awk -f prog.awk
```
