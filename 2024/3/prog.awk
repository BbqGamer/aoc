/do\(\)/ {
    disabled = 0
}
/don't\(\)/ {
    disabled = 1
}
/mul\([0-9]+,[0-9]+\)/ {
    if (disabled) next
    match($0, /mul\(([0-9]+),([0-9]+)\)/, a)
    res += a[1] * a[2]
}
END { print res }

