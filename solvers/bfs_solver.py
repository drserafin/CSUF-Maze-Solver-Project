# solvers/bfs_solver.py
# Author: Erik Argueta (module refactored as Python Generator using 'yield')
# This allows the algorithm to pause it's execution state at every step,
# handing control back to the Tkinter main loop so the GUI can draw the 
# search progress (blue cells) in real-time

def solve_bfs(grid_data, rows, cols):
    """
    Breadth-First Search Algorithm.
    Yields the current state so the GUI can animate the process.
    """
    # 1. Find the Start Node ('S')
    start_node = None
    for r in range(rows):
        for c in range(cols):
            if grid_data[r][c] == 'S':
                start_node = (r, c)
                break

    if not start_node: return

    # 2. Setup BFS Data Structures (Erik's logic)
    queue = [start_node]
    visited = {start_node}
    parent_map = {}
    nodes_explored = 0

    # 3. The main algorithm loop
    while queue:
        # BFS uses a Queue (First-In, First-Out)
        curr_r, curr_c = queue.pop(0)
        nodes_explored += 1

        # Did we find the End Node ('E')?
        if grid_data[curr_r][curr_c] == 'E':
            # Backtrack to get the final path
            path = []
            curr = parent_map.get((curr_r, curr_c))
            while curr and curr != start_node:
                path.append(curr)
                curr = parent_map.get(curr)
                
            # Yield the final success state back to the GUI
            yield ("FOUND", nodes_explored, path)
            return

        # YIELD: Pause the algorithm and hand the current node to the GUI for the blue color!
        yield ("EXPLORING", nodes_explored, (curr_r, curr_c))

        # Check Neighbors (Up, Down, Left, Right - Erik's logic)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = curr_r + dr, curr_c + dc
            
            # If within bounds, not a wall ('#'), and not visited
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid_data[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent_map[(nr, nc)] = (curr_r, curr_c)
                    queue.append((nr, nc))

    # If the queue empties and no end is found
    yield ("NO_SOLUTION", nodes_explored, [])