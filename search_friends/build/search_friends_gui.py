
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import mysql.connector
from tkinter import messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Aleks\Desktop\Tkinter-Designer-master\search_friends\build\assets\frame0")

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "abbe8ccf9d",
            database = "bookeat"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error",f"Failed to connect to database: {err}")
        return None
    

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def retrieve_data(text_item1,text_item2):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM account")

            rows = cursor.fetchall()

            for i, row in enumerate(rows):
                if i<3:
                   canvas.itemconfig(text_item1[i], text=rows[i])
                elif i>=3 and i<6:
                   canvas.itemconfig(text_item2[i-3],text=rows[i])
            
            cursor.close()
            conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to retrieve data: {err}")


def send_friend_req(conn):
    try:
        cursor=conn.cursor()
        cursor.execute("SELECT user_id FROM account WHERE username=aleks")
        sql = "INSERT INTO notifications VALUES ()"
        #cursor.execute(sql,data)
        conn.commit()
        messagebox.showinfo("Success","Data inserted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error",f"Failed to insert data: {err}")

def on_key_release(event):
    search_term = search_entry.get()
    search(search_term, text_items_row1, text_items_row2)  
 
def search(search_term, text_item1, text_item2):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()

            query = "SELECT username FROM account WHERE username LIKE %s"
            cursor.execute(query, ('%' + search_term + '%',))
            rows = cursor.fetchall()
           
            for i in range(3):
                canvas.itemconfig(text_item1[i], text="")
                canvas.itemconfig(text_item2[i], text="")
            
            for i,row in enumerate(rows):
                if i<3:
                    canvas.itemconfig(text_item1[i], text=rows[i])
                elif i>=3 and i<6:
                    canvas.itemconfig(text_item2[i-3], text=rows[i])
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Failed to retrieve data: {err}")



#main application window
window = tk.Tk()

conn = connect_to_database()

window.geometry("1237x856")
window.configure(bg = "#FFFFFF")

label = tk.Label(window, text="Search:")
label.pack()

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
    1237.0,
    856.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    83.0,
    856.0,
    fill="#7B3BE3",
    outline="")

canvas.create_text(
    99.0,
    22.0,
    anchor="nw",
    text=" Friends ",
    fill="#333333",
    font=("Inter Thin", 30 * -1)
)

canvas.create_rectangle(
    200.0,
    139.0,
    1149.0,
    802.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    845.0,
    11.0,
    1205.0,
    111.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    585.0,
    45.0,
    image=entry_image_1
)
search_entry = tk.Entry(
    window,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
search_entry.pack()
search_entry.bind("<KeyRelease>", on_key_release)

search_entry.place(
    x=484.0,
    y=18.0,
    width=202.0,
    height=52.0
)

canvas.create_rectangle(
    245.0,
    192.0,
    493.0,
    425.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    548.0,
    192.0,
    796.0,
    425.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    851.0,
    192.0,
    1099.0,
    425.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    851.0,
    471.0,
    1099.0,
    704.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    548.0,
    473.0,
    796.0,
    706.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    245.0,
    471.0,
    493.0,
    704.0,
    fill="#D9D9D9",
    outline="")

#first row of friends in the main page
text_items_row1 = []
for i in range(3):
    text_item = canvas.create_text(
        300.0*(i+1),
        210.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter", 30 * -1)
    )
    text_items_row1.append(text_item)

#second row of friends in the main page    
text_items_row2 = []
for i in range(3):
    text_item = canvas.create_text(
       300.0*(i+1),
       489.0,
       anchor="nw",
       text="",
       fill="#000000",
       font=("Inter", 30 * -1)
    )
    text_items_row2.append(text_item)

retrieve_data(text_items_row1,text_items_row2)

canvas.create_text(
    358.0,
    26.0,
    anchor="nw",
    text="Search",
    fill="#000000",
    font=("Inika", 25 * -1)
)

canvas.create_text(
    876.0,
    22.0,
    anchor="nw",
    text="Kostas",
    fill="#000000",
    font=("Inter Medium", 25 * -1)
)

canvas.create_rectangle(
    881.0,
    65.0,
    1101.0,
    75.0,
    fill="#000000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=send_friend_req(conn),
    relief="flat"
)
button_1.place(
    x=292.0,
    y=341.0,
    width=142.0,
    height=44.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=send_friend_req(conn),
    relief="flat"
)
button_2.place(
    x=609.0,
    y=341.0,
    width=131.0,
    height=44.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=send_friend_req(conn),
    relief="flat"
)
button_3.place(
    x=909.0,
    y=338.0,
    width=131.0,
    height=47.0
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
    x=909.0,
    y=596.0,
    width=131.0,
    height=47.0
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
    x=609.0,
    y=596.0,
    width=123.0,
    height=47.0
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
    x=303.0,
    y=596.0,
    width=131.0,
    height=47.0
)

canvas.create_text(
    609.0,
    311.0,
    anchor="nw",
    text="Add Friend",
    fill="#333333",
    font=("Inter Medium", 25 * -1)
)

canvas.create_text(
    292.0,
    309.0,
    anchor="nw",
    text="Add Friend",
    fill="#333333",
    font=("Inter Medium", 25 * -1)
)

canvas.create_text(
    909.0,
    309.0,
    anchor="nw",
    text="Add Friend",
    fill="#333333",
    font=("Inter Medium", 25 * -1)
)

canvas.create_text(
    909.0,
    566.0,
    anchor="nw",
    text="Add Friend",
    fill="#333333",
    font=("Inter Medium", 25 * -1)
)

canvas.create_text(
    300.0,
    566.0,
    anchor="nw",
    text="Add Friend",
    fill="#333333",
    font=("Inter Medium", 25 * -1)
)

canvas.create_text(
    601.0,
    566.0,
    anchor="nw",
    text="Add Friend",
    fill="#333333",
    font=("Inter Medium", 25 * -1)
)

canvas.create_rectangle(
    406.0,
    202.0,
    479.0,
    275.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    699.0,
    202.0,
    772.0,
    275.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1009.0,
    202.0,
    1082.0,
    275.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    1012.0,
    481.0,
    1085.0,
    554.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    703.0,
    481.0,
    776.0,
    554.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    406.0,
    481.0,
    479.0,
    554.0,
    fill="#FFFFFF",
    outline="")

window.resizable(False, False)
window.mainloop()

