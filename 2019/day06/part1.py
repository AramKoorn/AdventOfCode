from collections import defaultdict


f = open("2019/day06/input.txt").read().splitlines()
print(f)

all_nodes = set()

graph = defaultdict(list)
for l in f:
    n1, n2 = l.split(")")
    graph[n1].append(n2)
    all_nodes.add(n1)
    all_nodes.add(n2)

def get_ancestors(graph, target, visited=None):
    if visited is None:
        visited = set()

    for parent, children in graph.items():
        if target in children:
            if parent not in visited:
                visited.add(parent)
                get_ancestors(graph, parent, visited)
    return visited

t = 0
for node in all_nodes:
    ancestors = get_ancestors(graph, node)
    # print(f"{node}: {ancestors}")
    t += len(ancestors)

print(t)
