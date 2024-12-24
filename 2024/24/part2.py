import sys

correct_circuit = ""
correct_circuit += "x00 AND y00 -> carry00\n"
correct_circuit += "x00 XOR y00 -> z00\n"
for i in range(1, 44):
    z = f"z{i-1:02}"
    x, y = f"x{i:02}", f"y{i:02}"
    prev_carry = f"carry{i-1:02}"
    carry = f"carry{i:02}"
    aand = f"and{i:02}"
    xor = f"xor{i:02}"
    cand = f"cand{i:02}"

    correct_circuit += f"{x} AND {y} -> {aand}\n"
    correct_circuit += f"{x} XOR {y} -> {xor}\n"
    correct_circuit += f"{xor} XOR {prev_carry} -> {z}\n"
    correct_circuit += f"{xor} AND {prev_carry} -> {cand}\n"
    correct_circuit += f"{cand} OR {aand} -> {carry}\n"


def parse(string):
    graph = {}
    for line in string.split("\n"):
        a, op, b, _, dest = line.split()
        if a > b:
            a, b = b, a
        graph[f"{a} {op} {b}"] = dest
    return graph


correct = parse(correct_circuit.strip())
given = parse(sys.stdin.read().strip().split("\n\n")[1])

swaps = {
    "z05": "tst",
    "tst": "z05",
    "sps": "z11",
    "z11": "sps",
    "z23": "frt",
    "frt": "z23",
    "pmd": "cgh",
    "cgh": "pmd",
}

for k, v in given.items():
    if v in swaps:
        given[k] = swaps[v]

print(",".join(sorted(swaps.keys())))

mapping = {}
for i in range(44):
    x, y, z = f"x{i:02}", f"y{i:02}", f"z{i:02}"
    mapping[x] = x
    mapping[y] = y
    mapping[z] = z
last = f"z{44:02}"
mapping[last] = last

for gate, dest in correct.items():
    a, op, b = gate.split()
    if mapping[a] > mapping[b]:
        a, b = b, a

    search = f"{mapping[a]} {op} {mapping[b]}"
    if search not in given:
        print(f"Missing: {search} ({a} {op} {b})")
        break
    mapping[dest] = given[search]
