"""
stats_display.py

This module is responsible for displaying algorithm results and performance
statistics for the Maze Solver application.

Responsibilities:
- Render a structured results panel in the UI.
- Display key metrics from maze solving algorithms (algorithm used, path found,
  path length, nodes explored, runtime).
- Provide reusable UI rows for statistic entries.
- Allow dynamic updating and resetting of displayed algorithm results.
"""

import tkinter as tk
from .styles import *

class ResultLine(tk.Frame):
    def __init__(self, parent, icon, label, initial_val, val_color):
        super().__init__(parent, bg=BG_PANEL)
        self.pack(fill="x", pady=10)
        
        tk.Label(self, text=f"{icon} {label}", bg=BG_PANEL, fg=TEXT_GRAY, font=FONT_MAIN).pack(side="left")
        
        self.val_lbl = tk.Label(self, text=initial_val, bg=BG_PANEL, fg=val_color, font=FONT_MONO)
        self.val_lbl.pack(side="right")

    def update(self, new_val, new_color=None):
        self.val_lbl.config(text=new_val)
        if new_color is not None:
            self.val_lbl.config(fg=new_color)

class StatsDisplay(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_PANEL, highlightthickness=1, highlightbackground=BORDER_COL)
        self.pack(fill="both", expand=True, pady=0)
        
        self.container = tk.Frame(self, bg=BG_PANEL)
        self.container.pack(fill="both", expand=True, padx=12, pady=12)

        tk.Label(self.container, text="RESULTS", font=FONT_BOLD, 
                 bg=BG_PANEL, fg=TEXT_GRAY).pack(anchor="w", pady=(0, 10))

        self.algo = ResultLine(self.container, "⚙️", "Algorithm", "BFS", ACCENT_NEON)
        self.found = ResultLine(self.container, "✅", "Path Found", "No", COL_END)
        self.length = ResultLine(self.container, "📏", "Path Length", "0 steps", ACCENT_NEON)
        self.nodes = ResultLine(self.container, "🔍", "Nodes Explored", "0", TEXT_GRAY)
        self.runtime = ResultLine(self.container, "⏱️", "Runtime", "0.000 ms", ACCENT_NEON)

    def reset_stats(self):
        self.found.update("No", COL_END)       
        self.length.update("0 steps", ACCENT_NEON) 
        self.nodes.update("0", TEXT_GRAY)
        self.runtime.update("0.000 ms", ACCENT_NEON)