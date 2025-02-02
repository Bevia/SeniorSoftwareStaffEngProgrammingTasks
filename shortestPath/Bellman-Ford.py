#  The Bellman-Ford algorithm is used to find the shortest path from a single source node to all other nodes in a graph,
#  even if the graph contains negative edge weights (but no negative cycles).

def bellman_ford(graph, start):
    # Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances

# Example graph (adjacency list)
graph = {
    'A': {'B': 5, 'D': 2},
    'B': {'C': 3, 'E': 4},
    'C': {'F': 1},
    'D': {'E': 6},
    'E': {'F': 2},
    'F': {}
}

# Find shortest paths from node 'A'
start_node = 'A'
shortest_paths = bellman_ford(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")