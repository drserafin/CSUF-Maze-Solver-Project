"""
navlink.py

This module defines the NavLink UI component for the Maze Solver application.

Responsibilities:
- Creates the top navigation/header bar of the application.
- Displays the application title and course information.
- Provides a visual legend explaining maze cell colors (Start, End, Wall, Path).
- Organizes header layout with a left branding section and a right legend section.

This component is intended to be placed at the top of the main application window.
"""

import tkinter as tk
from .styles import *

class NavLink(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_DARK, height=80)
        self.pack(side="top", fill="x", padx=20, pady=(15, 0))
        
        title_frame = tk.Frame(self, bg=BG_DARK)
        title_frame.pack(side="left")

        tk.Label(
            title_frame,
            text="🧩 Maze Solver",
            font=FONT_TITLE,
            fg="white",
            bg=BG_DARK
        ).pack(anchor="w")

        tk.Label(
            title_frame,
            text="CSUF CPSC 335 - Algorithm Engineering",
            font=("Arial", 9),
            fg=TEXT_GRAY,
            bg=BG_DARK
        ).pack(anchor="w")

        legend_frame = tk.Frame(self, bg=BG_DARK)
        legend_frame.pack(side="right", pady=10)

        legend_items = [
            ("Start", COL_START),
            ("End", COL_END),
            ("Wall", COL_WALL),
            ("Path", COL_PATH)
        ]

        for text, color in legend_items:
            f = tk.Frame(legend_frame, bg=BG_DARK)
            f.pack(side="left", padx=10)

            tk.Frame(
                f,
                width=12,
                height=12,
                bg=color
            ).pack(side="left", padx=5)

            tk.Label(
                f,
                text=text,
                fg=TEXT_GRAY,
                bg=BG_DARK,
                font=("Arial", 9)
            ).pack(side="left")