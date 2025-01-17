f = open("2024/day04/input_test.txt", "r")
lines = f.readlines()
lines = [l.split("\n") for l in lines]

grid = []
for x in lines:
    grid.append([x for x in x[0]])

n = len(grid)
m = len(grid[0])

WORD = 'XMAS'
visited = set()
visited = []
offset = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-Right (Diagonal)
    (1, -1),  # Down-Left (Diagonal)
    (-1, 1),  # Up-Right (Diagonal)
    (-1, -1)  # Up-Left (Diagonal)
]
res = [0]
def bfs(path, pos):

    if pos == 3 and path not in visited:
        visited.append(path)
        res[0] += 1
        print("".join([grid[a][b] for a, b in path]))
        return 
    if pos == 3:
        return 
    
    find_letter = WORD[pos + 1]
    x, y = path[-1]

    for i, j in offset:
        dx = x + i 
        dy = y + j
        if 0 <= dx < n and 0 <= dy < m:
            if grid[dx][dy] == find_letter and (dx, dy) not in path:
                bfs(path + [(dx, dy)], pos + 1)


for i in range(n):
    for j in range(m):
        if grid[i][j] == "X":
            bfs(path=[(i, j)], pos=0)
print(res)

# Convert each list to a tuple and use a set to find unique lists
unique_lists = [list(t) for t in set(tuple(lst) for lst in visited)]
# Print the result
print(len(unique_lists))

