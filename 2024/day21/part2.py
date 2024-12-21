from itertools import permutations
from functools import lru_cache

lines = open('2024/day21/input.txt').read().splitlines()

num_keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['.', '0', 'A']]
dir_keypad = [['.', '^', 'A'], ['<', 'v', '>']]

grid_keypad = {} 
for i in range(len(num_keypad)):
    for j in range(len(num_keypad[0])):
        grid_keypad[num_keypad[i][j]] = (i, j)

grid_dirs = {}
for i in range(len(dir_keypad)):
    for j in range(len(dir_keypad[0])):
        grid_dirs[dir_keypad[i][j]] = (i, j)

        
offset = ((0, 1), (1, 0), (-1, 0), (0, -1))
directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
# directions = {v: k for k, v in directions.items()}
print(grid_keypad)


print(num_keypad)

"02"

def get_possible_routes(grid, a, b):
    """
    find all possible paths from a to b given the grid
    it's always faster to go up up left then up left up (this holds for all directions)
    """
    curr = grid[a]
    nxt = grid[b]

    di = nxt[0] - curr[0]
    dj = nxt[1] - curr[1]

    moves = []
    if di > 0:
        moves.append(["v"] * di)
    else:
        moves.append(["^"] * abs(di))
    if dj > 0:
        moves.append([">"] * abs(dj))
    else:
        moves.append(["<"] * abs(dj))
    
    # generate all possible permutations
    moves = [x for x in moves if x != []]
    moves = list(permutations(moves))

    # Check if not walking on empty spaces
    grid = {v: k for k, v in grid.items()}  # swap lookup
    valid_moves = []
    while moves:
        c = moves.pop()
        c_str = ''.join([item for sublist in list(c) for item in sublist])
        curr_r, curr_c = curr
        ok = True
        for d in c_str:
            dr, dc = directions[d]
            curr_r += dr
            curr_c += dc
            if grid[(curr_r, curr_c)]== '.':
                ok = False
                break
        if ok:
            valid_moves.append(c_str + "A")

    return valid_moves 


@lru_cache(maxsize=None)
def rec(a, b, depth):

    grid = grid_keypad if depth == ROBOTS else grid_dirs
    paths = get_possible_routes(grid, a, b)

    if depth == 0:
        return min([len(x) for x in get_possible_routes(grid, a, b)])


    min_cost = float("inf")
    for p in paths:
        route = "A" + p
        cost = 0
        # we can have something like Avvv
        for i in range(len(route) - 1):
            cost += rec(route[i], route[i + 1], depth - 1)
            # print(cost)
        min_cost = min(min_cost, cost)

    return min_cost


# cost = 0
# cost += rec("A", "0", 2)
# cost += rec("0", "2", 2)
# cost += rec("2", "9", 2)
# cost += rec("9", "A", 2)
# cost += rec("A", "7", 2)
# 029A
# print(cost)

t = 0
ROBOTS = 25
for l in lines:
    l = "A" + l
    num_code = int(l.replace("A", ""))

    cost = 0
    for i in range(len(l) - 1):
        cost += rec(l[i], l[i + 1], ROBOTS)
    t += cost * num_code
    

print(t)