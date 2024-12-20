from collections import deque
from collections import Counter


grid = open("input.txt").read().splitlines()
n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            start = (i, j, 0)
        if grid[i][j] == 'E':
            end = (i, j)

q = deque([start])
seen = set()
offset = ((0, 1), (1, 0), (-1, 0), (0, -1))
steps = set()

def bfs(q):
    while q:
        r, c, step = q.popleft()
        seen.add((r, c))
        steps.add((r, c, step))

        for dr, dc in offset:
            nr = r + dr
            nc = c + dc
            if grid[nr][nc] != "#" and (nr, nc) not in seen:
                q.append((nr, nc, step + 1))
                seen.add((nr, nc))

bfs(q)
ordered = sorted([(s, r, c) for r, c, s in steps])
cheats = []

for s, r, c in ordered:
    for dr, dc in offset:
        nr = r + dr
        nc = c + dc
        if grid[nr][nc] == "#" and nr != 0 and nr != n - 1 and nc != 0 and nc != m - 1:
            min_cheat = 0
            for di, dj in offset:
                if (nr + di, nc + dj) != (nr, nc) and (nr + di, nc + dj) in seen:
                    nstep = [x for x, r, c, in ordered if r == nr + di and c == nc + dj][0]
                    min_cheat = max(min_cheat, nstep - s - 2)
            cheats.append(min_cheat)
    # cheats.append(min_cheat)

c = Counter(cheats)
t = 0
for k, v in c.items():
    if k >= 100:
        t += v

print(t)
