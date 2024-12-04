function print_arr(arr) { 
    for (i in arr) { printf arr[i] } 
    printf "\n"
}
function print_2d_arr(arr) { for (i in arr) print_arr(arr[i]) }
BEGIN {FS = ""}
{
    for (i = 1; i <= NF; i++) {
        cols[i][NR] = $i
        diags[i - NR][NR] = $i
        diags2[NF - i - NR + 1][NR] = $i
    }
    print $0
}
END {
    print_2d_arr(cols);
    print_2d_arr(diags);
    print_2d_arr(diags2);
}
