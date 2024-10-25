from collections import deque


# BFS function
def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Queue to manage the BFS process

    while queue:
        # Dequeue a vertex from the queue
        node = queue.popleft()

        # If the node hasn't been visited yet
        if node not in visited:
            print(node, end=" ")  # Process the node (e.g., print it)
            visited.add(node)  # Mark it as visited

            # Enqueue all adjacent nodes
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run BFS
bfs(graph, 'A')
