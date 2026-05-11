Problem 9 - Node Path Existence
You are given a directed graph represented by its nodes and edges. Each node is identified by a unique label. The nodes in graph may contain cycles or may not be connected. Write a function that takes the graph, start node, and end node as inputs and returns two pieces of information:

1. A boolean value indicating whether a connected path exists between the specified nodes.
2. The connected path itself, if it exists.

Solution:
Use BFS (Breadth-First Search):
  finds shortest path in unweighted graph
  queue for traversal
  parent dictionary to reconstruct path
  visited set to avoid cycles

Code

from collections import deque

def bfs_shortest_path(graph, start, end):

    # Queue for BFS: stores nodes to explore
    queue = deque([start])

    # Track visited nodes (avoid cycles)
    visited = set([start])

    # Parent map to reconstruct path
    parent = {start: None}

    # BFS traversal
    while queue:

        current = queue.popleft()

        # If we reached destination → stop
        if current == end:
            break

        # Explore neighbors
        for neighbor in graph.get(current, []):

            if neighbor not in visited:

                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # If end not reached
    if end not in parent:
        return False, []

    # Reconstruct path from end → start
    path = []
    node = end

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    return True, path


# Graph Definition by using adjacency list
graph = {
    "A": ["B"],
    "B": ["A", "C", "D", "E"],
    "C": ["F"],
    "D": ["G", "E"],
    "E": ["F"],
    "F": ["B", "G"],
    "G": [],
    "H": []
}

# TEST/Show result
exists, path = bfs_shortest_path(graph, "F", "A")

print("Path exists:", exists)
print("Path:", path)
