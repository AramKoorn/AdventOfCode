from collections import defaultdict

dirs = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}
wires = [x.split(',') for x in open("2019/day03/input.txt").read().split('\n')]

wires1 = defaultdict(list)
wires2 = defaultdict(list)

for i, wire in enumerate(wires):
    s = 0
    curr = (0, 0)
    for x in wire:
        d, steps = x[0], int(x[1:])
        delta = dirs[d]
        for _ in range(steps):
            s += 1
            curr = (curr[0] + delta[0], curr[1] + delta[1])
            if i == 0:
                if len(wires1[curr]) == 1:
                    continue
                wires1[curr].append(s)
            else:
                if len(wires2[curr]) == 1:
                    continue
                wires2[curr].append(s)


smallest = float("inf")
for k, v in wires1.items():
    if k in wires2:
        smallest = min(smallest, sum(v) + sum(wires2[k]))

print(smallest)