Part 1:
```
cat <(grep -o "XMAS" lines) <(grep -o "SAMX" lines) | wc -l
```

Part 2:
```
awk -f squares.awk | grep -e "M.S.A.M.S" -e "M.M.A.S.S" -e "S.M.A.S.M" -e "S.S.A.M.M" | wc -l
```
