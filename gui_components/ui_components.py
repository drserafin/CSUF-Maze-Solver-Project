"""
ui_components.py

Contains reusable, styled Tkinter widgets for the CSUF Maze Solver Sidebar.

Note:
- SidebarBox: Provides a themed container with a title and border.
- StyledButton: Implemented as a Frame + Label to bypass the macOS 
  native button bug where background colors are often ignored.
"""

import tkinter as tk
from .styles import *

class SidebarBox(tk.Frame):
    """
    A container for grouping related UI elements (e.g., Maze Source, Algorithm).
    Uses a panel background and subtle border for a modern 'card' aesthetic.
    """
    def __init__(self, parent, title):
        super().__init__(parent, bg=BG_PANEL, highlightthickness=1, highlightbackground=BORDER_COL)
        
        # Bottom padding to separate different cards in the sidebar
        self.pack(fill="x", pady=(0, 15))

        # Inner container to manage margins within the card
        self.content = tk.Frame(self, bg=BG_PANEL)
        self.content.pack(fill="both", expand=True, padx=15, pady=15)

        # The Section Title
        tk.Label(
            self.content,
            text=title,
            font=FONT_BOLD,
            bg=BG_PANEL,
            fg=TEXT_GRAY
        ).pack(anchor="w", pady=(0, 15))


class StyledButton(tk.Frame):
    """
    A custom button replacement that ensures consistent colors across OS platforms.
    Wraps a Label inside a Frame to allow full control over padding and hover effects.
    """
    def __init__(self, parent, text, command, color=BG_DARK, text_color="white", **kwargs):
        super().__init__(parent, bg=color, cursor="hand2")
        
        # Vertical gap between sibling buttons
        self.pack(fill="x", pady=6)
        self.command = command
        
        # The text label that acts as the button face
        self.lbl = tk.Label(
            self, 
            text=text, 
            bg=color, 
            fg=text_color, 
            font=FONT_BOLD, 
            pady=10  # Vertical 'height' of the button
        )
        self.lbl.pack(fill="both", expand=True)
        
        # Bind left-click to the provided command for both the frame and label
        self.bind("<Button-1>", lambda e: self.command())
        self.lbl.bind("<Button-1>", lambda e: self.command())
    