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

def intro():
    print("Welcome to the Breadth First Solver (BFS) program.")
    print("Here is the maze being read:")
    readFile()


def outro():
    print("Algorithm Used: BFS")
    print("Path Length: ")
    print("Number of Visited Cells: ")
    print("Runtime: ")

def readFile():
    try:
        with open('mazes/basic_maze.txt', 'r') as file:
            maze = file.read()
            print(maze)
    except FileNotFoundError:
        print("Error: File 'maze.txt' was not found.")


def setMaze():
    rowSize = int(input("Enter the total rows in the maze: "))
    colSize = int(input("Enter the total columns in the maze: "))
    V = rowSize * colSize



intro()