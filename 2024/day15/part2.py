f = open("2024/day15/input.txt").read()

grid, ins = f.split("\n\n")
grid = grid.splitlines()

# expand grid
new_grid = []
for r in grid:
    nr = ""
    for i, char in enumerate(r):
        match char:
            case '@':
                nr += "@."
            case "O":
                nr += "[]"
            case _: 
                nr += char * 2
    new_grid.append(nr)
    
grid = [[x for x in g] for g in new_grid]

for g in grid:
    print(g)

ins = "".join(ins.splitlines())

n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            robot = (i, j)

dirs = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


def move_horizontally(robot, dir):
    conn = [("@", robot)]
    x, y = robot

    while grid[x + dir[0]][y + dir[1]] == '[' or grid[x + dir[0]][y + dir[1]] == ']':
        x += dir[0]
        y += dir[1]
        conn.append((grid[x][y], (x, y)))

    # Shift values grid
    if grid[x + dir[0]][y + dir[1]] == ".":
        grid[robot[0]][robot[1]] = "."
        for char, (x, y) in conn:
            if char == "@":
                robot = (x, y + dir[1])
            grid[x][y + dir[1]] = char
    return robot
                

def move_vertically(robot, dir):

    conn = []

    q = [(grid[robot[0] + dir[0]][robot[1]], (robot[0] + dir[0], robot[1]))]
    while q:
        char, (x, y) = q.pop(0)
        conn.append((char, (x, y)))
        # find neighbour
        match char:
            case '[':
                if (']', (x, y + 1)) not in conn:
                    q.append((']', (x, y + 1)))
            case ']':
                if ('[', (x, y - 1)) not in conn:
                    q.append(('[', (x,  y - 1)))
        if grid[x + dir[0]][y] == "[" or grid[x + dir[0]][y] == "]" and (grid[x + dir[0]][y], (x + dir[0], y)) not in conn:
            q.append((grid[x + dir[0]][y], (x + dir[0], y)))
            
    # connection of all vertical blocks
    # check if we can move all the blocks vertically
    cords = [x[1] for x in conn]
    move = True
    for x, y in cords:
        if grid[x + dir[0]][y] != '.' and (x + dir[0], y) not in cords:
            move = False
            break

    # Update grid
    if move:
        new_moves = set()
        for char, (x, y) in conn:
            grid[x + dir[0]][y] = char
            new_moves.add((x + dir[0], y))
    # Update empty space and robot
    if move:
        grid[robot[0]][robot[1]] = '.'
        robot = (robot[0] + dir[0], robot[1])
        for x, y in (set(cords) -  new_moves):
            grid[x][y] = '.'
    grid[robot[0]][robot[1]] = "@"
    return robot

for move in ins:

    x, y = robot
    dir = dirs[move]
    # start with easy case
    if grid[x + dir[0]][y + dir[1]] == ".":
        grid[x][y] = '.'
        robot = (x + dir[0], y + dir[1])
        grid[robot[0]][robot[1]] = "@"
        continue

    if grid[x + dir[0]][y + dir[1]] == "#":
        continue
    
    # move horizontally
    if move == "<" or move == ">":
        robot = move_horizontally(robot, dir)
    # move vertically
    else:
        robot = move_vertically(robot, dir)
    

t = 0 
for i in range(n):
    for j in range(m):
        if grid[i][j] == '[':
            t += j
            t += i * 100
print(t)