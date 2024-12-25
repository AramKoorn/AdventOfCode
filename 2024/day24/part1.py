import re


w, gates = open("2024/day24/input.txt").read().split("\n\n")

wires = {}
for wire in w.splitlines():
    a, b = wire.split(":")
    wires[a] = int(b.strip())

pattern = re.compile(r"(\w+)\s+(\w+)\s+(\w+)\s*->\s*(\w+)")

for i in range(len(gates.splitlines())):
    for g in gates.splitlines():
        t = pattern.match(g)
        w1, op, w2, w3 = t.groups()
        try:
            match op:
                case "AND":
                    wires[w3] = wires[w1] & wires[w2]
                case "OR":
                    wires[w3] = wires[w1] | wires[w2]
                case "XOR":
                    wires[w3] = wires[w1] ^ wires[w2]
        except:
            print(f"iteration {i} not possible yet")

bits = []
for wire in sorted(wires):
    if wire[0] == "z":
        bits.append(wires[wire])
    print(f"{wire}: {wires[wire]}")

bits = bits[::-1]
binary_str = "".join(str(bit) for bit in bits)  
decimal = int(binary_str, 2)
print(decimal)



for i in range(45):
    number = f"{i:02d}" 
    if wires[f"x{number}"] ^ wires[f"y{number}"] != wires[f"z{number}"]:
        print(number)

print(wires["z01"])
    

