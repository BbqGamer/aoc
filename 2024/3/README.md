## Solution
```bash
# Part1:
grep -oE "mul\([0-9]+,[0-9]+\)" input.txt | sed -En 's/mul\(([0-9]+),([0-9]+)\)/\1 \2/p' | awk '{res+=$1*$2}END{print res}'
# Part2:
grep -oE "[a-z\']+\([0-9\,]*)" input.txt | sed -Enf parse.sed | awk -f prog.awk
```
