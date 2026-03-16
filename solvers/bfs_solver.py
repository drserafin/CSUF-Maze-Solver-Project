"""
bfs_solver.py

Responsible for implementing the Breadth-First Search (BFS) pathfinding
algorithm for the maze solver. This module locates the start and end nodes,
explores the maze level-by-level, tracks explored nodes for visualization,
reconstructs the shortest path, and returns performance timing data.
"""

import time
from collections import deque

def solve_bfs(grid_data):
    start_time = time.time()

    rows = len(grid_data)
    cols = len(grid_data[0])

    start_node = None
    end_node = None

    for r in range(rows):
        for c in range(cols):
            if grid_data[r][c] == 'S':
                start_node = (r, c)
            elif grid_data[r][c] == 'E':
                end_node = (r, c)

    if not start_node or not end_node:
        return [], [], 0.0

    queue = deque([start_node])
    visited = {start_node}
    parent_map = {}
    explored_nodes = []

    while queue:
        curr_r, curr_c = queue.popleft()
        explored_nodes.append((curr_r, curr_c))

        if (curr_r, curr_c) == end_node:
            path = []
            curr = parent_map.get((curr_r, curr_c))

            while curr and curr != start_node:
                path.append(curr)
                curr = parent_map.get(curr)

            path.reverse()
            runtime = (time.time() - start_time) * 1000
            return path, explored_nodes, runtime

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = curr_r + dr
            nc = curr_c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid_data[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent_map[(nr, nc)] = (curr_r, curr_c)
                    queue.append((nr, nc))

    runtime = (time.time() - start_time) * 1000
    return [], explored_nodes, runtime