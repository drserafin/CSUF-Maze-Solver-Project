"""
maze_app.py

This module defines the main application controller for the Maze Solver.

Responsibilities:
- Initialize and manage the main Tkinter window and overall layout.
- Coordinate UI components such as the navigation bar, maze grid, sidebar controls, and statistics panel.
- Handle user interactions including maze size selection, algorithm selection, solving, and resetting.
- Generate solvable mazes using the Recursive Backtracking algorithm.
- Serve as the central controller connecting the UI with maze generation and future pathfinding algorithms (BFS/DFS).
"""

import tkinter as tk
import random
from .styles import *
from .navlink import NavLink
from .maze_grid import MazeGrid
from .stats_display import StatsDisplay


class SidebarBox(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, bg=BG_PANEL, highlightthickness=1, highlightbackground=BORDER_COL)
        self.pack(fill="x", pady=(0, 12)) 
        
        self.content = tk.Frame(self, bg=BG_PANEL)
        self.content.pack(fill="both", expand=True, padx=12, pady=12)
        
        tk.Label(self.content, text=title, font=FONT_BOLD, 
                 bg=BG_PANEL, fg=TEXT_GRAY).pack(anchor="w", pady=(0, 10))


class StyledButton(tk.Button):
    def __init__(self, parent, text, command, color=BG_DARK, text_color="white", **kwargs):
        super().__init__(parent, text=text, command=command, bg=color, fg=text_color, 
                         relief="flat", activebackground=BORDER_COL, 
                         font=FONT_BOLD, pady=10, **kwargs)
        self.pack(fill="x", pady=4)


class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg=BG_DARK)
        self.rows = self.cols = 21 
        self.grid_data = []
        self.selected_algo = tk.StringVar(value="BFS")
        
        self.setup_ui()
        self.root.after(200, self.generate_perfect_maze)

    def setup_ui(self):
        self.nav = NavLink(self.root)
        
        body = tk.Frame(self.root, bg=BG_DARK)
        body.pack(fill="both", expand=True, padx=10, pady=5)

        self.maze_grid = MazeGrid(body)
        
        sidebar = tk.Frame(body, bg=BG_DARK, width=340)
        sidebar.pack(side="right", fill="y", padx=10, pady=10)
        sidebar.pack_propagate(False)

        src_box = SidebarBox(sidebar, "MAZE SOURCE")
        StyledButton(src_box.content, "📋 Simple 11x11", lambda: self.set_size(11))
        StyledButton(src_box.content, "📋 Medium 25x25", lambda: self.set_size(25))
        
        tk.Label(src_box.content, text="Adjust Maze Size", bg=BG_PANEL, fg=ACCENT_NEON, font=FONT_MAIN).pack(pady=(10,0))
        self.size_slider = tk.Scale(src_box.content, from_=11, to=61, orient="horizontal", bg=BG_PANEL, 
                                   fg="white", highlightthickness=0, troughcolor=BORDER_COL,
                                   command=lambda s: self.set_size(int(s)))
        self.size_slider.set(21)
        self.size_slider.pack(fill="x", pady=(0, 10))
        
        StyledButton(src_box.content, "⚡ Generate Perfect Maze", self.generate_perfect_maze)
        StyledButton(src_box.content, "📤 Load from .txt", lambda: print("Load File"))

        algo_box = SidebarBox(sidebar, "ALGORITHM")
        
        btn_frame = tk.Frame(algo_box.content, bg=BG_PANEL)
        btn_frame.pack(fill="x", pady=(0, 10))
        
        self.bfs_btn = tk.Button(btn_frame, text="BFS", command=lambda: self.set_algo("BFS"),
                                 bg=ACCENT_NEON, fg="black", relief="flat", font=FONT_BOLD, width=8, pady=8)
        self.bfs_btn.pack(side="left", expand=True, fill="x", padx=(0,4))
        
        self.dfs_btn = tk.Button(btn_frame, text="DFS", command=lambda: self.set_algo("DFS"),
                                 bg=BG_DARK, fg="white", relief="flat", font=FONT_BOLD, width=8, pady=8)
        self.dfs_btn.pack(side="right", expand=True, fill="x", padx=(4,0))

        tk.Label(algo_box.content, text="Animation Speed", bg=BG_PANEL, fg=ACCENT_NEON, font=FONT_MAIN).pack()
        self.speed_slider = tk.Scale(algo_box.content, from_=1, to=100, orient="horizontal", bg=BG_PANEL, 
                                    fg="white", highlightthickness=0, troughcolor=BORDER_COL)
        self.speed_slider.set(70)
        self.speed_slider.pack(fill="x", pady=(0, 10))

        action_frame = tk.Frame(algo_box.content, bg=BG_PANEL)
        action_frame.pack(fill="x", pady=(5, 0))

        self.solve_btn = tk.Button(action_frame, text="▶ Solve", command=self.start_solver,
                                   bg=ACCENT_GREEN, fg="black", font=FONT_BOLD, relief="flat", pady=8)
        self.solve_btn.pack(side="left", fill="x", expand=True, padx=(0, 6))

        self.reset_btn = tk.Button(action_frame, text="↺", command=self.reset_maze,
                                   bg=BG_DARK, fg="white", font=FONT_BOLD, relief="flat", width=4, pady=8)
        self.reset_btn.pack(side="right")

        self.stats = StatsDisplay(sidebar)

    def set_algo(self, name):
        self.selected_algo.set(name)
        self.bfs_btn.configure(bg=ACCENT_NEON if name == "BFS" else BG_DARK, fg="black" if name == "BFS" else "white")
        self.dfs_btn.configure(bg=ACCENT_NEON if name == "DFS" else BG_DARK, fg="black" if name == "DFS" else "white")
        self.stats.algo.update(name)

    def set_size(self, val):
        val = int(val)
        if val % 2 == 0: 
            val += 1
        self.rows = self.cols = val
        self.generate_perfect_maze()

    def generate_perfect_maze(self):
        self.grid_data = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        stack, visited = [(0, 0)], set([(0, 0)])
        self.grid_data[0][0] = 0
        
        while stack:
            r, c = stack[-1]
            neighbors = []
            for dr, dc in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in visited:
                    neighbors.append((nr, nc))
            
            if neighbors:
                nr, nc = random.choice(neighbors)
                self.grid_data[r + (nr-r)//2][c + (nc-c)//2] = 0
                self.grid_data[nr][nc] = 0
                visited.add((nr, nc))
                stack.append((nr, nc))
            else:
                stack.pop()
        
        self.grid_data[0][0], self.grid_data[self.rows-1][self.cols-1] = 2, 3
        self.stats.reset_stats()
        self.maze_grid.init_grid(self.grid_data, self.rows, self.cols)

    def reset_maze(self):
        self.stats.reset_stats()
        self.generate_perfect_maze()

    def start_solver(self):
        algo = self.selected_algo.get()
        speed = self.speed_slider.get()
        self.stats.reset_stats()
        
        if algo == "BFS":
            print(f"Starting BFS with speed {speed}...")
        elif algo == "DFS":
            print(f"Starting DFS with speed {speed}...")