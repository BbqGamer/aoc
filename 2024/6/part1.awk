BEGIN {FS = ""}
{
    for (i = 1; i <= NF; i++) {
        if ($i == "#") obstacles[NR][i] = 1
        if ($i == "^") { guardx = i; guardy = NR }
    }
} END {
    dx = 0; dy = -1  # zwrócony w górę
    while(guardx >= 1 && guardy >= 1 && guardx <= NF && guardy <= NR) {
        visited[guardy][guardx] = 1
        newx = guardx + dx; newy = guardy + dy
        if (obstacles[newy][newx]) { # napotkano przeszkodę
            if (dx == 0) {
                if (dy == -1) dx = 1
                else dx = -1   
                dy = 0
            } else {
                if (dx == 1) dy = 1
                else dy = -1
                dx = 0
            }
        } else { guardx = newx; guardy = newy }
    }

    # count number of visited tiles
    for (row in visited) {
        for (col in visited[row]) res += visited[row][col]
    }
    print res
}
