import time
from collections import deque
def bfs(puzzle):
    start_time = time.time()
    frontier = deque([(puzzle.start_initial_state, [])])
    explore = set()
    nodes_expanded= 0

    while frontier:
        state, path = frontier.popleft()
        nodes_expanded += 1

        if state == puzzle.goal:
            runtime = time.time() - start_time
            return {
                "path_to_goal": path,
                "cost_of_path": len(path),
                "nodes_expanded": nodes_expanded,
                "search_depth": len(path),
                "running_time": runtime
            }

        explore.add(tuple(state))

        for neighbor, move in puzzle.neighbors(state):
            if tuple(neighbor) not in explore:
                frontier.append((neighbor, path + [move]))

    return None
