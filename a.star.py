
def a_star(graph, start, goal, heuristic):
    open_list = [(start, 0)]  # Open list: (Nodes, f values)
    closed_list = set()  # a closed list
    g_score = {start: 0}  # Start Node Cost
    came_from = {}  # Path Tracking

    while open_list:
        current, _ = min(open_list, key=lambda x: x[1])  # Select the node with the smallest f value
        if current == goal:
            return reconstruct_path(came_from, current)  # Return Shortest Path

        open_list = [(node, f) for node, f in open_list if node != current]
        closed_list.add(current)

        for neighbor in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g = g_score[current] + graph[current][neighbor]
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                open_list.append((neighbor, f_score))
                came_from[neighbor] = current

    return None  # If there is no path

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def heuristic(node, goal):
    # Example: Manhattan Street
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def main():
    # Graph Definition (Node: {Neighbor Node: Distance})
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
        print("shortest path:", path)
    else:
        print("Path not found.")

if __name__ == "__main__":
    main()

    