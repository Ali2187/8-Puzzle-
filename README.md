# 8-Puzzle Solver

A Python implementation of the classic 8-puzzle problem solver with multiple search algorithms. This project demonstrates different search strategies for solving the sliding puzzle problem.

## Overview

The 8-puzzle is a sliding puzzle that consists of a 3×3 grid with 8 numbered tiles and one empty space (represented as 0). The goal is to rearrange the tiles from a given starting configuration to the goal state by sliding tiles into the empty space.

## Project Structure

```
.
├── EightPuzzle.py       # Core puzzle class and state representation
├── astar_algorithm.py   # A* search implementation (Manhattan & Euclidean heuristics)
├── bfs_algorithm.py     # Breadth-First Search implementation
├── dfs_algorithm.py     # Depth-First Search implementation
├── game.py              # Main entry point with interactive menu
└── README.md            # This file
```

## Algorithms Implemented

### 1. Breadth-First Search (BFS)
- **File**: `bfs_algorithm.py`
- **Strategy**: Explores all nodes at the present depth before moving to nodes at the next depth level
- **Guarantees**: Optimal solution (shortest path)
- **Space Complexity**: O(b^d) - exponential
- **Use case**: When optimal solution is required and state space is manageable

### 2. Depth-First Search (DFS)
- **File**: `dfs_algorithm.py`
- **Strategy**: Explores as far as possible along each branch before backtracking
- **Guarantees**: Not guaranteed to find optimal solution
- **Space Complexity**: O(bd) - linear
- **Configuration**: Max depth limit of 50 (configurable)
- **Use case**: Memory-constrained environments

### 3. A* Search with Manhattan Distance
- **File**: `astar_algorithm.py`
- **Heuristic**: Manhattan distance (sum of horizontal + vertical distances of each tile from goal)
- **Strategy**: Best-first search using f(n) = g(n) + h(n)
- **Guarantees**: Optimal solution (with admissible heuristic)
- **Use case**: Most efficient for this problem

### 4. A* Search with Euclidean Distance
- **File**: `astar_algorithm.py`
- **Heuristic**: Euclidean distance (straight-line distance of each tile from goal)
- **Strategy**: Best-first search using f(n) = g(n) + h(n)
- **Guarantees**: Optimal solution (with admissible heuristic)
- **Use case**: Alternative heuristic for comparison

## Installation

```bash
# No external dependencies required - uses only Python standard library
python3 --version  # Requires Python 3.6+
```

## Usage

Run the main game file to interactively solve the puzzle:

```bash
python game.py
```

### Interactive Menu

```
**** welcome to 8puzzle****
press 1 to display BFS.
press 2 to display DFS.
press 3 to display A* with heuristic manhattan.
press 4 to display A* with heuristic euclidean.

Enter from 1 to 4: 
```

### Default Starting State

The puzzle uses this default starting configuration:
```
[1, 2, 5]
[3, 4, 0]
[6, 7, 8]
```

### Goal State
```
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
```

## Customizing the Puzzle

To use a different starting state, modify the `start_state` variable in `game.py`:

```python
start_state = [1, 2, 3,
               4, 5, 6,
               7, 8, 0]  # Already solved
```

Or create a custom puzzle in your own script:

```python
from EightPuzzle import EightPuzzle
from astar_algorithm import a_star

# Custom start state
start_state = [2, 8, 3,
               1, 6, 4,
               7, 0, 5]

puzzle = EightPuzzle(start_initial_state=start_state)
result = a_star(puzzle, heuristic="manhattan")

print(f"Solution found in {result['cost_of_path']} moves")
print(f"Path: {result['path_to_goal']}")
```

## Output Format

All search algorithms return a dictionary with the following keys:

| Key | Description |
|-----|-------------|
| `path_to_goal` | List of moves (e.g., `['up', 'left', 'down']`) |
| `cost_of_path` | Number of moves in the solution |
| `nodes_expanded` | Number of nodes explored during search |
| `search_depth` | Depth of the solution |
| `running_time` | Execution time in seconds |

If no solution is found, `path_to_goal` will be `None`.

## Example Output

```
 Initial State:
[1, 2, 5]
[3, 4, 0]
[6, 7, 8]
➡️ Step 1: Move left
[1, 2, 5]
[3, 0, 4]
[6, 7, 8]
➡️ Step 2: Move up
[1, 0, 5]
[3, 2, 4]
[6, 7, 8]
...

--- Solution Summary ---
Path to Goal: left → up → left → down → down → right → right → up → up
Cost of Path: 9
Nodes Expanded: 156
Search Depth: 9
Running Time: 0.002341 seconds
```

## Algorithm Comparison

| Algorithm | Optimal? | Time Complexity | Space Complexity | Typical Nodes Expanded |
|-----------|----------|-----------------|------------------|------------------------|
| BFS | ✅ Yes | O(b^d) | O(b^d) | High |
| DFS | ❌ No | O(b^m) | O(bm) | Variable |
| A* (Manhattan) | ✅ Yes | O(b^d) | O(b^d) | Low |
| A* (Euclidean) | ✅ Yes | O(b^d) | O(b^d) | Low-Medium |

Where:
- b = branching factor (max 4 for 8-puzzle)
- d = depth of solution
- m = maximum depth of search tree

## How It Works

### State Representation
The puzzle state is represented as a flat list of 9 integers:
- Index 0-2: First row
- Index 3-5: Second row
- Index 6-8: Third row
- Value `0` represents the empty space

### Move Generation
The `EightPuzzle.neighbors()` method generates valid moves:
- **Up**: Move empty space up (index - 3)
- **Down**: Move empty space down (index + 3)
- **Left**: Move empty space left (index + 1)
- **Right**: Move empty space right (index - 1)

Edge cases are handled to prevent wrapping between rows.

### Heuristics
- **Manhattan Distance**: Σ|x₁ - x₂| + |y₁ - y₂| for each tile
- **Euclidean Distance**: Σ√((x₁ - x₂)² + (y₁ - y₂)²) for each tile

Both heuristics are admissible (never overestimate the true cost), guaranteeing optimality for A*.

## Requirements

- Python 3.6+
- No external packages required (uses `heapq`, `collections.deque`, `time`, `math`)

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to submit issues or pull requests to improve the algorithms, add new heuristics, or enhance the visualization.