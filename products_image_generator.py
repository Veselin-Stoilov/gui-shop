import os.path
import tkinter as tk
from PIL import Image, ImageTk


def show_image(product):
    image_path = os.path.join('db', 'images', product['image'])

    image = Image.open(image_path).resize((100, 100))
    photo_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(image=photo_image)
    image_label.image = photo_image
    return image_label
