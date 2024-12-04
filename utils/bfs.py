from collections import deque

def bfs(graph, start):
    """
    Perform BFS on a graph starting from a given node.

    Parameters:
    graph (dict): Adjacency list representation of the graph.
    start: Starting node for BFS.

    Returns:
    list: List of nodes in the order they are visited.
    """
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add unvisited neighbors to the queue
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'C'
print(bfs(graph, start_node))
