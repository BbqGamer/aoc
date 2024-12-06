BEGIN {FS = ""}
{
    for (i = 1; i <= NF; i++) {
        if ($i == "#") obstacles[NR][i] = 1
        if ($i == "^") { original_guardx = i; original_guardy = NR }
    }
}
END {
    dx = 0; dy = -1
    guardx = original_guardx; guardy = original_guardy
    while(guardx >= 1 && guardy >= 1 && guardx <= NF && guardy <= NR) {
        visited_p1[guardy][guardx] = 1
        newx = guardx + dx; newy = guardy + dy
        if (obstacles[newy][newx]) {
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
    for (row in visited_p1) {
        for (col in visited_p1[row]) res += visited_p1[row][col]
    }
    print "part 1", res

    for (ox = 1; ox <= NF; ox++) {
        for (oy = 1; oy <= NR; oy++) {
            if (!visited_p1[oy][ox]) continue

            obstacles[oy][ox] = 1

            dx = 0; dy = -1
            guardx = original_guardx; guardy = original_guardy
            delete visited; delete dxs; delete dys

            while(guardx >= 1 && guardy >= 1 && guardx <= NF && guardy <= NR) {
                visited[guardy][guardx] = 1

                if (dxs[guardy][guardx][dx] && dys[guardy][guardx][dy]) {
                    cycles += 1
                    break
                }

                dxs[guardy][guardx][dx] = 1
                dys[guardy][guardx][dy] = 1

                newx = guardx + dx
                newy = guardy + dy
                if (obstacles[newy][newx]) {
                    if (dx == 0) {
                        if (dy == -1) dx = 1
                        else dx = -1   
                        dy = 0
                    } else {
                        if (dx == 1) dy = 1
                        else dy = -1
                        dx = 0
                    }
                } else {
                    guardx = newx; guardy = newy
                }
            }
            obstacles[oy][ox] = 0
        }
    }
    print "Part 2", cycles
}
