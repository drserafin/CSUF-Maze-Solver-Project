"""
maze_app.py

Main GUI controller for the CSUF Maze Solver application.

Responsibilities:
- Orchestrates the UI layout using custom components.
- Manages the state of the maze grid (loading, generation, and resizing).
- Interfaces with backend solvers (BFS) and generators.
- Handles real-time animation of search algorithms while preserving 
  UI responsiveness via Tkinter's 'after' loop.
"""

import tkinter as tk
from tkinter import filedialog, messagebox

# Internal GUI Component Imports
from .styles import *
from .navlink import NavLink
from .maze_grid import MazeGrid
from .stats_display import StatsDisplay
from .ui_components import SidebarBox, StyledButton

# Backend Algorithm Imports
from solvers.bfs_solver import solve_bfs
from .maze_generator import create_perfect_maze, create_unsolvable_maze

class MazeApp:
    def __init__(self, root):
        """Initializes the main application window and core variables."""
        self.root = root
        self.root.title("CSUF Maze Solver")
        self.root.configure(bg=BG_DARK)
        
        # Set a minimum size to prevent UI clipping on small screens
        self.root.minsize(1050, 700)

        # Maze state variables
        self.rows = self.cols = 21
        self.grid_data = []
        self.selected_algo = tk.StringVar(value="BFS")
        
        # solve_id acts as a session token to stop old animations if a new one starts
        self.solve_id = 0

        self.setup_ui()
        
        # Initial maze generation on startup
        self.root.after(200, self.generate_perfect_maze)

    def setup_ui(self):
        """Builds the primary UI regions: Navigation, Maze Canvas, and Sidebar."""
        self.nav = NavLink(self.root)

        # Main horizontal container
        body = tk.Frame(self.root, bg=BG_DARK)
        body.pack(fill="both", expand=True, padx=10, pady=5)

        # LEFT SIDE: The Maze Canvas
        self.maze_grid = MazeGrid(body)
        self.maze_grid.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # RIGHT SIDE: The Sidebar Control Panel
        sidebar = tk.Frame(body, bg=BG_DARK)
        sidebar.pack(side="right", fill="y", padx=10, pady=5)
        
        # Invisible spacer to maintain a clean, consistent sidebar width
        tk.Frame(sidebar, width=400, height=1, bg=BG_DARK).pack()

        # --- SECTION 1: MAZE SOURCE ---
        src_box = SidebarBox(sidebar, "MAZE SOURCE")
        StyledButton(src_box.content, "📋 Simple 8x8", lambda: self.set_size(8))
        StyledButton(src_box.content, "📋 Medium 25x25", lambda: self.set_size(25))
        StyledButton(src_box.content, "📋 No Solution", self.generate_unsolvable_maze)

        tk.Label(src_box.content, text="Adjust Maze Size", bg=BG_PANEL, 
                 fg=ACCENT_NEON, font=FONT_MAIN).pack(pady=(15, 5))

        self.size_slider = tk.Scale(
            src_box.content, from_=11, to=61, orient="horizontal", 
            bg=BG_PANEL, fg="white", highlightthickness=0, troughcolor=BORDER_COL,
            command=lambda s: self.set_size(int(s))
        )
        self.size_slider.set(21)
        self.size_slider.pack(fill="x", pady=(0, 10))

        StyledButton(src_box.content, "⚡ Generate Perfect Maze", self.generate_perfect_maze)
        StyledButton(src_box.content, "📤 Load from .txt", self.load_from_file)

        # --- SECTION 2: ALGORITHM SELECTION ---
        algo_box = SidebarBox(sidebar, "ALGORITHM")
        
        btn_frame = tk.Frame(algo_box.content, bg=BG_PANEL)
        btn_frame.pack(fill="x", pady=(0, 10))

        self.bfs_btn = tk.Label(btn_frame, text="BFS", bg=ACCENT_NEON, fg="black", 
                                font=FONT_BOLD, width=8, pady=10, cursor="hand2")
        self.bfs_btn.pack(side="left", expand=True, fill="x", padx=(0, 4))
        self.bfs_btn.bind("<Button-1>", lambda e: self.set_algo("BFS"))

        self.dfs_btn = tk.Label(btn_frame, text="DFS", bg=BG_DARK, fg="white", 
                                font=FONT_BOLD, width=8, pady=10, cursor="hand2")
        self.dfs_btn.pack(side="right", expand=True, fill="x", padx=(4, 0))
        self.dfs_btn.bind("<Button-1>", lambda e: self.set_algo("DFS"))

        tk.Label(algo_box.content, text="Animation Speed", bg=BG_PANEL, 
                 fg=ACCENT_NEON, font=FONT_MAIN).pack(pady=(10, 5))

        self.speed_slider = tk.Scale(
            algo_box.content, from_=1, to=100, orient="horizontal", 
            bg=BG_PANEL, fg="white", highlightthickness=0, troughcolor=BORDER_COL
        )
        self.speed_slider.set(70)
        self.speed_slider.pack(fill="x", pady=(0, 15))

        # --- SECTION 3: ACTIONS ---
        action_frame = tk.Frame(algo_box.content, bg=BG_PANEL)
        action_frame.pack(fill="x", pady=(10, 0))

        self.solve_btn = tk.Label(action_frame, text="▶ Solve", bg=ACCENT_GREEN, 
                                  fg="black", font=FONT_BOLD, pady=12, cursor="hand2")
        self.solve_btn.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self.solve_btn.bind("<Button-1>", lambda e: self.start_solver())

        self.reset_btn = tk.Label(action_frame, text="↺", bg=BG_DARK, fg="white", 
                                  font=FONT_BOLD, width=4, pady=12, cursor="hand2")
        self.reset_btn.pack(side="right")
        self.reset_btn.bind("<Button-1>", lambda e: self.reset_maze())

        # --- SECTION 4: RESULTS ---
        self.stats = StatsDisplay(sidebar)

    # --- LOGIC METHODS ---

    def set_algo(self, name):
        """Updates the selected algorithm and UI button states."""
        self.selected_algo.set(name)
        self.bfs_btn.configure(bg=ACCENT_NEON if name == "BFS" else BG_DARK, 
                               fg="black" if name == "BFS" else "white")
        self.dfs_btn.configure(bg=ACCENT_NEON if name == "DFS" else BG_DARK, 
                               fg="black" if name == "DFS" else "white")
        self.stats.algo.update(name)

    def set_size(self, val):
        """Adjusts the maze dimensions (must be odd for the generator)."""
        val = int(val)
        if val % 2 == 0: val += 1
        self.rows = self.cols = val
        self.generate_perfect_maze()

    def generate_perfect_maze(self):
        """Invokes the generator to create a new solvable maze."""
        self.solve_id += 1 # Interrupts any running animations
        self.grid_data = create_perfect_maze(self.rows, self.cols)
        self.stats.reset_stats()
        self.maze_grid.init_grid(self.grid_data, self.rows, self.cols)

    def generate_unsolvable_maze(self):
        """Creates a maze with a wall down the middle."""
        self.solve_id += 1
        self.grid_data = create_unsolvable_maze(self.rows, self.cols)
        self.stats.reset_stats()
        self.maze_grid.init_grid(self.grid_data, self.rows, self.cols)

    def load_from_file(self):
        """Loads a maze structure from a .txt file."""
        file_path = filedialog.askopenfilename(title="Select Maze File", 
                                              filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if not file_path: return

        try:
            self.solve_id += 1
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]

            if not lines: raise ValueError("The file is empty.")

            self.rows = len(lines)
            self.cols = len(lines[0])
            self.grid_data = [list(row) for row in lines]

            self.stats.reset_stats()
            self.maze_grid.init_grid(self.grid_data, self.rows, self.cols)
        except Exception as e:
            messagebox.showerror("Error Loading File", f"Could not load the maze:\n\n{str(e)}")

    def reset_maze(self):
        """Clears current solution and resets to a new random maze."""
        self.stats.reset_stats()
        self.generate_perfect_maze()

    def start_solver(self):
        """Executes the solver and triggers the visual animation sequence."""
        self.solve_id += 1
        current_session = self.solve_id

        algo = self.selected_algo.get()
        self.stats.reset_stats()
   
        # Clean current grid of old explored (X) or path (P) tiles
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid_data[r][c] in ('X', 'P'):
                    self.grid_data[r][c] = '.'
                    
        self.maze_grid.init_grid(self.grid_data, self.rows, self.cols)

        # 1. RUN ALGORITHM (Synchronous)
        if algo == "BFS":
            path, explored_nodes, runtime = solve_bfs(self.grid_data)
        elif algo == "DFS":
            print("DFS not yet implemented.")
            return

        # 2. UPDATE STATIC STATS
        self.stats.nodes.update(str(len(explored_nodes)))
        self.stats.runtime.update(f"{runtime:.4f} ms")

        # 3. ANIMATION LOGIC
        delay = int(105 - self.speed_slider.get())

        def animate_path(idx=0):
            """Step-by-step coloring of the final solution path."""
            if current_session != self.solve_id: return

            if not path:
                self.stats.found.update("No", COL_END)
                return

            if idx == 0:
                self.stats.found.update("Yes", ACCENT_GREEN)
                self.stats.length.update(f"{len(path)} steps", ACCENT_GREEN)

            if idx < len(path):
                r, c = path[idx]
                if self.grid_data[r][c] not in ('S', 'E'):
                    self.grid_data[r][c] = 'P' 
                    self.maze_grid.draw_cell(r, c, 'P')
                self.root.after(delay, animate_path, idx + 1)

        def animate_explored(idx=0):
            """Step-by-step coloring of every node visited by the algorithm."""
            if current_session != self.solve_id: return

            if idx < len(explored_nodes):
                r, c = explored_nodes[idx]
                if self.grid_data[r][c] not in ('S', 'E'):
                    self.grid_data[r][c] = 'X' 
                    self.maze_grid.draw_cell(r, c, 'X')
                self.root.after(delay, animate_explored, idx + 1)
            else:
                # Once exploration is done, draw the winning path
                animate_path(0)

        # Start the sequence
        animate_explored(0)