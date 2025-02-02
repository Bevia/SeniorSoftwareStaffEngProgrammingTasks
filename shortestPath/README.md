**Dijkstra’s algorithm** and the **Bellman-Ford algorithm** for finding the shortest path in a weighted graph.

## **1. Dijkstra’s Algorithm**
Dijkstra’s algorithm is used to find the shortest path from a 
single source node to all other nodes in a graph with **non-negative edge weights**.


## **2. Bellman-Ford Algorithm**
The Bellman-Ford algorithm is used to find the shortest path from a 
single source node to all other nodes in a graph, even if the graph 
contains **negative edge weights** (but no negative cycles).

A negative cycle is a cycle in a graph where the sum of the edge weights is negative. In other words, 
if you traverse the cycle, the total cost or distance decreases. This is problematic for shortest-path algorithms 
because it allows for infinitely decreasing paths, making it impossible to determine a true "shortest path."

Key Takeaways:
A negative cycle is a cycle where the sum of edge weights is negative.
Negative cycles make it impossible to determine a finite shortest path because
you can keep reducing the total cost by traversing the cycle.

The Bellman-Ford algorithm can detect negative cycles but cannot provide 
valid shortest paths if they exist.

Negative cycles are often encountered in applications like financial arbitrage, 
where they represent opportunities for infinite profit (in theory).

## **Key Differences Between Dijkstra and Bellman-Ford**:
| **Feature**            | **Dijkstra’s Algorithm**                          | **Bellman-Ford Algorithm**                 |
|-------------------------|---------------------------------------------------|-------------------------------------------|
| **Edge Weights**        | Non-negative only.                                | Can handle negative weights.              |
| **Negative Cycles**     | Cannot detect negative cycles.                    | Can detect negative cycles.               |
| **Time Complexity**     | O((V + E) log V) with a priority queue.           | O(V * E), slower than Dijkstra.           |
| **Use Case**            | Efficient for graphs with non-negative weights.   | Useful for graphs with negative weights.    

---

### **Example Graph**:
Both algorithms are applied to the following graph:
```
A --5-- B --3-- C
|       |       |
2       4       1
|       |       |
D --6-- E --2-- F
```

- **Dijkstra’s Output**: Shortest paths from `A` are `{'A': 0, 'B': 5, 'C': 8, 'D': 2, 'E': 7, 'F': 9}`.
- **Bellman-Ford Output**: Same as Dijkstra’s for this graph (no negative weights).

---

### **When to Use Which?**
- Use **Dijkstra’s algorithm** for graphs with **non-negative weights** (faster and more efficient).
- Use **Bellman-Ford algorithm** for graphs with **negative weights** or when you need to detect negative cycles.

Let me know if you have further questions! 😊