import tkinter as tk
from tkinter import filedialog, messagebox

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSUF Maze Solver Project")
        self.root.geometry("800x600") 
        self.label = tk.Label(self.root, text="Welcome to the Maze Solver", font=("Arial", 14))
        self.label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()