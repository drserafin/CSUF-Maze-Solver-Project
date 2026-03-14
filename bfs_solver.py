"""
bfs_solver.py
Author: Erik Argueta
Description: 
    1. Finds shortest path (in number of steps) when a path exists 
    2. Provides correctness testing and edge cases

INPUT:
    Your maze is a 2D grid of cells:
        S = Start (exactly 1)
        E = Exit/End (exactly 1)
        # = Wall (blocked)
        . = Open path (walkable)

    Valid Moves:
        - 4-direction movement only: Up, Down, Left, Right
        - No diagonal moves
    
OUTPUT: 
    1. Algortihm used (BFS vs DFS)
    2. Path length (number of steps from S to E)
    3. Number of visited/explored cells (how many nodes expanded)
    4. Runtime (simple timing using Python time module)
"""

from collections import deque
import time


def intro(maze):
    print("Welcome to the Breadth First Solver (BFS) program.")
    print("\nHere is the maze being read:")
    readFile(maze)


def readFile(maze):
    try:
        with open('mazes/basic_maze.txt', 'r') as file:
            for line in file:
                clean_line = line.replace('\n', '')
                print(clean_line)
                maze.append(list(clean_line))
            # print(maze)
    except FileNotFoundError:
        print("Error: File 'maze.txt' was not found.")


# finds the location index of where the maze Starts
def findStart(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'S':
                # print(f"\nStart located at location: ({row}, {col})")
                return (row, col)

# start: (row, col)
def bfs(maze, start):
    visited = set()
    queue = [start]
    solution = [start]
    visited.add(start)
    # print(f"Running BFS Algorithm...")

    start = time.time()
    while queue:
        vertex_row, vertex_col = queue.pop(0)
        # print(f"Current Vertex Coordinate: {vertex_row}, {vertex_col}")

        for move_row, move_col in neighbors:
            neighbor_row = vertex_row + move_row
            neighbor_col = vertex_col + move_col

            if neighbor_row >=0 and neighbor_col >= 0 and (neighbor_row, neighbor_col) not in visited:     # If the cell is within bounds AND has NOT been visited
                visited.add((neighbor_row, neighbor_col))       # Add the cell to visited[]

                if maze[neighbor_row][neighbor_col] == '.':     # If the cell being visited is '.'
                    queue.append((neighbor_row, neighbor_col))  # add this cell to queue to progress
                    solution.append((neighbor_row, neighbor_col))   # add to the solution set
                
                elif maze[neighbor_row][neighbor_col] == 'E':    # If the cell being visited is the End
                    # print(f"Located End...")
                    solution.append((neighbor_row, neighbor_col))   # add to the solution set
                    print(f"")
                    end = time.time()
                    return solution, len(visited), True, (end-start)

    end = time.time()
    return solution, len(visited), False, (end-start)

neighbors = [
    (-1, 0),    # check row above
    (1, 0),     # check row below
    (0,-1),     # check col left
    (0,1)       # check col right
]

def printResults(solution, visited, success, time_elapsed):
    if success == True: print("Solution was found!") 
    else: print("No Solution Found")
    
    print(f"Algortihm Used: BFS")
    if success == True:
        print(f"The Length of the Shortest Path is: {len(solution)}")
    if success == False:
        print(f"No Solution Found.")
    
    print(f"Number of Visited Cells: {visited}")
    print(f"Time elapsed: {time_elapsed: .8f}s")

maze = []
intro(maze)
start = findStart(maze)
shortest_path, total_visited, success, time_elapsed = bfs(maze, start)
printResults(shortest_path, total_visited, success, time_elapsed)