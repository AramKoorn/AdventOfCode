from collections import defaultdict


lines = open("2024/day23/input.txt").read().splitlines()

graph = defaultdict(list)
for l in lines:
    a, b = l.split("-")[0], l.split("-")[1]
    graph[a].append(b)
    graph[b].append(a)

components = set()

def dfs(node, comp):

    if comp in components:
        return
    components.add(comp)

    for n in graph[node]:
        if n in comp:
            continue
        if all([n in graph[x] for x in comp]):
            dfs(n, comp | frozenset([n]))
        
for node in list(graph):
    dfs(node, frozenset([node]))


mx = 0
for c in components:
    mx = max(len(c), mx)

print(",".join(sorted(max(components, key=len))))