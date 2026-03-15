"""
maze_grid.py
"""

import tkinter as tk
from .styles import *

class MazeGrid(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BG_DARK, highlightbackground=BORDER_COL, highlightthickness=1)
        self.canvas = tk.Canvas(self, bg=BG_DARK, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=20, pady=20)
        self.grid_data = []
        self.rows = 0
        self.cols = 0
        self.canvas.bind("<Configure>", self.draw)

    def init_grid(self, grid_data, rows, cols):
        self.grid_data = grid_data
        self.rows = rows
        self.cols = cols
        self.draw()

    def get_color(self, char):
        if char == 'S': return COL_START
        if char == 'E': return COL_END
        if char == '#': return COL_WALL
        if char == '.': return COL_TILE
        if char == 'X': return COL_EXPLORED
        if char == 'P': return COL_PATH
        return BG_DARK

    def draw(self, event=None):
        if not self.grid_data or self.rows == 0: return
        self.canvas.delete("all")
        
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        
        MAX_CELL_SIZE = 100 
        cell_size = min(canvas_w / self.cols, canvas_h / self.rows, MAX_CELL_SIZE)
        
        padding = 4 
        inner_size = cell_size - padding
        
        maze_block_w = cell_size * self.cols
        maze_block_h = cell_size * self.rows
        
        start_x = (canvas_w - maze_block_w) / 2
        start_y = (canvas_h - maze_block_h) / 2

        for r in range(self.rows):
            for c in range(self.cols):
                char = self.grid_data[r][c]
                color = self.get_color(char)
                
                x1 = start_x + (c * cell_size) + (padding / 2)
                y1 = start_y + (r * cell_size) + (padding / 2)
                x2 = x1 + inner_size
                y2 = y1 + inner_size
                
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color, 
                    outline=BORDER_COL if char == '#' else "", 
                    width=1, 
                    tags=f"cell_{r}_{c}"
                )
                
                if char == 'S':
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text="S", 
                                          fill="black", font=("Arial", int(inner_size/2.5), "bold"))
                elif char == 'E':
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text="E", 
                                          fill="white", font=("Arial", int(inner_size/2.5), "bold"))

    def draw_cell(self, r, c, char):
        """Updates a single cell visually for real-time algorithm animation."""
        color = self.get_color(char)
        # Updates the existing rectangle by its unique tag
        self.canvas.itemconfig(f"cell_{r}_{c}", fill=color)