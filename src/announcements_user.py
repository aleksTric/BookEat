import mysql.connector
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox
from tkinter import ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets_announcements_user/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="bookeat"
    )

class Event:
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
            61.0,
            53.0,
            anchor="nw",
            text="Announcements",
            fill="#000000",
            font=("Inter Bold", 18)
        )
        self.canvas.create_rectangle(
            61.0,
            137.0,
            610.0,
            189.0,
            fill="#D9D9D9",
            outline=""
        )

        self.categories = self.get_events()
        self.category_combobox = ttk.Combobox(window, values=self.categories, font=("Inter", 14))
        self.category_combobox.set("Select announcement")
        self.category_combobox.place(
            x=69.0,
            y=146.0,
            width=440.0,
            height=28.0
        )
        self.category_combobox.bind("<<ComboboxSelected>>", self.on_combobox_selected)

        self.canvas.create_text(
            69.0,
            146.0,
            anchor="nw",
            text="Select announcement",
            fill="#000000",
            font=("Inter", 18)
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=494.0,
            y=670.0,
            width=275.0,
            height=58.0
        )

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.submit_interest,
            relief="flat"
        )
        self.button_3.place(
            x=582.0,
            y=678.0,
            width=100.0,
            height=41.0
        )

        self.canvas.create_rectangle(
            61.0,
            575.0,
            411.0,
            625.0,
            fill="#D9D9D9",
            outline=""
        )

        self.canvas.create_text(
            68.0,
            582.0,
            anchor="nw",
            text="Ιnterested users:",
            fill="#000000",
            font=("Inter", 18)
        )

        self.canvas.create_rectangle(
            299.0,
            582.0,
            399.0,
            617.0,
            fill="#FFFFFF",
            outline=""
        )
        self.users_label = self.canvas.create_text(
            310.0,
            582.0,
            anchor="nw",
            text="0",
            fill="#000000",
            font=("Inter", 18)
        )

        self.canvas.create_rectangle(
            442.0,
            575.0,
            792.0,
            625.0,
            fill="#D9D9D9",
            outline=""
        )

        self.canvas.create_text(
            449.0,
            582.0,
            anchor="nw",
            text="Available seats:",
            fill="#000000",
            font=("Inter", 18)
        )

        self.canvas.create_rectangle(
            680.0,
            582.0,
            780.0,
            617.0,
            fill="#FFFFFF",
            outline=""
        )
        self.seats_label = self.canvas.create_text(
            690.0,
            582.0,
            anchor="nw",
            text="0",
            fill="#000000",
            font=("Inter", 18)
        )

        self.canvas.create_rectangle(
            813.0,  
            570.0,  
            1183.0,  
            630.0,  
            fill="#D9D9D9",
            outline=""
        )

        self.canvas.create_text(
            830.0,
            582.0,
            anchor="nw",
            text="Date of the event:",
            fill="#000000",
            font=("Inter", 18)
        )

        self.canvas.create_rectangle(
            1045.0,  
            582.0,
            1175.0,  
            617.0,
            fill="#FFFFFF",
            outline=""
        )
        self.date_label = self.canvas.create_text(
            1055.0, 
            582.0,
            anchor="nw",
            text="N/A",
            fill="#000000",
            font=("Inter", 10)  
        )

        self.canvas.create_text(
            61.0,
            210.0,
            anchor="nw",
            text="Announcement text:",
            fill="#000000",
            font=("Inter", 18)
        )

        self.canvas.create_rectangle(
            61.0,
            240.0,
            610.0,
            370.0,
            fill="#FFFFFF",
            outline=""
        )

        self.texting_label = self.canvas.create_text(
            69.0,
            245.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter", 14),
            width=540
        )

    def get_events(self):
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM announcements")
        events = cursor.fetchall()
        conn.close()
        return [event[0] for event in events]

    def get_event_details(self, event_title):
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

    def update_event_details(self, event_title):
        details = self.get_event_details(event_title)
        if details:
            date_hour, available_seats, interested_users, texting = details
            self.canvas.itemconfig(self.date_label, text=date_hour.strftime("%Y-%m-%d %H:%M:%S"))
            self.canvas.itemconfig(self.seats_label, text=available_seats)
            self.canvas.itemconfig(self.users_label, text=interested_users)
            self.canvas.itemconfig(self.texting_label, text=texting)

    def on_combobox_selected(self, event):
        selected_event = self.category_combobox.get()
        self.update_event_details(selected_event)

    def submit_interest(self):
        selected_event = self.category_combobox.get()
        if not selected_event:
            return

        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE event e
            JOIN announcements a ON e.event_id = a.announcement_id
            SET e.interested_users = e.interested_users + 1, 
                e.available_seats = e.available_seats - 1
            WHERE a.title = %s
        """, (selected_event,))
        conn.commit()
        conn.close()
        self.update_event_details(selected_event)
        messagebox.showinfo("Success", "Successfully registered for the event")

if __name__ == "__main__":
    window = Tk()
    app = Event(window)
    window.resizable(False, False)
    window.mainloop()
