"""
maze_generator.py

Handles the algorithmic generation of 2D maze grids. 
Separated from the GUI to keep the application modular.

The 'Perfect Maze' is generated using a Randomized Depth-First Search 
(Recursive Backtracker) algorithm, ensuring a solvable path with 
no loops and no unreachable areas.
"""

import random

def create_perfect_maze(rows, cols):
    """
    Generates a perfect maze where every cell is reachable and exactly 
    one primary path exists between any two points.
    
    Algorithm: Randomized Depth-First Search
    1. Start with a grid full of walls.
    2. Pick a starting cell and mark it as part of the maze.
    3. While there are unvisited cells:
        - If the current cell has unvisited neighbors, pick one at random.
        - Remove the wall between the current cell and the chosen neighbor.
        - Move to the neighbor and repeat.
    """
    # Initialize grid with walls ('#')
    grid_data = [['#' for _ in range(cols)] for _ in range(rows)]
    
    # DFS Stack and Visited set
    stack = [(0, 0)]
    visited = {(0, 0)}

    # Starting point in the grid
    grid_data[0][0] = '.'

    while stack:
        r, c = stack[-1]
        neighbors = []

        # Check neighbors at a distance of 2 (to leave walls in between)
        for dr, dc in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                neighbors.append((nr, nc))

        if neighbors:
            # Choose a random neighbor to move to
            nr, nc = random.choice(neighbors)
            
            # Remove the wall between the current cell and the chosen neighbor
            grid_data[r + (nr - r) // 2][c + (nc - c) // 2] = '.'
            grid_data[nr][nc] = '.'

            visited.add((nr, nc))
            stack.append((nr, nc))
        else:
            # Backtrack if no unvisited neighbors remain
            stack.pop()

    # Place the Start and End markers
    grid_data[0][0] = 'S'
    grid_data[rows - 1][cols - 1] = 'E'
    
    return grid_data

def create_unsolvable_maze(rows, cols):
    """
    Generates a grid that is physically impossible to solve.
    Useful for testing algorithm failure handling in the GUI.
    """
    # Create an open floor grid ('.')
    grid_data = [['.' for _ in range(cols)] for _ in range(rows)]
    
    # Place a solid vertical wall ('#') down the center
    mid_col = cols // 2
    for r in range(rows):
        grid_data[r][mid_col] = '#'

    # Place Start and End on opposite sides of the wall
    grid_data[0][0] = 'S'
    grid_data[rows - 1][cols - 1] = 'E'
    
    return grid_data