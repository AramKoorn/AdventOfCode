from collections import deque


f = open("input.txt").read().splitlines()
SIZE = 71
STEPS = 1024
grid = [["." for x in range(SIZE)] for _ in range(SIZE)]


cnt = 0
for i, l in enumerate(f):
    c, r = list(map(int, l.split(",")))
    if i < STEPS:
        cnt += 1
        # print(r, c)
        grid[r][c] = "#"

assert cnt == STEPS
# for g in grid:
#     print(g)

start = (0, 0, 0)
end = (SIZE - 1, SIZE - 1)
q = deque([start])
offset = ((0, 1), (1, 0), (-1, 0), (0, -1))
seen = set()

while q:
    r, c, steps = q.popleft()
    seen.add((r, c))

    if (r, c) == end:
        print(steps)
        break

    for dr, dc in offset:
        i = r + dr
        j = c + dc
        if 0 <= i < SIZE and 0 <= j < SIZE:
            if grid[i][j] != "#" and (i, j) not in seen:
                q.append((i, j, steps + 1))
                seen.add((i, j))
