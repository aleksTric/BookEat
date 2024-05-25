import mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter import ttk  

# Define the paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\panek\OneDrive\Υπολογιστής\LIBRARY\assets_room_form\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bookeat"
    )

class Room_form:


    def __init__(self, equipment_name, timer, members):
        self.__equipment_name = equipment_name
        self.__timer = timer
        self.__members = members

    def update_database(members, timer):
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE room SET members = %s, timer = %s", (members, timer))
        conn.commit()
        conn.close()

    def get_equipment():
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT equipment_name FROM equipment")
        equipment = cursor.fetchall()
        conn.close()
        return [item[0] for item in equipment]

    def insert_room(room_name, members, timer):
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rooms (room_name, members, timer, status) VALUES (%s, %s, %s, %s)",
                    (room_name, members, timer, 'Available'))
        conn.commit()
        conn.close()

    def check_parameters(room_name, members, timer):
        if members < 5:
            if 1 <= timer <= 3:
                return True, ""
            else:
                return False, "Error in timer. Timer must be between 1 and 3."
        else:
            return False, "Error in members. Members must be less than 5."

    def send_message():
        room_name = entry_1.get()
        members = int(entry_2.get())
        timer = int(entry_3.get())
        valid, message = check_parameters(room_name, members, timer)
        if valid:
            insert_room(room_name, members, timer)
            messagebox.showinfo("Success", "Room created successfully!")
        else:
            messagebox.showerror("Error", message)

    
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

    equipment_combobox = ttk.Combobox(window, values=get_equipment(), font=("Inter", 14))
    equipment_combobox.set("Select equipment")  # Default value
    equipment_combobox.place(
        x=549.0,
        y=320.0,
        width=255.0,
        height=50.0
    )

    category_combobox = ttk.Combobox(window, values=get_equipment(), font=("Inter", 14))
    category_combobox.set("Select equipment")  # Default value
    category_combobox.place(
        x=259.0,
        y=320.0,
        width=243.0,
        height=50.0
    )

    category_combobox = ttk.Combobox(window, values=get_equipment(), font=("Inter", 14))
    category_combobox.set("Select equipment")  # Default value
    category_combobox.place(
        x=854.0,
        y=320.0,
        width=231.0,
        height=50.0
    )

    create_button = Button(
        text="Create",
        command=send_message  
    )
    create_button.place(x=500, y=800) 

    window.resizable(False, False)
    window.mainloop()
