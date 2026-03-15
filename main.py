"""
main.py

Application entry point for the Maze Solver.

Responsibilities:
- Initialize the Tkinter root window.
- Launch the MazeApp controller.
- Ensure the application starts in a maximized window state.
"""

import tkinter as tk
from gui_components.maze_app import MazeApp

if __name__ == "__main__":
    root = tk.Tk()
    root.title("CSUF Maze Solver")

    # Start application maximized
    root.state("zoomed")

    app = MazeApp(root)
    root.mainloop()