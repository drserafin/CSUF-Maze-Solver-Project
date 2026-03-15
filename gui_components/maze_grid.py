"""
maze_grid.py

This module defines the MazeGrid UI component responsible for rendering
and updating the maze visualization.

Responsibilities:
- Render the maze grid on a Tkinter canvas.
- Convert maze data (walls, paths, start, end, solution) into colored tiles.
- Automatically scale and center the maze when the window is resized.
- Provide efficient updates to grid cells during algorithm visualization.
"""

import tkinter as tk
from .styles import *

class MazeGrid(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_DARK, highlightthickness=1, highlightbackground=BORDER_COL)
        self.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        
        self.canvas = tk.Canvas(self, bg=BG_DARK, highlightthickness=0, bd=0)
        self.canvas.pack(fill="both", expand=True)
        
        self.last_data, self.last_rows, self.last_cols = None, 21, 21
        self.rect_ids = []
        self.canvas.bind("<Configure>", lambda e: self.init_grid(self.last_data, self.last_rows, self.last_cols))

    def init_grid(self, grid_data, rows, cols):
        if grid_data is None: 
            return

        self.last_data, self.last_rows, self.last_cols = grid_data, rows, cols
        self.canvas.delete("all")
        
        self.update_idletasks()
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if w <= 10: 
            return 

        self.cell_size = min(w / cols, h / rows)
        self.ox = (w - (cols * self.cell_size)) / 2
        self.oy = (h - (rows * self.cell_size)) / 2

        self.rect_ids = [[None for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                val = grid_data[r][c]

                color = COL_TILE if val == 0 else COL_WALL
                if val == 2: 
                    color = COL_START
                elif val == 3: 
                    color = COL_END
                elif val == 4: 
                    color = COL_PATH
                
                x1 = self.ox + (c * self.cell_size)
                y1 = self.oy + (r * self.cell_size)
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                self.rect_ids[r][c] = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, outline="#1c2128"
                )

    def update_all(self, grid_data):
        for r in range(len(grid_data)):
            for c in range(len(grid_data[0])):
                val = grid_data[r][c]

                color = COL_TILE if val == 0 else COL_WALL
                if val == 2: 
                    color = COL_START
                elif val == 3: 
                    color = COL_END
                elif val == 4: 
                    color = COL_PATH

                if self.rect_ids:
                    self.canvas.itemconfig(self.rect_ids[r][c], fill=color)