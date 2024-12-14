from collections import defaultdict
from copy import deepcopy


f = open("input.txt").read()
stones = list(map(int, f.split(" ")))

c = defaultdict(int)
for s in stones:
    c[s] += 1

STEPS = 75
for _ in range(STEPS):
    tmp = defaultdict(int)
    for k, v in c.items():
        if k == 0:
            tmp[1] += v
        elif len(str(k)) % 2 == 0:
            length = len(str(k))
            str_number = str(k)
            mid = length // 2
            l = int(str_number[:mid])
            r = int(str_number[mid:])
            tmp[l] += v
            tmp[r] += v
        else:
            tmp[k * 2024] = v
    c = deepcopy(tmp)

print(sum(tmp.values()))
