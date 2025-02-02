from collections import deque

def has_cycle_bfs(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            # Queue stores (current_node, parent_node)
            queue = deque([(node, None)])
            visited.add(node)

            while queue:
                current, parent = queue.popleft()

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current))
                    elif neighbor != parent:
                        # If the neighbor is visited and not the parent, a cycle exists
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
print("Graph has a cycle:", has_cycle_bfs(graph))