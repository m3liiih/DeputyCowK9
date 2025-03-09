
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("720x450")
window.configure(bg = "#626262")


canvas = Canvas(
    window,
    bg = "#626262",
    height = 450,
    width = 720,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    bg="#626262",
    activebackground="#626262",
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=310.0,
    y=274.0,
    width=100.0,
    height=150.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    bg="#626262",
    activebackground="#626262",
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=409.9999694824219,
    y=279.0,
    width=135.41543579101562,
    height=170.77076721191406
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    bg="#626262",
    activebackground="#626262",
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=175.00001525878906,
    y=279.0,
    width=135.41543579101562,
    height=170.77078247070312
)

canvas.create_rectangle(
    0.0,
    0.0,
    720.0,
    61.0,
    fill="#363636",
    outline="")

canvas.create_rectangle(
    144.0,
    16.0,
    575.0,
    46.0,
    fill="#363636",
    outline="")

canvas.create_rectangle(
    144.0,
    16.0,
    575.0,
    46.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    146.0,
    20.0,
    anchor="nw",
    text="K-9 bites Cow, Deputy Tases K-9, Cow kicks Deputy",
    fill="#000000",
    font=("Small Fonts", 18 * -1)
)

canvas.create_rectangle(
    12.0,
    10.0,
    127.0,
    50.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    18.0,
    13.0,
    anchor="nw",
    text="Player",
    fill="#000000",
    font=("Small Fonts", 13 * -1)
)

canvas.create_rectangle(
    592.0,
    10.0,
    707.0,
    50.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    598.0,
    13.0,
    anchor="nw",
    text="Computer",
    fill="#000000",
    font=("Small Fonts", 13 * -1)
)
window.resizable(False, False)
window.mainloop()
