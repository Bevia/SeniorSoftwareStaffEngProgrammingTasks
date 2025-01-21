from collections import deque


def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS
    bfs_order = []  # List to keep track of the BFS traversal order

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
print(bfs(graph, start_node))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
