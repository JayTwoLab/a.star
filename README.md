### `A* (A star)` Algorithm: An Efficient Shortest Path Search Algorithm

- The `A* (A star)` algorithm is a graph search and pathfinding algorithm known for its efficiency in finding the shortest path.
- It is commonly used in navigation systems, game AI, and robot path planning.
- A* is similar to Dijkstra's algorithm but uses **heuristics** to make the search more efficient.

---

### Key Components of the `A*` Algorithm

1. **Node Cost (`g(n)`)**
   - The actual cost of moving from the start node to the current node.

2. **Heuristic (`h(n)`)**
   - The estimated cost from the current node to the goal node (e.g., Euclidean or Manhattan distance).

3. **Evaluation Function (`f(n)`)**
   - \( f(n) = g(n) + h(n) \)
   - Determines the priority for exploration based on the total estimated cost.

---

### How It Works

1. **Initialization**
   - Add the start node to the `open list`.
   - Keep the `closed list` empty.

2. **Iterative Process**
   - Select the node with the lowest \( f(n) \) value from the open list.
   - If the selected node is the goal node, terminate the search.
   - Move the selected node to the closed list.
   - For each neighbor of the selected node:
     - Skip if it's already in the closed list.
     - If it's not in the open list, add it and calculate its \( g(n), h(n), \) and \( f(n) \).
     - If it is in the open list and the new \( g(n) \) is smaller, update its values.

3. **Termination**
   - If the goal node is reached, return the path.
   - If the open list is empty but the goal is not reached, there is no path.

---

### Pseudo Code
```python
def main():
    # Define graph (node: {neighbor: distance})
    graph = {
        (0, 0): {(0, 1): 1, (1, 0): 1},
        (0, 1): {(0, 0): 1, (1, 1): 1},
        (1, 0): {(0, 0): 1, (1, 1): 1},
        (1, 1): {(0, 1): 1, (1, 0): 1, (2, 2): 2},
        (2, 2): {(1, 1): 2}
    }

    start = (0, 0)
    goal = (2, 2)

    path = a_star(graph, start, goal, heuristic)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
```

<p align="center"> <img width="70%" src="https://gist.githubusercontent.com/j2doll/36975662784b338d0b36ab12ea29fc5e/raw/dd99d47e5d9067eec4cb7129b5512d43461180cc/output%2520(1).png" /> </p>

A* returns the optimal path but provides only **one shortest path**, even when multiple optimal paths exist with the same heuristic and cost conditions.

#### 1. Current Path (Returned by A*)
- `(0, 0) → (0, 1) → (1, 1) → (2, 2)`
- Cost Calculation:
  - `(0, 0) → (0, 1)`: Cost 1
  - `(0, 1) → (1, 1)`: Cost 1
  - `(1, 1) → (2, 2)`: Cost 2
  - **Total Cost = 1 + 1 + 2 = 4**

#### 2. Alternative Path (Including Another Node)
- `(0, 0) → (1, 0) → (1, 1) → (2, 2)`
- Cost Calculation:
  - `(0, 0) → (1, 0)`: Cost 1
  - `(1, 0) → (1, 1)`: Cost 1
  - `(1, 1) → (2, 2)`: Cost 2
  - **Total Cost = 1 + 1 + 2 = 4**

#### Analysis
Both paths have the same total cost. Thus, the alternative path `(0, 0) → (1, 0) → (1, 1) → (2, 2)` is also a valid shortest path.

#### Characteristics of `A*`
- Since `A*` returns **only one shortest path**, other shortest paths may not be explored unless the algorithm is modified.
- To find all shortest paths, other approaches like BFS might be more appropriate.

---

### Advantages of the `A*` Algorithm
1. **Optimality**: Guarantees the shortest path if \( h(n) \) is **admissible** and **consistent**.
2. **Efficiency**: Reduces unnecessary path exploration, making it faster.

### Applications
1. **Game Development**: Moving units around obstacles to reach a target.
2. **Robotics**: Robot path planning.
3. **Navigation Systems**: Vehicle route finding.
