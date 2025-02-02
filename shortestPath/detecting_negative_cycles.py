def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relax edges (V - 1) times
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                return "Graph contains a negative-weight cycle"

    return distances

# Example graph with a negative cycle
graph = {
    'A': {'B': 2},
    'B': {'C': 3},
    'C': {'A': -6}  # Negative weight creates a negative cycle
}

# Detect negative cycles
start_node = 'A'
result = bellman_ford(graph, start_node)
print(result)