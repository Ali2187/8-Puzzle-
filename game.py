from EightPuzzle import EightPuzzle
from astar_algorithm import a_star
from dfs_algorithm import dfs
from bfs_algorithm import bfs

def show_path(puzzle, path):
    state = puzzle.start_initial_state.copy()
    print(" Initial State:")
    puzzle.display(state)

    for i, move in enumerate(path.get("path_to_goal", []), start=1):
        for neighbor, m in puzzle.neighbors(state):
            if m == move:
                state = neighbor
                break
        print(f"➡️ Step {i}: Move {move}")
        puzzle.display(state)


    print("\n--- Solution Summary ---")
    print(f"Path to Goal: {' → '.join(path.get('path_to_goal', []))}")
    print(f"Cost of Path: {path.get('cost_of_path', 'N/A')}")
    print(f"Nodes Expanded: {path.get('nodes_expanded', 'N/A')}")
    print(f"Search Depth: {path.get('search_depth', 'N/A')}")
    print(f"Running Time: {path.get('running_time', 0):.6f} seconds")






start_state = [1,2,5,
               3,4,0,
               6,7,8]
puzzle = EightPuzzle(start_initial_state=start_state)

bfs_result = bfs(puzzle)
dfs_result = dfs(puzzle)
astar_result1 = a_star(puzzle, heuristic="manhattan")
astar_result2=a_star(puzzle, heuristic="euclidean")
print("""
**** welcome to 8puzzle****
press 1 to display BFS.
press 2 to display DFS.
press 3 to display A* with heuristic manhattan.
press 4 to display A* with heuristic euclidean.
""")
x=int(input("Enter from 1 to 4: "))
if x==1:
    print("BFS")
    show_path(puzzle, bfs_result)
elif x==2:
    print("DFS")
    show_path(puzzle, dfs_result)
elif x==3:
    print("A* with heuristic manhattan")
    show_path(puzzle, astar_result1)
elif x==4:
    print("A* with heuristic euclidean")
    show_path(puzzle, astar_result2)
