import time
import math
from heapq import heappush, heappop

def manhattan_distance(state, goal):

    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = goal.index(tile)
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_index, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def euclidean_distance(state, goal):

    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = goal.index(tile)
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_index, 3)
        distance += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


def a_star(puzzle, heuristic="manhattan"):

    start_time = time.time()

    start = puzzle.start_initial_state
    goal = puzzle.goal

    heuristic_func = manhattan_distance if heuristic == "manhattan" else euclidean_distance

    frontier = []
    heappush(frontier, (heuristic_func(start, goal), start, []))
    explored = set()
    nodes_expanded = 0

    while frontier:
        f_cost, state, path = heappop(frontier)
        nodes_expanded += 1

        if state == goal:
            end_time = time.time()
            return {
                "path_to_goal": path,
                "cost_of_path": len(path),
                "nodes_expanded": nodes_expanded,
                "search_depth": len(path),
                "running_time": end_time - start_time
            }

        explored.add(tuple(state))

        for neighbor, move in puzzle.neighbors(list(state)):
            if tuple(neighbor) not in explored:
                g = len(path) + 1
                h = heuristic_func(neighbor, goal)
                f = g + h
                heappush(frontier, (f, neighbor, path + [move]))

    end_time = time.time()
    return {
        "path_to_goal": None,
        "cost_of_path": 0,
        "nodes_expanded": nodes_expanded,
        "search_depth": 0,
        "running_time": end_time - start_time
    }
