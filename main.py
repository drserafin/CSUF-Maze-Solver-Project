import tkinter as tk
from gui_components import Navbar, MazeGrid
from utils import create_sidebar_box

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSUF Maze Solver")
        self.root.geometry("1300x900")
        self.root.configure(bg="#0d1117")

        # 1. NAVBAR
        self.nav = Navbar(self.root)

        # 2. BODY
        self.body = tk.Frame(self.root, bg="#0d1117")
        self.body.pack(fill="both", expand=True)

        # 3. MAZE (Left Side)
        self.maze = MazeGrid(self.body)
        self.maze.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=20)

        # 4. SIDEBAR (Right Side)
        self.sidebar = tk.Frame(self.body, width=350, bg="#0d1117")
        self.sidebar.pack(side="right", fill="y", padx=(10, 20), pady=20)
        self.sidebar.pack_propagate(False)

        # Use the utility function to create the boxes
        self.source_box = create_sidebar_box(self.sidebar, "MAZE SOURCE", 250)
        self.algo_box = create_sidebar_box(self.sidebar, "ALGORITHM", 200)
        self.results_box = create_sidebar_box(self.sidebar, "RESULTS", 280)

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()