import heapq


#  Dijkstra’s algorithm is used to find the shortest path from a single source node
#  to all other nodes in a graph with non-negative edge weights.

def dijkstra(graph, start):
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    # Dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If a shorter path is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Example graph (adjacency list)
graph = {
    'A': {'B': 5, 'D': 2},
    'B': {'A': 5, 'C': 3, 'E': 4},
    'C': {'B': 3, 'F': 1},
    'D': {'A': 2, 'E': 6},
    'E': {'B': 4, 'D': 6, 'F': 2},
    'F': {'C': 1, 'E': 2}
}

# Find shortest paths from node 'A'
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")
