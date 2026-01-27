import time

def dfs(puzzle, max_depth=50):

    start_state = tuple(puzzle.start_initial_state)
    goal_state = tuple(puzzle.goal)

    frontier = [(start_state, [], 0)]
    explored = set()
    nodes_expanded = 0
    start_time = time.time()

    while frontier:
        current_state, path, depth = frontier.pop()  # LIFO stack

        # التحقق من الهدف
        if current_state == goal_state:
            end_time = time.time()
            return {
                "path_to_goal": path,
                "cost_of_path": len(path),
                "nodes_expanded": nodes_expanded,
                "search_depth": depth,
                "running_time": end_time - start_time
            }

        if current_state in explored:
            continue

        explored.add(current_state)
        nodes_expanded += 1

        # الحصول على الجيران
        neighbors = puzzle.neighbors(list(current_state))
        neighbors.reverse()

        for neighbor, move in neighbors:
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple not in explored and depth + 1 <= max_depth:
                frontier.append((neighbor_tuple, path + [move], depth + 1))

    end_time = time.time()
    return {
        "path_to_goal": None,
        "cost_of_path": 0,
        "nodes_expanded": nodes_expanded,
        "search_depth": 0,
        "running_time": end_time - start_time
    }
