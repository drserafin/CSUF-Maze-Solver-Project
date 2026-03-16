"""
stats_display.py

Handles the 'RESULTS' panel in the sidebar.
Uses a reactive design where each stat line can be updated independently
by the MazeApp controller as the algorithm progresses.
"""

import tkinter as tk
from .styles import *

class ResultLine(tk.Frame):
    """
    A single row in the results panel containing an icon, label, and value.
    """
    def __init__(self, parent, icon, label, initial_val, val_color):
        super().__init__(parent, bg=BG_PANEL)
        
        # Standard vertical spacing between stat rows
        self.pack(fill="x", pady=8) 
        
        # Left Side: Icon and Label
        tk.Label(
            self, 
            text=f"{icon} {label}", 
            bg=BG_PANEL, 
            fg=TEXT_GRAY, 
            font=FONT_MAIN
        ).pack(side="left")
        
        # Right Side: The actual value (e.g., "0.1400 ms")
        # Note: We use side="right" to create a clean column on the edge of the panel.
        self.val_lbl = tk.Label(
            self, 
            text=initial_val, 
            bg=BG_PANEL, 
            fg=val_color, 
            font=FONT_MONO
        )
        self.val_lbl.pack(side="right")
        
    def update(self, new_val, new_color=None):
        """Updates the text and optionally the color of the stat value."""
        self.val_lbl.config(text=new_val)
        if new_color is not None:
            self.val_lbl.config(fg=new_color)

class StatsDisplay(tk.Frame):
    """
    The main Results card. Orchestrates the layout of all algorithm metrics.
    """
    def __init__(self, parent):
        super().__init__(parent, bg=BG_PANEL, highlightthickness=1, highlightbackground=BORDER_COL)
        self.pack(fill="both", expand=True, pady=0)
        
        # Inner padding container
        self.container = tk.Frame(self, bg=BG_PANEL)
        self.container.pack(fill="both", expand=True, padx=15, pady=15)

        # Section Header
        tk.Label(
            self.container, 
            text="RESULTS", 
            font=FONT_BOLD, 
            bg=BG_PANEL, 
            fg=TEXT_GRAY
        ).pack(anchor="w", pady=(0, 10))

        # Individual Metric Rows
        self.algo = ResultLine(self.container, "⚙️", "Algorithm", "BFS", ACCENT_NEON)
        self.found = ResultLine(self.container, "✅", "Path Found", "No", COL_END)
        self.length = ResultLine(self.container, "📏", "Path Length", "0 steps", ACCENT_NEON)
        self.nodes = ResultLine(self.container, "🔍", "Nodes Explored", "0", TEXT_GRAY)
        self.runtime = ResultLine(self.container, "⏱️", "Runtime", "0.000 ms", ACCENT_NEON)

    def reset_stats(self):
        """Restores all metrics to their default state for a new maze run."""
        self.found.update("No", COL_END)       
        self.length.update("0 steps", ACCENT_NEON) 
        self.nodes.update("0", TEXT_GRAY)
        self.runtime.update("0.000 ms", ACCENT_NEON)