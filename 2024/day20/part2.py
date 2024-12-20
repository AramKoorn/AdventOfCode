from collections import deque
from collections import Counter
from tqdm import tqdm


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


def reachable_points(x, y, steps):
    return [(i, j) for i in range(x - steps, x + steps + 1)
            for j in range(y - (steps - abs(i - x)), y + (steps - abs(i - x)) + 1)]


STEPS = 20
# takes roughly 10 minutes
for s, r, c in tqdm(ordered):

    cords = reachable_points(r, c, STEPS)
    poss = [(s, r, c,) for s, r, c in ordered if (r, c) in cords]
    cheat = [point - (abs(r - dr) + abs(c - dc)) - s for point, dr, dc in poss]
    cheats.extend(cheat)

c = Counter(cheats)
t = 0
for k, v in c.items():
    if k >= 100:
        t += v

print(t)
