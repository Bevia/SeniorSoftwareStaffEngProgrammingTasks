from collections import deque


def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS
    bfs_order = []  # List to keep track of the BFS traversal order

    while queue:
        node = queue.popleft()
        #  The line `node = queue.popleft()` in the BFS algorithm is crucial for managing
        #  the traversal process efficiently. Here's a detailed explanation:
        #
        # ### Purpose of `queue.popleft()`
        #
        # 1. **Queue Management**: The `queue` in BFS is used to keep track of nodes that need
        # to be explored. It follows the FIFO (First In, First Out) principle.
        # 2. **Dequeuing Nodes**: `queue.popleft()` removes and returns the leftmost element
        # from the deque (double-ended queue). This ensures that nodes are processed in
        # the order they were added, maintaining the level-by-level exploration characteristic of BFS.
        #
        # ### Why `popleft` and Not `pop`?
        #
        # - **Efficiency**: Using `popleft()` on a deque is an O(1) operation, meaning
        # it's done in constant time. This is efficient and fast.
        # - **Correct Order**: By using `popleft()`, we ensure that nodes are explored in the exact
        # order they were added to the queue, adhering to the BFS principle.
        #
        # ### Example Workflow
        #
        # Consider a simplified scenario where you start BFS from node **A**:
        #
        # 1. **Initial State**:
        #    - Queue: [A]
        #    - Visited: []
        #
        # 2. **Dequeue A (queue.popleft())**:
        #    - Process A.
        #    - Enqueue neighbors B, C.
        #    - Queue: [B, C]
        #    - Visited: [A]
        #
        # 3. **Dequeue B (queue.popleft())**:
        #    - Process B.
        #    - Enqueue neighbors D, E (A is already visited).
        #    - Queue: [C, D, E]
        #    - Visited: [A, B]
        #
        # 4. **Dequeue C (queue.popleft())**:
        #    - Process C.
        #    - Enqueue neighbor F (A is already visited).
        #    - Queue: [D, E, F]
        #    - Visited: [A, B, C]
        #
        # This process continues until the queue is empty, ensuring all nodes are visited in BFS order.
        #
        # In summary, `node = queue.popleft()` is used to efficiently remove the first element
        # from the queue and process it, maintaining the correct BFS traversal order.

        if node not in visited:
            visited.add(node)
            bfs_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order


# Example usage
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
print(bfs(graph, start_node))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
