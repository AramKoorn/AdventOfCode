import re
import graphviz


w, gates = open("2024/day24/input.txt").read().split("\n\n")

wires = {}
for wire in w.splitlines():
    a, b = wire.split(":")
    wires[a] = int(b.strip())

pattern = re.compile(r"(\w+)\s+(\w+)\s+(\w+)\s*->\s*(\w+)")

# manual add swaps after inspecting graph
swaps = {"z12": "djg",
        "djg": "z12", 
        "z19": "sbg", 
        "sbg": "z19",
       "hjm": "mcq", "mcq": "hjm",
       "z37": "dsd", "dsd": "z37" 
        }

for i in range(len(gates.splitlines())):
    for g in gates.splitlines():
        t = pattern.match(g)
        w1, op, w2, w3 = t.groups()
        if w3 in swaps:
            w3 = swaps[w3]
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


# check if circuit is working properly when fail
# investigate graph to see which nodes we need to swap

carry = 0
for i in range(45):  
    number = f"{i:02d}" 
    s = wires[f"x{number}"] + wires[f"y{number}"] + carry
    if wires[f"z{number}"] != s % 2:
        print(number)
        break 
    carry = s // 2

    
print(",".join(sorted(list(swaps))))