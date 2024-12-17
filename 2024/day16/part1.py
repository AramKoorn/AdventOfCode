import heapq


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

curr_dir = (0, 1)
q = [(0, start[0], start[1], curr_dir)]
visited = set()

while q:
    cost, r, c, (dr, dc) = heapq.heappop(q)
    visited.add((r, c, dr, dc))
    
    if grid[r][c] == "E":
        print(cost)
        break
    
    rot1 = rotate_direction((dr, dc), clockwise=True)
    rot2 = rotate_direction((dr, dc), clockwise=False)
    poss = [(cost + 1, r + dr, c + dc, (dr, dc)),
    (cost + 1000, r, c , rot1),
    (cost + 1000, r, c , rot2)]
    for cst, nr, nc, dir in poss:
        if grid[nr][nc] != "#" and (nr, nc, dir[0], dir[1]) not in visited:
            heapq.heappush(q, (cst, nr, nc, dir))
