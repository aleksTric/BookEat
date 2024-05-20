
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\panek\OneDrive\Υπολογιστής\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1237x856")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 856,
    width = 1237,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    137.0,
    40.0,
    anchor="nw",
    text="Rooms",
    fill="#000000",
    font=("Inter Bold", 30 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=137.0,
    y=136.0,
    width=206.0,
    height=128.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=137.0,
    y=469.0,
    width=206.0,
    height=128.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=516.0,
    y=469.0,
    width=206.0,
    height=128.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=897.0,
    y=469.0,
    width=206.0,
    height=128.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=516.0,
    y=136.0,
    width=206.0,
    height=128.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=897.0,
    y=136.0,
    width=206.0,
    height=128.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=186.0,
    y=182.0,
    width=109.0,
    height=28.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=564.0,
    y=182.0,
    width=113.0,
    height=28.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=183.0,
    y=512.0,
    width=125.0,
    height=37.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=564.0,
    y=512.0,
    width=113.0,
    height=29.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=947.0,
    y=182.0,
    width=116.0,
    height=29.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=947.0,
    y=512.0,
    width=116.0,
    height=37.0
)

canvas.create_rectangle(
    137.0,
    303.0,
    425.0,
    353.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    897.0,
    636.0,
    1185.0,
    686.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    516.0,
    636.0,
    804.0,
    686.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    137.0,
    636.0,
    425.0,
    686.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    897.0,
    303.0,
    1185.0,
    353.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    516.0,
    303.0,
    804.0,
    353.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    144.0,
    308.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    901.0,
    644.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    522.0,
    644.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    144.0,
    644.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    901.0,
    309.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    522.0,
    308.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    237.0,
    310.0,
    415.0,
    345.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    997.0,
    643.0,
    1175.0,
    678.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    619.0,
    643.0,
    797.0,
    678.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    240.0,
    644.0,
    418.0,
    679.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    998.0,
    310.0,
    1176.0,
    345.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    615.0,
    310.0,
    793.0,
    345.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
