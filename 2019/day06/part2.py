from collections import defaultdict, deque


f = open("2019/day06/input.txt").read().splitlines()

all_nodes = set()

graph = defaultdict(list)
for l in f:
    n1, n2 = l.split(")")
    graph[n1].append(n2)
    graph[n2].append(n1)
    all_nodes.add(n1)
    all_nodes.add(n2)

q = deque([("YOU", 0)])
seen = set()

while q:
    node, step = q.popleft()
    seen.add(node)

    if node == "SAN":
        print(step - 2)
        break

    for n in graph[node]:
        if n not in seen:
            q.append((n, step + 1))
            seen.add(node)
