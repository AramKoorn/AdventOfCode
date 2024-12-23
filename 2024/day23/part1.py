from collections import defaultdict
from collections import deque
from itertools import combinations
from tqdm import tqdm


lines = open("2024/day23/input.txt").read().splitlines()

graph = defaultdict(list)

for l in lines:
    a, b = l.split("-")[0], l.split("-")[1]
    graph[a].append(b)
    graph[b].append(a)

nodes = list(graph)
all_combinations = combinations(nodes, 3)


trips = []
for c in tqdm(all_combinations):
    ok = True
    cnt_t = 0
    for node in c:
        if node[0] == 't':
            cnt_t += 1
        # check if all connected
        other_nodes = set(c) - set([node])
        if len(other_nodes & set(graph[node])) != len(other_nodes):
            ok = False
            break
    if ok and cnt_t > 0:
        trips.append(c) 

print(len(trips))