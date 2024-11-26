//> using scala 3.5.2

@main
def hello(): Unit =
    val data = scala.io.Source.stdin.getLines().next()

    var pos = 0
    var lvl = 0
    var first_negative_pos = -1

    while(pos < data.length) {
        if (data(pos) == '(') {
            lvl += 1
        } else {
            lvl -= 1
            if (lvl == -1 && first_negative_pos == -1) {
                first_negative_pos = pos + 1
            }
        }
        pos += 1
    }
    
    println(f"Part 1: $lvl")
    println(f"Part 2: $first_negative_pos")
