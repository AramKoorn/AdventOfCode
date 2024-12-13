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


def get_sides(region):
    up_sides = 0
    down_sides = 0
    left_sides = 0
    right_sides = 0
    for (x, y) in region:
        left = x - 1
        right = x + 1
        above = y - 1
        below = y + 1
        right_not_in_region = (right, y) not in region
        below_not_region = (x, below) not in region

        if (x, above) not in region:
            if right_not_in_region or (right, above) in region:
                up_sides += 1

        if (x, below) not in region:
            if right_not_in_region or (right, below) in region:
                down_sides += 1

        if (left, y) not in region:
            if below_not_region or (left, below) in region:
                left_sides += 1

        if (right, y) not in region:
            if below_not_region or (right, below) in region:
                right_sides += 1

    return up_sides + down_sides + left_sides + right_sides


all_cords = set()
t = 0
for i in range(n):
    for j in range(m):
        curr = grid[i][j]
        if curr not in area:
            q = deque([(i, j)])
            bfs(q)
            area_size = len(area[curr])
            corners = get_sides(area[curr])
            t += area_size * corners
            # print(curr, perimeter_size)
        else:
            if (i, j) not in all_cords:
                del area[curr]
                q = deque([(i, j)])
                bfs(q)
                area_size = len(area[curr])
                corners = get_sides(area[curr])
                print(curr, corners)
                t += area_size * corners

print(t)