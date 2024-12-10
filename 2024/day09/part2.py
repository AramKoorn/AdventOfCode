import os
from collections import defaultdict
import heapq

print(os.getcwd())
f = open("input.txt").read()
disk = []
fid = 0
pos = 0

spaces = defaultdict(list)
files = []

for i, char in enumerate(f):
    x = int(char)
    if i % 2 == 0:
        disk += [fid] * x
        # Position, gap, ID
        files.append((pos, x, fid))
        fid += 1
    else:
        disk += [-1] * x
        heapq.heappush(spaces[x], pos)
    pos += x


for pos, gap, fid in files[::-1]:
    possible_gaps = sorted([[spaces[gap_len][0], gap_len] for gap_len in spaces if gap_len >= gap])
    if len(possible_gaps) > 0:
        p_gap, gap_level = possible_gaps[0]
        if p_gap < pos:
            heapq.heappop(spaces[gap_level])
            if not spaces[gap_level]:
                del spaces[gap_level]

            # update disk
            for i in range(pos, pos + gap):
                disk[i] = -1

            # Update spaces
            for i in range(p_gap, p_gap + gap):
                disk[i] = fid

            if gap_level - gap > 0:
                heapq.heappush(spaces[gap_level - gap], p_gap + gap)

# print("".join([str(x) for x in disk]))
print(sum(i * x for i, x in enumerate(disk) if x != -1))