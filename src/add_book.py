
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\lessons\BookEat\src\assets\add_book\frame0")


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
canvas.create_rectangle(
    0.0,
    0.0,
    1454.0,
    856.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    59.0,
    23.0,
    1136.0,
    844.0,
    fill="#FFFFFF",
    outline="")

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
    x=173.0,
    y=157.0,
    width=324.0,
    height=44.0
)

canvas.create_text(
    230.0,
    212.0,
    anchor="nw",
    text="JSON",
    fill="#333333",
    font=("Inter Light", 15 * -1)
)

canvas.create_rectangle(
    204.0,
    212.0,
    219.0,
    227.0,
    fill="#9B9B9B",
    outline="")

canvas.create_rectangle(
    152.0,
    237.0,
    1082.0,
    822.0,
    fill="#D9D9D9",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    633.0,
    276.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    614.0,
    504.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_1.place(
    x=175.0,
    y=481.0,
    width=878.0,
    height=45.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    617.0,
    421.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_2.place(
    x=178.0,
    y=398.0,
    width=878.0,
    height=45.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    617.0,
    335.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)
entry_3.place(
    x=178.0,
    y=312.0,
    width=878.0,
    height=45.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    613.5,
    599.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 20)
)

entry_4.place(
    x=175.0,
    y=576.0,
    width=877.0,
    height=45.0
)

canvas.create_text(
    174.0,
    280.0,
    anchor="nw",
    text=" Title",
    fill="#333333",
    font=("Inter Light", 30 * -1)
)

canvas.create_text(
    180.0,
    360.0,
    anchor="nw",
    text="Category",
    fill="#333333",
    font=("Inter Light", 30 * -1)
)

canvas.create_text(
    180.0,
    445.0,
    anchor="nw",
    text="Author",
    fill="#333333",
    font=("Inter Light", 30 * -1)
)

canvas.create_text(
    174.0,
    539.0,
    anchor="nw",
    text=" Date",
    fill="#333333",
    font=("Inter Light", 30 * -1)
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
    x=509.0,
    y=671.0,
    width=248.0,
    height=90.0
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
    x=746.0,
    y=157.0,
    width=329.0,
    height=59.0
)

canvas.create_text(
    195.0,
    69.0,
    anchor="nw",
    text="file :",
    fill="#000000",
    font=("Inter", 24 * -1)
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
    x=173.0,
    y=100.0,
    width=150.0,
    height=34.0
)

canvas.create_rectangle(
    777.0,
    88.0,
    1051.0,
    143.0,
    fill="#D9D9D9",
    outline="")

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    914.5,
    116.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_5.place(
    x=791.0,
    y=98.0,
    width=247.0,
    height=34.0
)

canvas.create_text(
    786.0,
    48.0,
    anchor="nw",
    text="category:",
    fill="#333333",
    font=("Inter Light", 32 * -1)
)
window.resizable(False, False)
window.mainloop()