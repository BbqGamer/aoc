{
    split($0,a)
    asort(a)
    res += a[length(a)] - a[1]
}
END {
    print r
}
