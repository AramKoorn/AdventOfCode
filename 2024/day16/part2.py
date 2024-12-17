import heapq
from collections import defaultdict


grid = open("2024/day16/input.txt").read().splitlines()

n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            start = (i, j)


def rotate_direction(direction, clockwise=True):
    complex_dir = complex(direction[0], direction[1])
    multiplier = -1j if clockwise else 1j
    rotated = complex_dir * multiplier
    return int(rotated.real), int(rotated.imag)

q = [(0, start[0], start[1], 0, 1)]
visited = {}
min_cost = {}
memory = defaultdict(set)
end_points = set()
opt_score = float("inf")


while q:
    cost, r, c, dr, dc = heapq.heappop(q)
    
    if min_cost.get((r, c, dr, dc), float("inf")) < cost:
        continue
    
    visited[(r, c, dr, dc)] = cost


    if grid[r][c] == "E":
        if opt_score < cost:
            break
        opt_score = cost
        end_points.add((r, c, dr, dc))
        print(cost)
    
    rot1 = rotate_direction((dr, dc), clockwise=True)
    rot2 = rotate_direction((dr, dc), clockwise=False)
    poss = [(cost + 1, r + dr, c + dc, (dr, dc)),
    (cost + 1000, r, c , rot1),
    (cost + 1000, r, c , rot2)]
    for cst, nr, nc, dir in poss:
        if grid[nr][nc] != "#":
            low = min_cost.get((nr, nc, dir[0], dir[1]), float('inf'))
            if cst > low:
                continue
            if cst < low:
                min_cost[(nr, nc, dir[0], dir[1])] = cst
                # if visited.get((nr, nc, dir[0], dir[1]), float('inf')) >= cst:
            heapq.heappush(q, (cst, nr, nc, dir[0], dir[1]))
            memory[(nr, nc, dir[0], dir[1])].add((r, c, dr, dc))
 
# backtrack 
stack = list(end_points)
sit = set()

while stack:
    cords = stack.pop(0)
    for c in memory[cords]:
        if c not in sit:
            stack.append(c)
        sit.add(cords)


res = {(r, c) for r, c, dr, dc in sit}

print(len(res))