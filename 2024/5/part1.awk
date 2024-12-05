BEGIN { FS = "|" }
/\|/{
    x[$1][$2] = 1
    y[$2][$1] = 1
}
/^$/ { FS = "," }
/,/ { 
    for (i = 1; i < NF; i++)
        if (!($(i+1) in x[$1] && $(i) in y[$(i+1)])) next
    sum += $(int((NF + 1) / 2))
}
END { print sum }
