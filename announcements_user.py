import mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk

# Define the paths
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\panek\OneDrive\Υπολογιστής\LIBRARY\assets_announcements_user\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Database connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bookeat"
    )

class Announcements:

    def __init__(self, title, date_of_the_event, interested_users, available_seats):
        self.__title = title
        self.__date_of_the_event = date_of_the_event
        self.__interested_users = interested_users
        self.__available_seats = available_seats


    def get_events():
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM announcements")
        events = cursor.fetchall()
        conn.close()
        return [event[0] for event in events]

    def get_event_details(event_title):
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.date_hour, e.available_seats, e.interested_users, a.texting
            FROM announcements a
            JOIN event e ON a.announcement_id = e.event_id
            WHERE a.title = %s
        """, (event_title,))
        event_details = cursor.fetchone()
        conn.close()
        return event_details

    def update_event_details(event_title):
        details = get_event_details(event_title)
        if details:
            date_hour, available_seats, interested_users, texting = details
            canvas.itemconfig(date_label, text=date_hour.strftime("%Y-%m-%d %H:%M:%S"))
            canvas.itemconfig(seats_label, text=available_seats)
            canvas.itemconfig(users_label, text=interested_users)
            canvas.itemconfig(texting_label, text=texting)

    # Initialize the window
    window = Tk()
    window.geometry("1237x856")
    window.configure(bg="#FFFFFF")

    # Create a canvas
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=856,
        width=1237,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_text(
        61.0,
        53.0,
        anchor="nw",
        text="Announcements",
        fill="#000000",
        font=("Inter Bold", 18)
    )
    canvas.create_rectangle(
        61.0,
        137.0,
        610.0,
        189.0,
        fill="#D9D9D9",
        outline=""
    )

    # Create the combobox
    categories = get_events()
    category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 14))
    category_combobox.set("Select announcement")
    category_combobox.place(
        x=69.0,
        y=146.0,
        width=440.0,
        height=28.0
    )

    # Define a callback for when an event is selected
    category_combobox.bind("<<ComboboxSelected>>", lambda e: update_event_details(category_combobox.get()))

    canvas.create_text(
        69.0,
        146.0,
        anchor="nw",
        text="Select announcement",
        fill="#000000",
        font=("Inter", 18)
    )

    # Continue with the rest of the GUI components
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=494.0,
        y=670.0,
        width=275.0,
        height=58.0
    )

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=582.0,
        y=678.0,
        width=100.0,
        height=41.0
    )

    canvas.create_rectangle(
        61.0,
        575.0,
        411.0,
        625.0,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_text(
        68.0,
        582.0,
        anchor="nw",
        text="Ιnterested users:",
        fill="#000000",
        font=("Inter", 18)
    )

    canvas.create_rectangle(
        299.0,
        582.0,
        399.0,
        617.0,
        fill="#FFFFFF",
        outline=""
    )
    users_label = canvas.create_text(
        310.0,
        582.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 18)
    )

    canvas.create_rectangle(
        442.0,
        575.0,
        792.0,
        625.0,
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_text(
        449.0,
        582.0,
        anchor="nw",
        text="Available seats:",
        fill="#000000",
        font=("Inter", 18)
    )

    canvas.create_rectangle(
        680.0,
        582.0,
        780.0,
        617.0,
        fill="#FFFFFF",
        outline=""
    )
    seats_label = canvas.create_text(
        690.0,
        582.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("Inter", 18)
    )

    canvas.create_rectangle(
        813.0,  # Adjusted X coordinate for the gray rectangle
        570.0,  # Adjusted Y coordinate for the gray rectangle
        1183.0,  # Increased width of the gray rectangle
        630.0,  # Increased height of the gray rectangle
        fill="#D9D9D9",
        outline=""
    )

    canvas.create_text(
        830.0,
        582.0,
        anchor="nw",
        text="Date of the event:",
        fill="#000000",
        font=("Inter", 18)
    )

    canvas.create_rectangle(
        1045.0,  # Adjusted X coordinate for the white rectangle
        582.0,
        1175.0,  # Adjusted width of the white rectangle
        617.0,
        fill="#FFFFFF",
        outline=""
    )
    date_label = canvas.create_text(
        1055.0,  # Adjusted X coordinate
        582.0,
        anchor="nw",
        text="N/A",
        fill="#000000",
        font=("Inter", 10)  # Adjust font size to 10
    )

    # Add label for the announcement text
    canvas.create_text(
        61.0,
        210.0,
        anchor="nw",
        text="Announcement text:",
        fill="#000000",
        font=("Inter", 18)
    )

    canvas.create_rectangle(
        61.0,
        240.0,
        610.0,
        370.0,
        fill="#FFFFFF",
        outline=""
    )

    texting_label = canvas.create_text(
        69.0,
        245.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 14),
        width=540
    )

    window.resizable(False, False)
    window.mainloop()
