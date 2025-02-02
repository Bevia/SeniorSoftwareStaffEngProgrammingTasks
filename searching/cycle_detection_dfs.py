def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node, parent):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor in recursion_stack and neighbor != parent:
                return True

        recursion_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# Example unweighted graph
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E'],
    'D': ['A', 'E'],
    'E': ['B', 'C', 'D']
}

# Check if the graph has a cycle
print("Graph has a cycle:", has_cycle(graph))