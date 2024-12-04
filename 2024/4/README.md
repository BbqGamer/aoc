Part 1:
```
awk -f part1.awk input.txt > lines; cat <(grep -o "XMAS" lines) <(grep -o "SAMX" lines) | wc -l
```

Part 2:
```
awk -f part2.awk input.txt | grep -e "M.S.A.M.S" -e "M.M.A.S.S" -e "S.M.A.S.M" -e "S.S.A.M.M" | wc -l
```
