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

        ##########
        #S..#....#
        #.#.##.#.#
        #.#....#.#
        #.####.#E#
        #........#
        ##########

    Valid Moves:
        - 4-direction movement only: Up, Down, Left, Right
        - No diagonal moves
    
OUTPUT: 
    1. Algortihm used (BFS vs DFS)
    2. Path length (number of steps from S to E)
    3. Number of visited/explored cells (how many nodes expanded)
    4. Runtime (simple timing using Python time module)

    

    #######
    #S...E#
    #######

"""

from collections import deque

def intro(maze):
    print("Welcome to the Breadth First Solver (BFS) program.")
    print("Here is the maze being read:")
    readFile(maze)


def outro():
    print("Algorithm Used: BFS")
    print("Path Length: ")
    print("Number of Visited Cells: ")
    print("Runtime: ")

def readFile(maze):
    try:
        with open('mazes/basic_maze.txt', 'r') as file:
            for line in file:
                clean_line = line.replace('\n', '')
                maze.append(list(clean_line))
            print(maze)
    except FileNotFoundError:
        print("Error: File 'maze.txt' was not found.")


# finds the location index of where the maze Starts
def findStart(maze, start):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'S':
                print(f"Start located at maze[{row}, {col}]")
                return (row, col)

# start: (row, col)
def bfs(maze, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex_row, vertex_col = queue.pop(0)
        print(f"Current Vertex Coordinate: {vertex_row}, {vertex_col}")

        for move_row, move_col in neighbors:
            neighbor_row = vertex_row + move_row
            neighbor_col = vertex_col + move_col

            if maze[neighbor_row][neighbor_col] not in visited:
                visited.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col))

neighbors = [
    (-1, 0),    # check row above
    (1, 0),     # check row below
    (0,-1),     # check col left
    (0,1)       # check col right
]      

start = None
maze = []
intro(maze)
findStart(maze, start)
bfs(maze, start)
