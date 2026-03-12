import tkinter as tk
from utils import add_legend_item

class Navbar(tk.Frame):
    def __init__(self, master):
        # Background Color
        super().__init__(master, bg="#0d1117", height=80)
        self.pack(side="top", fill="x", padx=20, pady=10)
        
        # Left side: Title and Subtitle
        title_frame = tk.Frame(self, bg="#0d1117")
        title_frame.pack(side="left")
        
        tk.Label(title_frame, text="🧩 Maze Solver", font=("Arial", 18, "bold"), 
                 fg="white", bg="#0d1117").pack(anchor="w")
        
        tk.Label(title_frame, text="BFS & DFS Visualization - Reference Demo", 
                 font=("Arial", 10), fg="#6e7681", bg="#0d1117").pack(anchor="w")

        # Right side: Color Legend (calling the helper from utils)
        legend_frame = tk.Frame(self, bg="#0d1117")
        legend_frame.pack(side="right", pady=10)
        
        add_legend_item(legend_frame, "Start", "#2ecc71")   # Green
        add_legend_item(legend_frame, "End", "#e74c3c")     # Red
        add_legend_item(legend_frame, "Wall", "#21262d")    # Dark Gray
        add_legend_item(legend_frame, "Path", "#f1c40f")    # Gold/Yellow

class MazeGrid(tk.Frame):
    def __init__(self, master, rows=15, cols=15):
        # The main container for the maze
        super().__init__(master, bg="#161b22", highlightbackground="#30363d", highlightthickness=1)
        self.rows = rows
        self.cols = cols
        
        # The Canvas is where the actual rectangles are drawn
        self.canvas = tk.Canvas(self, bg="#0d1117", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=20, pady=20)
        
        # This tells Python to redraw the grid whenever the window is resized
        self.canvas.bind("<Configure>", self.draw)

    def draw(self, event=None):
        """Calculates cell sizes and draws the grid squares."""
        self.canvas.delete("all")
        
        # Get current dimensions of the canvas
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        
        # Calculate width/height for each cell
        cell_w = w / self.cols
        cell_h = h / self.rows

        for r in range(self.rows):
            for c in range(self.cols):
                # Default background color for a cell
                color = "#161b22" 
                
                # Logic for Start and End positions
                if r == 0 and c == 0: 
                    color = "#2ecc71" # Start
                elif r == self.rows - 1 and c == self.cols - 1: 
                    color = "#e74c3c" # End

                # Draw the square with a small 2px offset to create a "grid" look
                self.canvas.create_rectangle(
                    c * cell_w + 2, 
                    r * cell_h + 2, 
                    (c + 1) * cell_w - 2, 
                    (r + 1) * cell_h - 2,
                    fill=color, 
                    outline="#21262d", 
                    width=1
                )