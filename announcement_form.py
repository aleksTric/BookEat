from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\panek\OneDrive\Υπολογιστής\LIBRARY\assets_announcement_form\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def create_entry_with_placeholder(x, y, width, height, placeholder):
    entry = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry.place(x=x, y=y, width=width, height=height)
    
    placeholder_label = Label(
        window,
        text=placeholder,
        fg="#999999",
        bg="#FFFFFF"
    )
    placeholder_label.place(x=x + 5, y=y + 3)  # Προσαρμογή του πλαισίου του Label
    
    # Όταν το κουτί κειμένου έχει κείμενο, το Label αποκρύπτεται
    entry.bind("<FocusIn>", lambda event: placeholder_label.place_forget())
    entry.bind("<FocusOut>", lambda event: placeholder_label.place(x=x + 5, y=y + 3) if not entry.get() else None)
    
    return entry

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
    39.0,
    0.0,
    anchor="nw",
    text="Announcement Form",
    fill="#333333",
    font=("Italiana Regular", 40 * -1)
)

canvas.create_rectangle(
    92.0,
    53.0,
    1039.0,
    837.0,
    fill="#333333",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    565.5,
    105.5,
    image=entry_image_1
)
entry_1 = create_entry_with_placeholder(
    x=136.0,
    y=73.0,
    width=859.0,
    height=63.0,
    placeholder="Enter title"
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    268.0,
    187.5,
    image=entry_image_2
)
entry_2 = create_entry_with_placeholder(
     x=186.0,
    y=157.0,
    width=164.0,
    height=59.0,
    placeholder="month"
)


entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    497.5,
    187.5,
    image=entry_image_3
)
entry_3 = create_entry_with_placeholder(
    x=419.0,
    y=157.0,
    width=157.0,
    height=59.0,
    placeholder="day"
)


entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    698.5,
    189.5,
    image=entry_image_4
)
entry_4 = create_entry_with_placeholder(
    x=639.0,
    y=157.0,
    width=119.0,
    height=63.0,
    placeholder="year"
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    961.0,
    191.5,
    image=entry_image_5
)
entry_5 = create_entry_with_placeholder(
    x=938.0,
    y=161.0,
    width=46.0,
    height=59.0,
    placeholder="minutes"
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    843.0,
    191.5,
    image=entry_image_6
)
entry_6 = create_entry_with_placeholder(
    x=820.0,
    y=161.0,
    width=46.0,
    height=59.0,
    placeholder="hour"
)

canvas.create_rectangle(
    218.0,
    681.0,
    809.0,
    743.0,
    fill="#D9D9D9",
    outline="")

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    565.5,
    347.0,
    image=entry_image_7
)
entry_7 = create_entry_with_placeholder(
    x=133.0,
    y=268.0,
    width=865.0,
    height=156.0,
    placeholder="Enter your text"
)


entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    565.5,
    547.0,
    image=entry_image_8
)
entry_8 = create_entry_with_placeholder(
    x=133.0,
    y=445.0,
    width=865.0,
    height=202.0,
    placeholder="Enter the location of the event"
)

canvas.create_text(
    249.0,
    692.0,
    anchor="nw",
    text="Available Seats",
    fill="#000000",
    font=("Italiana Regular", 35 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    899.0,
    718.0,
    image=entry_image_9
)
entry_9 = create_entry_with_placeholder(
    x=847.0,
    y=677.0,
    width=104.0,
    height=80.0,
    placeholder="number of seats"
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
    x=313.0,
    y=768.0,
    width=477.0,
    height=62.0
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
    x=481.0,
    y=769.0,
    width=169.0,
    height=61.0
)

canvas.create_text(
    895.0,
    158.0,
    anchor="nw",
    text=":",
    fill="#000000",
    font=("Inter Medium", 50 * -1)
)
window.resizable(False, False)
window.mainloop()