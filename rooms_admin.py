
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk  # Import ttk for the combobox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\panek\OneDrive\Υπολογιστής\LIBRARY\assets_rooms_admin\frame0")


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
    x=135.0,
    y=138.0,
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
    x=135.0,
    y=445.0,
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
    x=514.0,
    y=445.0,
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
    x=895.0,
    y=445.0,
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
    x=514.0,
    y=138.0,
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
    x=895.0,
    y=138.0,
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
    x=181.0,
    y=184.0,
    width=112.0,
    height=29.0
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
    x=562.0,
    y=184.0,
    width=114.0,
    height=29.0
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
    x=182.0,
    y=488.0,
    width=125.0,
    height=29.0
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
    x=563.0,
    y=488.0,
    width=114.0,
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
    x=945.0,
    y=184.0,
    width=118.0,
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
    x=946.0,
    y=488.0,
    width=118.0,
    height=29.0
)

canvas.create_rectangle(
    137.0,
    281.0,
    425.0,
    331.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    895.0,
    589.0,
    1183.0,
    639.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    514.0,
    589.0,
    802.0,
    639.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    135.0,
    589.0,
    423.0,
    639.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    897.0,
    281.0,
    1185.0,
    331.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    516.0,
    281.0,
    804.0,
    331.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    144.0,
    291.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    899.0,
    597.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    520.0,
    597.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    142.0,
    597.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    901.0,
    291.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    521.0,
    292.0,
    anchor="nw",
    text="Status:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    237.0,
    288.0,
    415.0,
    323.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    995.0,
    596.0,
    1173.0,
    631.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    617.0,
    596.0,
    795.0,
    631.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    238.0,
    597.0,
    416.0,
    632.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    998.0,
    288.0,
    1176.0,
    323.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    615.0,
    288.0,
    793.0,
    323.0,
    fill="#FFFFFF",
    outline="")



# Create the combobox
category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 12))
category_combobox.set("Requests")  # Default value
category_combobox.place(
    x=137.0,
    y=341.0,
    width=185.0,
    height=38.0
)


category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
category_combobox.set("Requests")  # Default value
category_combobox.place(
    x=896.0,
    y=651.0,
    width=185.0,
    height=38.0
)




category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
category_combobox.set("Requests")  # Default value
category_combobox.place(
    x=514.0,
    y=652.0,
    width=185.0,
    height=38.0
)



category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
category_combobox.set("Requests")  # Default value
category_combobox.place(
    x=135.0,
    y=652.0,
    width=185.0,
    height=38.0
)



category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
category_combobox.set("Requests")  # Default value
category_combobox.place(
    x=897.0,
    y=341.0,
    width=185.0,
    height=38.0
)


category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
category_combobox.set("Requests")  # Default value
category_combobox.place(
    x=519.0,
    y=341.0,
    width=185.0,
    height=38.0
)



button_image_31 = PhotoImage(
    file=relative_to_assets("button_31.png"))
button_31 = Button(
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_31 clicked"),
    relief="flat"
)
button_31.place(
    x=328.0,
    y=339.0,
    width=40.0,
    height=40.0
)

button_image_32 = PhotoImage(
    file=relative_to_assets("button_32.png"))
button_32 = Button(
    image=button_image_32,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_32 clicked"),
    relief="flat"
)
button_32.place(
    x=385.0,
    y=339.0,
    width=40.0,
    height=40.0
)

button_image_33 = PhotoImage(
    file=relative_to_assets("button_33.png"))
button_33 = Button(
    image=button_image_33,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_33 clicked"),
    relief="flat"
)
button_33.place(
    x=328.0,
    y=339.0,
    width=40.0,
    height=40.0
)

button_image_34 = PhotoImage(
    file=relative_to_assets("button_34.png"))
button_34 = Button(
    image=button_image_34,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_34 clicked"),
    relief="flat"
)
button_34.place(
    x=385.0,
    y=339.0,
    width=40.0,
    height=40.0
)

button_image_35 = PhotoImage(
    file=relative_to_assets("button_35.png"))
button_35 = Button(
    image=button_image_35,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_35 clicked"),
    relief="flat"
)
button_35.place(
    x=1087.0,
    y=651.0,
    width=40.0,
    height=40.0
)

button_image_36 = PhotoImage(
    file=relative_to_assets("button_36.png"))
button_36 = Button(
    image=button_image_36,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_36 clicked"),
    relief="flat"
)
button_36.place(
    x=1144.0,
    y=651.0,
    width=40.0,
    height=40.0
)

