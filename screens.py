import tkinter as tk


def render_main_screen(window):
    login_button = tk.Button(
        window,
        text='Login',
        bg='green',
        fg='white',
        command=lambda: print('Login clicked'))

    register_button = tk.Button(
        window,
        text='Register',
        bg='yellow',
        fg='black',
        command=lambda: print('reg clicked'))

    login_button.grid(row=0, column=0)
    register_button.grid(row=0, column=1)