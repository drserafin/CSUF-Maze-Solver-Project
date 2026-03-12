import tkinter as tk

def create_sidebar_box(parent, title, height):
    """Creates a styled dark card for the sidebar."""
    box = tk.Frame(parent, bg="#161b22", highlightbackground="#30363d", 
                   highlightthickness=1, height=height)
    box.pack(fill="x", pady=(0, 15))
    box.pack_propagate(False)
    
    tk.Label(box, text=title, fg="#8b949e", bg="#161b22", 
             font=("Arial", 9, "bold")).pack(anchor="w", padx=15, pady=10)
    return box

def add_legend_item(parent, text, color):
    """Helper to create the color dots in the navbar."""
    item_frame = tk.Frame(parent, bg="#0d1117")
    item_frame.pack(side="left", padx=10)
    
    # The color indicator
    tk.Frame(item_frame, width=12, height=12, bg=color).pack(side="left", padx=5)
    # The label
    tk.Label(item_frame, text=text, fg="#8b949e", bg="#0d1117", font=("Arial", 9)).pack(side="left")