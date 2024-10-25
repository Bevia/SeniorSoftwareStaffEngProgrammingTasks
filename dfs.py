# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# Depth-First Search function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Track visited nodes to avoid revisits
    visited.add(start)  # Visit the current node
    print(start, end=" ")  # Print the visited node

    # Recur for all neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# Starting DFS from node 'A'
dfs(graph, 'A')