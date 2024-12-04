f = open("2024/day04/input.txt", "r")
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
    (1, 1),   # Down-Right (Diagonal)
    (1, -1),  # Down-Left (Diagonal)
    (-1, 1),  # Up-Right (Diagonal)
    (-1, -1)  # Up-Left (Diagonal)
]

res = 0
cnt = 0
for i in range(n):
    for j in range(m):
        cnt = 0
        if grid[i][j] == "A":
            for dx, dy in offset:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m:
                    if grid[x][y] == 'M' or grid[x][y] == 'S':
                        opp_x = i + dx * -1
                        opp_y = j + dy * -1
                        if 0 <= opp_x < n and 0 <= opp_y < m:
                            match grid[x][y]:
                                case "M":
                                    inv = "S"
                                case "S":
                                    inv = "M"
                            
                            if grid[opp_x][opp_y] == inv:
                                cnt += 1
        if cnt == 4:
            res += 1
                            
print(res)
