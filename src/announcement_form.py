from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, messagebox
import mysql.connector
from mysql.connector import Error

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\panek\OneDrive\Υπολογιστής\LIBRARY\assets_announcement_form\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Announcements:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1237x856")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=856,
            width=1237,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            39.0,
            0.0,
            anchor="nw",
            text="Announcement Form",
            fill="#333333",
            font=("Italiana Regular", 40 * -1)
        )
        self.canvas.create_rectangle(
            92.0,
            53.0,
            1039.0,
            837.0,
            fill="#333333",
            outline=""
        )

        self.entry_1 = self.create_entry_with_placeholder(136.0, 73.0, 859.0, 63.0, "Enter title")
        self.entry_2 = self.create_entry_with_placeholder(186.0, 157.0, 164.0, 59.0, "month")
        self.entry_3 = self.create_entry_with_placeholder(419.0, 157.0, 157.0, 59.0, "day")
        self.entry_4 = self.create_entry_with_placeholder(639.0, 157.0, 119.0, 63.0, "year")
        self.entry_5 = self.create_entry_with_placeholder(938.0, 161.0, 46.0, 59.0, "minutes")
        self.entry_6 = self.create_entry_with_placeholder(820.0, 161.0, 46.0, 59.0, "hour")
        self.entry_7 = self.create_entry_with_placeholder(133.0, 268.0, 865.0, 156.0, "Enter your text")
        self.entry_8 = self.create_entry_with_placeholder(133.0, 445.0, 865.0, 202.0, "Enter the location of the event")
        self.entry_9 = self.create_entry_with_placeholder(847.0, 677.0, 104.0, 80.0, "number of seats")

        self.button_1 = self.create_button(313.0, 768.0, 477.0, 62.0, self.insert_announcement_data)
        self.button_2 = self.create_button(481.0, 769.0, 169.0, 61.0, self.insert_announcement_data)  # Changed command to insert_announcement_data

        self.canvas.create_text(
            895.0,
            158.0,
            anchor="nw",
            text=":",
            fill="#000000",
            font=("Inter Medium", 50 * -1)
        )

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='bookeat',
                user='root',
                password='root'
            )
            if connection.is_connected():
                print("Connected to MySQL database")
            return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def create_entry_with_placeholder(self, x, y, width, height, placeholder):
        entry = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry.place(x=x, y=y, width=width, height=height)

        placeholder_label = Label(
            self.window,
            text=placeholder,
            fg="#999999",
            bg="#FFFFFF"
        )
        placeholder_label.place(x=x + 5, y=y + 3)
        entry.bind("<FocusIn>", lambda event: placeholder_label.place_forget())
        entry.bind("<FocusOut>", lambda event: placeholder_label.place(x=x + 5, y=y + 3) if not entry.get() else None)

        return entry

    def create_button(self, x, y, width, height, command):
        button = Button(
            self.window,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat",
            text="Create",
            bg="#FFFFFF"
        )
        button.place(x=x, y=y, width=width, height=height)
        return button

    def insert_announcement_data(self):
        print("insert_announcement_data called")
        connection = self.connect_to_db()
        if connection is None:
            messagebox.showerror("Error", "Failed to connect to the database")
            return

        title = self.entry_1.get()
        month = self.entry_2.get()
        day = self.entry_3.get()
        year = self.entry_4.get()
        hour = self.entry_6.get()
        minutes = self.entry_5.get()
        texting = self.entry_7.get()
        location = self.entry_8.get()
        available_seats = self.entry_9.get()

        date_hour = f"{year}-{month}-{day} {hour}:{minutes}:00"

        print(f"Inserting: title={title}, texting={texting}, date_hour={date_hour}, location={location}, available_seats={available_seats}")

        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO announcements (title, texting) VALUES (%s, %s)",
                (title, texting)
            )
            announcement_id = cursor.lastrowid
            print(f"Announcement ID: {announcement_id}")

            cursor.execute(
                "INSERT INTO event (event_id, date_hour, location, available_seats, interested_users) VALUES (%s, %s, %s, %s, %s)",
                (announcement_id, date_hour, location, available_seats, 0)
            )

            connection.commit()
            messagebox.showinfo("Success", "Announcement data inserted successfully")
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", "Failed to insert data into the database: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


window = Tk()
announcements = Announcements(window)
window.resizable(False, False)
window.mainloop()
