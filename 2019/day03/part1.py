from collections import defaultdict

dirs = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}
wires = [x.split(',') for x in open("2019/day03/input.txt").read().split('\n')]
cords = defaultdict(int)

smallest = float('inf')
for wire in wires:
    curr = (0, 0)
    for x in wire:
        d, steps = x[0], int(x[1:])
        delta = dirs[d]
        for _ in range(steps):
            curr = (curr[0] + delta[0], curr[1] + delta[1])
            cords[curr] += 1
            if cords[curr] > 1:
                dist = abs(curr[0]) + abs(curr[1])
                smallest = min(smallest, dist)

print(smallest)