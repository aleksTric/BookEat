
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk  # Import ttk for the combobox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\panek\OneDrive\Υπολογιστής\LIBRARY\assets_room_form\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1237x856")
window.configure(bg = "#FFFFFF")

# Define the categories for the combobox
categories = ["Category 1", "Category 2", "Category 3", "Category 4"]
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
    107.0,
    4.0,
    anchor="nw",
    text="Room form",
    fill="#333333",
    font=("Inter", 30 * -1)
)

canvas.create_rectangle(
    193.0,
    50.0,
    1161.0,
    844.0,
    fill="#333333",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    687.5,
    169.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=674.0,
    y=139.0,
    width=27.0,
    height=59.0
)

canvas.create_rectangle(
    247.0,
    61.0,
    1131.0,
    129.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    234.0,
    232.0,
    1118.0,
    297.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    487.0,
    627.0,
    767.0,
    688.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    457.0,
    81.0,
    anchor="nw",
    text="Enter the number of members",
    fill="#000000",
    font=("Inter Medium", 24 * -1)
)

canvas.create_text(
    516.0,
    253.0,
    anchor="nw",
    text="Enter the equipment",
    fill="#000000",
    font=("Inter Medium", 24 * -1)
)

canvas.create_text(
    593.0,
    643.0,
    anchor="nw",
    text="Timer",
    fill="#000000",
    font=("Inter Medium", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    826.5,
    656.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=813.0,
    y=626.0,
    width=27.0,
    height=59.0
)

canvas.create_text(
    867.0,
    643.0,
    anchor="nw",
    text="h",
    fill="#FFFFFF",
    font=("Inter Medium", 24 * -1)
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
    x=431.000006821707,
    y=744.0,
    width=471.28728784880315,
    height=65.91875249229338
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
    x=623.0,
    y=758.0,
    width=83.0,
    height=29.0
)

# Create the combobox
category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
category_combobox.set("Select announcement")  # Default value
category_combobox.place(
     x=549.0,
    y=320.0,
    width=255.0,
    height=50.0
)

# Create the combobox
category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
category_combobox.set("Select announcement")  # Default value
category_combobox.place(
    x=259.0,
    y=320.0,
    width=243.0,
    height=50.0
)

# Create the combobox
category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
category_combobox.set("Select announcement")  # Default value
category_combobox.place(
    x=854.0,
    y=320.0,
    width=231.0,
    height=50.0
)



window.resizable(False, False)
window.mainloop()
