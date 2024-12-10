grid = open("input.txt").read().splitlines()
grid = [[int(x) for x in g] for g in grid]

n = len(grid)
m = len(grid[0])

offset = ((1, 0), (0, 1), (-1, 0), (0, -1))


def rec(i, j, t):
    curr = grid[i][j]
    if curr == 9:
        t += 1

    for dx, dy in offset:
        x = i + dx
        y = j + dy
        if 0 <= x < n and 0 <= y < m and (x, y):
            if grid[x][y] == curr + 1:
                t = rec(x, y, t)  # Update t with the returned value

    return t

t = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            t += rec(i, j, 0)

print(t)

