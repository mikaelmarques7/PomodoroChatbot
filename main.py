import tkinter as tk
from interface import PomodoroApp


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()