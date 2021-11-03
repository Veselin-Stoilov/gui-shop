import tkinter as tk

from authentication_service import register


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

    tk.Label(window, text='Username').grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text='Password').grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    tk.Label(window, text='First Name').grid(row=2, column=0)
    first_name = tk.Entry(window)
    first_name.grid(row=2, column=1)

    tk.Label(window, text='Last Name').grid(row=3, column=0)
    last_name = tk.Entry(window)
    last_name.grid(row=3, column=1)

    def on_register():
        result = register(
            username.get(),
            password.get(),
            first_name.get(),
            last_name.get()
        )
        if result:
            render_login_screen(window)
        else:
            tk.Label(window, text='Username has been already registered!', fg='red').grid(row=0, column=2)

    tk.Button(
        window,
        text='Register',
        bg='green',
        fg='black',
        command=lambda: on_register()
    ).grid(row=4, column=1)


def render_login_screen(window: tk.Tk):
    clear_window(window)
