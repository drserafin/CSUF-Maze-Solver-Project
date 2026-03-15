# CSUF Maze Solver Project

## Team Members & Roles
- **Kevin Serafin – GUI Engineer**  
  Responsible for application architecture, UI design and styling, maze generation, file I/O, and integration of the pathfinding algorithms into the GUI.

- **Erik Argueta – BFS Engineer**  
  Implemented the Breadth-First Search algorithm, shortest path computation, and performance analytics including runtime and nodes explored.

- **Matt – DFS Engineer**  
  Responsible for implementing the Depth-First Search exploration algorithm.

---

# 1. Overview
This application is a **Python-based Maze Solver** that visualizes the **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** algorithms.

The project includes a custom **Tkinter graphical user interface** that allows users to generate mazes, run search algorithms, and observe how each algorithm explores the maze in real time.

The application focuses on **algorithm visualization, performance comparison, and interactive exploration** of search strategies.

---

# 2. Key Features

## Rubric Compliance
The maze format follows the required character representation:

| Symbol | Meaning |
|------|------|
| `#` | Wall (Blocked) |
| `.` | Open Path |
| `S` | Start Position |
| `E` | Exit / End |

---

## Animated Search Visualization
Algorithms are implemented as **generators**, allowing the program to update the GUI during execution. This enables the visualization of each step of the search without freezing the interface.

---

## Maze Sources
The program supports multiple ways to load mazes:

- **Random Perfect Maze Generation**
- **Loading custom mazes from `.txt` files**

---

## Dynamic Grid Scaling
The maze grid automatically resizes and stays centered within the window.  
Cells maintain **perfect square proportions** regardless of screen size or window resizing.

---

## Results & Performance Metrics
The results panel displays key performance statistics including:

- Algorithm Used
- Path Length
- Nodes Explored
- Runtime (milliseconds)
- Solution Found / No Solution

---

# 3. How to Run

## Requirements
- Python **3.10 or higher**
- **Tkinter** (included with most Python installations)

---

## Instructions

1. Navigate to the project root directory.

2. Run the program:

```bash
python main.py