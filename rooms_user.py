from pathlib import Path
import mysql.connector
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\panek\OneDrive\Υπολογιστής\LIBRARY\assets_rooms_user\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bookeat"
    )

class Rooms:

    def get_rooms():
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT room_name, status FROM rooms")
        rooms_data = cursor.fetchall()
        conn.close()
        return rooms_data

    def check_status(status):
        if status == "Available":
            subprocess.run(["python", "room_form.py"])
        else:
            messagebox.showinfo("Room Not Available", "This room is not available.")

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

    # Define rectangles for rooms and statuses
    room_rectangles = [
        (137.0, 136.0, 425.0, 264.0),
        (516.0, 136.0, 799.0, 264.0),
        (897.0, 136.0, 1180.0, 264.0),
        (137.0, 469.0, 425.0, 597.0),
        (516.0, 469.0, 799.0, 597.0),
        (897.0, 469.0, 1180.0, 597.0)
    ]

    status_rectangles = [
        (137.0, 303.0, 425.0, 353.0),
        (516.0, 303.0, 804.0, 353.0),
        (897.0, 303.0, 1185.0, 353.0),
        (137.0, 636.0, 425.0, 686.0),
        (516.0, 636.0, 804.0, 686.0),
        (897.0, 636.0, 1185.0, 686.0)
    ]

    # Draw rectangles for rooms
    for (x1, y1, x2, y2) in room_rectangles:
        canvas.create_rectangle(x1, y1, x2, y2, fill="#D9D9D9", outline="")

    # Draw rectangles for statuses
    for (x1, y1, x2, y2) in status_rectangles:
        canvas.create_rectangle(x1, y1, x2, y2, fill="#D9D9D9", outline="")

    # Create status labels
    status_labels = [
        (144.0, 308.0),
        (522.0, 308.0),
        (901.0, 309.0),
        (144.0, 644.0),
        (522.0, 644.0),
        (901.0, 644.0)
    ]

    for (x, y) in status_labels:
        canvas.create_text(x, y, anchor="nw", text="Status:", fill="#000000", font=("Inter Bold", 24 * -1))

    # Fetch room data
    room_data = get_rooms()

    # Define positions for room names and statuses
    room_name_positions = [
        (161.0, 154.0),
        (542.0, 154.0),
        (923.0, 154.0),
        (161.0, 491.0),
        (542.0, 491.0),
        (923.0, 491.0)
    ]

    status_value_positions = [
        (237.0, 310.0, 415.0, 345.0),
        (615.0, 310.0, 793.0, 345.0),
        (998.0, 310.0, 1176.0, 345.0),
        (240.0, 644.0, 418.0, 679.0),
        (619.0, 643.0, 797.0, 678.0),
        (997.0, 643.0, 1175.0, 678.0)
    ]

    # Define button positions
    button_positions = [
        (192, 206),
        (571, 206),
        (951, 206),
        (192, 539),
        (571, 539),
        (951, 539)
    ]

    # Display room names and statuses
    for i, (room_name, status) in enumerate(room_data):
        if i < 6:  # Limit to 6 rooms
            room_name_x, room_name_y = room_name_positions[i]
            status_x1, status_y1, status_x2, status_y2 = status_value_positions[i]
            button_x, button_y = button_positions[i]
            
            canvas.create_text(
                room_name_x,
                room_name_y,
                anchor="nw",
                text=room_name,
                fill="#000000",
                font=("Inter Bold", 16)
            )
            
            canvas.create_rectangle(
                status_x1,
                status_y1,
                status_x2,
                status_y2,
                fill="#FFFFFF",
                outline=""
            )
            
            canvas.create_text(
                status_x1 + 10,  # Add a bit of padding from the left
                status_y1,
                anchor="nw",
                text=status,
                fill="#000000",
                font=("Inter Bold", 16)
            )
            
            # Create buttons
            button_image = PhotoImage(file=relative_to_assets("button_{}.png".format(i+1)))
            button = Button(
                image=button_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda s=status: check_status(s),
                relief="flat"
            )
            button.image = button_image  # Keep a reference to avoid garbage collection
            button.place(x=button_x, y=button_y, width=200, height=30)

    window.resizable(False, False)
    window.mainloop()
