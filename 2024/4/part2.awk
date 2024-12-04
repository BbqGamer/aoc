BEGIN {FS = ""}
{
    offset = NF * (NR - 1)
    for (i = 1; i <= NF; i++) {
        si = offset + i - 1
        for (x = 0; x < 3; x++) {
            for (y = 0; y < 3; y++) {
                pos = si - (x + NF * y)
                squares[pos][x + 3 * y] = $i
            }
        }
    }
} END {
    for (i = 0; i < NR - 2; i++) {
        for (j = 0; j < NF - 2; j++) {
            pos = i * NF + j
            for (v in squares[pos]) {
                printf squares[pos][v]
            }
            printf "\n"
        }
    }
}
