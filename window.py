from tkinter import *
from tkinter import messagebox
import tkinter as Tk

from drowsiness import *


def boardpage():
    window = Tk.Toplevel()

    window.geometry("1920x1080")
    window.configure(bg = "#222222")
    canvas = Canvas(
        window,
        bg = "#222222",
        height = 1080,
        width = 1920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(window,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = print('hello'),
        relief = "flat")

    b0.place(
        x = 1096, y = 827,
        width = 163,
        height = 62)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(window,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = eyetest,
        relief = "flat")

    b1.place(
        x = 880, y = 824,
        width = 177,
        height = 62)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        927.0, 475.0,
        image=background_img)

    window.resizable(False, False)
    window.mainloop()