button_image_37 = PhotoImage(
    file=relative_to_assets("button_37.png"))
button_37 = Button(
    image=button_image_37,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_37 clicked"),
    relief="flat"
)
button_37.place(
    x=703.0,
    y=651.0,
    width=40.0,
    height=40.0
)

button_image_38 = PhotoImage(
    file=relative_to_assets("button_38.png"))
button_38 = Button(
    image=button_image_38,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_38 clicked"),
    relief="flat"
)
button_38.place(
    x=760.0,
    y=651.0,
    width=40.0,
    height=40.0
)

button_image_39 = PhotoImage(
    file=relative_to_assets("button_39.png"))
button_39 = Button(
    image=button_image_39,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_39 clicked"),
    relief="flat"
)
button_39.place(
    x=327.0,
    y=651.0,
    width=40.0,
    height=40.0
)

button_image_40 = PhotoImage(
    file=relative_to_assets("button_40.png"))
button_40 = Button(
    image=button_image_40,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_40 clicked"),
    relief="flat"
)
button_40.place(
    x=384.0,
    y=651.0,
    width=40.0,
    height=40.0
)

button_image_41 = PhotoImage(
    file=relative_to_assets("button_41.png"))
button_41 = Button(
    image=button_image_41,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_41 clicked"),
    relief="flat"
)
button_41.place(
    x=1088.0,
    y=339.0,
    width=40.0,
    height=40.0
)

button_image_42 = PhotoImage(
    file=relative_to_assets("button_42.png"))
button_42 = Button(
    image=button_image_42,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_42 clicked"),
    relief="flat"
)
button_42.place(
    x=1145.0,
    y=339.0,
    width=40.0,
    height=40.0
)

button_image_43 = PhotoImage(
    file=relative_to_assets("button_43.png"))
button_43 = Button(
    image=button_image_43,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_43 clicked"),
    relief="flat"
)
button_43.place(
    x=710.0,
    y=340.0,
    width=40.0,
    height=40.0
)

button_image_44 = PhotoImage(
    file=relative_to_assets("button_44.png"))
button_44 = Button(
    image=button_image_44,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_44 clicked"),
    relief="flat"
)
button_44.place(
    x=761.0,
    y=339.0,
    width=40.0,
    height=40.0
)

button_image_45 = PhotoImage(
    file=relative_to_assets("button_45.png"))
button_45 = Button(
    image=button_image_45,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_45 clicked"),
    relief="flat"
)
button_45.place(
    x=724.0,
    y=354.0,
    width=12.0,
    height=12.0
)

button_image_46 = PhotoImage(
    file=relative_to_assets("button_46.png"))
button_46 = Button(
    image=button_image_46,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_46 clicked"),
    relief="flat"
)
button_46.place(
    x=1158.0,
    y=663.0,
    width=12.0,
    height=12.0
)

button_image_47 = PhotoImage(
    file=relative_to_assets("button_47.png"))
button_47 = Button(
    image=button_image_47,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_47 clicked"),
    relief="flat"
)
button_47.place(
    x=342.0,
    y=664.0,
    width=12.0,
    height=12.0
)

button_image_48 = PhotoImage(
    file=relative_to_assets("button_48.png"))
button_48 = Button(
    image=button_image_48,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_48 clicked"),
    relief="flat"
)
button_48.place(
    x=397.0,
    y=352.0,
    width=12.0,
    height=12.0
)

button_image_49 = PhotoImage(
    file=relative_to_assets("button_49.png"))
button_49 = Button(
    image=button_image_49,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_49 clicked"),
    relief="flat"
)
button_49.place(
    x=396.0,
    y=663.0,
    width=12.0,
    height=12.0
)

button_image_50 = PhotoImage(
    file=relative_to_assets("button_50.png"))
button_50 = Button(
    image=button_image_50,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_50 clicked"),
    relief="flat"
)
button_50.place(
    x=1159.0,
    y=352.0,
    width=12.0,
    height=12.0
)

button_image_51 = PhotoImage(
    file=relative_to_assets("button_51.png"))
button_51 = Button(
    image=button_image_51,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_51 clicked"),
    relief="flat"
)
button_51.place(
    x=1104.0,
    y=664.0,
    width=12.0,
    height=12.0
)

button_image_52 = PhotoImage(
    file=relative_to_assets("button_52.png"))
button_52 = Button(
    image=button_image_52,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_52 clicked"),
    relief="flat"
)
button_52.place(
    x=343.0,
    y=354.0,
    width=12.0,
    height=12.0
)

