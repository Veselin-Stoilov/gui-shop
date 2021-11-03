import tkinter as tk
import json
from screens import render_main_screen


if __name__ == '__main__':

    obj = {
        'username': 'vesso100',
        'password': '9281',
        'firstName': 'Veselin',
        'lastName': 'Stoilov',
    }
    print(json.dumps(obj))
    print(type(json.loads((json.dumps(obj)))))
    window = tk.Tk()
    window.geometry("800x600")
    window.title('GUI Shop')
    render_main_screen(window)
    window.mainloop()

