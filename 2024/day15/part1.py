f = open("2024/day15/input.txt").read()

grid, ins = f.split("\n\n")
grid = grid.splitlines()
grid = [[x for x in g] for g in grid]

ins = "".join(ins.splitlines())

n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            robot = (i, j)

dirs = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
custom_order = {'O': 1, '@': 2, '.': 3}


def custom_sort_key(char):
    return custom_order.get(char, 100)  


def get_connected(robot, dir):
    x, y = robot
    conn = [("@", robot)]
    d = dirs[dir]
    if grid[x + d[0]][y + d[1]] == '.':
        return conn + [(".", (x + d[0], y + d[1]))] 
    else:
        while grid[x + d[0]][y + d[1]] == 'O':
            x += d[0]
            y += d[1]
            conn.append(('O', (x, y)))
    # check if we reached empty spot
    if grid[x + d[0]][y + d[1]] == '.':
        conn.append(('.', (x + d[0], y + d[1])))
    return conn


def get_blocks(robot, dir):

    x, y = robot
    pos = []
    d = dirs[dir]
    while grid[x][y] != "#":
        pos.append((grid[x][y], (x, y)))
        x += d[0]
        y += d[1]
    return pos


def slide_blocks(blocks):
    s = sorted([x[0] for x in blocks], key=custom_sort_key)
    return list(zip(s, [x[1] for x in blocks][::-1]))


for move in ins:
    blocks = get_connected(robot, move)
    new_pos = slide_blocks(blocks)

    for char, (r, c) in new_pos:
        grid[r][c] = char
        if char == "@":
            robot = (r, c)
    print(move)
    # for g in grid:
    #     print(g)
    debug = True


t = 0 
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'O':
            t += j
            t += i * 100
print(t)