button_image_53 = PhotoImage(
    file=relative_to_assets("button_53.png"))
button_53 = Button(
    image=button_image_53,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_53 clicked"),
    relief="flat"
)
button_53.place(
    x=1105.0,
    y=354.0,
    width=12.0,
    height=12.0
)

button_image_54 = PhotoImage(
    file=relative_to_assets("button_54.png"))
button_54 = Button(
    image=button_image_54,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_54 clicked"),
    relief="flat"
)
button_54.place(
    x=773.0,
    y=664.0,
    width=12.0,
    height=12.0
)

button_image_55 = PhotoImage(
    file=relative_to_assets("button_55.png"))
button_55 = Button(
    image=button_image_55,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_55 clicked"),
    relief="flat"
)
button_55.place(
    x=775.0,
    y=353.0,
    width=12.0,
    height=12.0
)

button_image_56 = PhotoImage(
    file=relative_to_assets("button_56.png"))
button_56 = Button(
    image=button_image_56,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_56 clicked"),
    relief="flat"
)
button_56.place(
    x=717.0,
    y=664.0,
    width=12.0,
    height=12.0
)

button_image_57 = PhotoImage(
    file=relative_to_assets("button_57.png"))
button_57 = Button(
    image=button_image_57,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_57 clicked"),
    relief="flat"
)
button_57.place(
    x=340.0,
    y=155.0,
    width=83.0,
    height=90.0
)

button_image_58 = PhotoImage(
    file=relative_to_assets("button_58.png"))
button_58 = Button(
    image=button_image_58,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_58 clicked"),
    relief="flat"
)
button_58.place(
    x=1105.0,
    y=469.0,
    width=83.0,
    height=90.0
)

button_image_59 = PhotoImage(
    file=relative_to_assets("button_59.png"))
button_59 = Button(
    image=button_image_59,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_59 clicked"),
    relief="flat"
)
button_59.place(
    x=720.0,
    y=469.0,
    width=83.0,
    height=90.0
)

button_image_60 = PhotoImage(
    file=relative_to_assets("button_60.png"))
button_60 = Button(
    image=button_image_60,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_60 clicked"),
    relief="flat"
)
button_60.place(
    x=340.0,
    y=469.0,
    width=83.0,
    height=90.0
)

button_image_61 = PhotoImage(
    file=relative_to_assets("button_61.png"))
button_61 = Button(
    image=button_image_61,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_61 clicked"),
    relief="flat"
)
button_61.place(
    x=1104.0,
    y=155.0,
    width=83.0,
    height=90.0
)

button_image_62 = PhotoImage(
    file=relative_to_assets("button_62.png"))
button_62 = Button(
    image=button_image_62,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_62 clicked"),
    relief="flat"
)
button_62.place(
    x=720.0,
    y=154.0,
    width=83.0,
    height=90.0
)

button_image_63 = PhotoImage(
    file=relative_to_assets("button_63.png"))
button_63 = Button(
    image=button_image_63,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_63 clicked"),
    relief="flat"
)
button_63.place(
    x=352.0,
    y=178.0,
    width=62.0,
    height=45.0
)

button_image_64 = PhotoImage(
    file=relative_to_assets("button_64.png"))
button_64 = Button(
    image=button_image_64,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_64 clicked"),
    relief="flat"
)
button_64.place(
    x=735.0,
    y=178.0,
    width=62.0,
    height=45.0
)

button_image_65 = PhotoImage(
    file=relative_to_assets("button_65.png"))
button_65 = Button(
    image=button_image_65,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_65 clicked"),
    relief="flat"
)
button_65.place(
    x=1117.0,
    y=176.0,
    width=62.0,
    height=45.0
)

button_image_66 = PhotoImage(
    file=relative_to_assets("button_66.png"))
button_66 = Button(
    image=button_image_66,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_66 clicked"),
    relief="flat"
)
button_66.place(
    x=1118.0,
    y=488.0,
    width=61.0,
    height=45.0
)

button_image_67 = PhotoImage(
    file=relative_to_assets("button_67.png"))
button_67 = Button(
    image=button_image_67,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_67 clicked"),
    relief="flat"
)
button_67.place(
    x=354.0,
    y=488.0,
    width=61.0,
    height=45.0
)

button_image_68 = PhotoImage(
    file=relative_to_assets("button_68.png"))
button_68 = Button(
    image=button_image_68,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_68 clicked"),
    relief="flat"
)
button_68.place(
    x=733.0,
    y=492.0,
    width=61.0,
    height=45.0
)
window.resizable(False, False)
window.mainloop()
