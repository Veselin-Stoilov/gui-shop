import tkinter as tk
from screens import render_main_screen


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("800x600")
    window.title('GUI Shop')
    render_main_screen(window)
    window.mainloop()

