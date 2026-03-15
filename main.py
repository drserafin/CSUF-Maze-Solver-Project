"""
main.py
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