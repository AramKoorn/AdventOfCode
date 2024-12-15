from collections import defaultdict, deque

grid = defaultdict(list)
area = defaultdict(set)
edges = defaultdict(list)

f = open("input.txt").read().splitlines()
n = len(f)
m = len(f[0])

for i in range(n):
    for j in range(m):
        grid[i].append(f[i][j])


offset = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(q):
    visited = set()

    while q:
        i, j = q.popleft()
        curr = grid[i][j]
        area[curr].add((i, j))
        all_cords.add((i, j))
        for dx, dy in offset:
            x = i + dx
            y = j + dy
            if 0 <= x < n and 0 <= y < m:
                if grid[x][y] == curr and (x, y) not in visited:
                    q.append((x, y))
                    visited.add((x, y))

def perimeter(vals):
    t = 0
    for i, j in vals:
        for dx, dy in offset:
            if (i + dx, j + dy) not in vals:
                t += 1
    return t


all_cords = set()

t = 0
for i in range(n):
    for j in range(m):
        curr = grid[i][j]
        if curr not in area:
            q = deque([(i, j)])
            bfs(q)
            area_size = len(area[curr])
            perimeter_size = perimeter(area[curr])
            t += area_size * perimeter_size
            # print(curr, perimeter_size)
        else:
            if (i, j) not in all_cords:
                del area[curr]
                q = deque([(i, j)])
                bfs(q)
                area_size = len(area[curr])
                perimeter_size = perimeter(area[curr])
                t += area_size * perimeter_size


print(t)
