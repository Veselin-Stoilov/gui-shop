import tkinter as tk


def clear_window(window: tk.Tk):
    for widget in window.winfo_children():
        widget.destroy()


def render_main_screen(window: tk.Tk):
    tk.Button(
        window,
        text='Login',
        bg='green',
        fg='white',
        command=lambda: render_login_screen(window)
    ).grid(row=0, column=0)

    tk.Button(
        window,
        text='Register',
        bg='yellow',
        fg='black',
        command=lambda: render_register_screen(window)
    ).grid(row=0, column=1)


def render_register_screen(window: tk.Tk):
    clear_window(window)

    username = tk.Entry(window)
    username.grid(row=0, column=0)

    password = tk.Entry(window, show='*')
    password.grid(row=1, column=0)

    first_name = tk.Entry(window)
    first_name.grid(row=2, column=0)

    last_name = tk.Entry(window)
    last_name.grid(row=3, column=0)

    tk.Button(
        window,
        text='Register',
        bg='green',
        fg='black',
        command=lambda: print(username.get(), password.get())
    ).grid(row=4, column=0)


def render_login_screen(window: tk.Tk):
    clear_window(window)
