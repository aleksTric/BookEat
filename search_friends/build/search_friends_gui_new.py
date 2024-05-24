
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import mysql.connector
from tkinter import messagebox

from database import Database
from notifications import Notifications 
from searchfriends import SearchFriends
from user import User
from friendslist import FriendsList


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Aleks\Desktop\Tkinter-Designer-master\search_friends\build\assets\frame0")
    

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class MyApplication:
    def __init__(self, root):
        self.db = Database("localhost", "root", "abbe8ccf9d", "bookeat")
        self.conn = self.db.connect()
        
        self.window = root
        self.window.geometry("1237x856")
        self.window.configure(bg = "#FFFFFF")

        self.canvas = Canvas( self.window, bg = "#FFFFFF", height = 856, width = 1237, bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)
        self.create_ui()
        self.retrieve_data()
        
       # self.friend_user.get_user(self.text_item0)

    def create_ui(self):
       label = tk.Label(self.window, text="Search:")
       label.pack()

       self.canvas.create_rectangle( 0.0, 0.0, 1237.0, 856.0, fill="#D9D9D9", outline="")
       self.canvas.create_rectangle(0.0, 0.0, 83.0, 856.0, fill="#FFFFFF", outline="")
       self.canvas.create_text(99.0, 22.0, anchor="nw", text=" Friends ", fill="#333333", font=("Inter Thin", 30 * -1))

       self.canvas.create_rectangle(200.0, 139.0, 1149.0, 802.0, fill="#FFFFFF", outline="")
       self.canvas.create_rectangle(845.0, 11.0, 1205.0, 111.0, fill="#FFFFFF", outline="")

       self.canvas.create_rectangle( 245.0, 192.0, 493.0, 425.0, fill="#D9D9D9", outline="")
       self.canvas.create_rectangle( 548.0, 192.0, 796.0, 425.0, fill="#D9D9D9", outline="")
       self.canvas.create_rectangle( 851.0, 192.0, 1099.0, 425.0, fill="#D9D9D9", outline="")
       self.canvas.create_rectangle( 851.0, 471.0, 1099.0, 704.0, fill="#D9D9D9", outline="")
       self.canvas.create_rectangle( 548.0, 473.0, 796.0, 706.0, fill="#D9D9D9", outline="")
       self.canvas.create_rectangle( 245.0, 471.0, 493.0, 704.0, fill="#D9D9D9", outline="")


       self.canvas.create_text( 358.0, 26.0, anchor="nw", text="Search", fill="#000000", font=("Inika", 25 * -1))

       #logged in user 
       self.text_item_user = self.canvas.create_text( 876.0, 22.0, anchor="nw", text="Alexandra", fill="#000000", font=("Inter Medium", 25 * -1))
       
       #self.loggedin_user = User(self.canvas, self.db)
       #self.loggedin_user.is_user(self.text_item_user)
       
       # friend user
       self.friend_user = User(self.canvas, self.db)

       self.canvas.create_rectangle( 881.0, 65.0, 1101.0, 75.0, fill="#000000", outline="")
    
       self.canvas.create_text( 609.0, 311.0, anchor="nw", text="Add Friend", fill="#333333", font=("Inter Medium", 25 * -1))
       self.canvas.create_text( 292.0, 309.0, anchor="nw", text="Add Friend", fill="#333333", font=("Inter Medium", 25 * -1))
       self.canvas.create_text( 909.0, 309.0, anchor="nw", text="Add Friend", fill="#333333", font=("Inter Medium", 25 * -1))
       self.canvas.create_text( 909.0, 566.0, anchor="nw", text="Add Friend", fill="#333333", font=("Inter Medium", 25 * -1))
       self.canvas.create_text( 300.0, 566.0, anchor="nw", text="Add Friend", fill="#333333", font=("Inter Medium", 25 * -1))
       self.canvas.create_text( 601.0, 566.0, anchor="nw", text="Add Friend", fill="#333333", font=("Inter Medium", 25 * -1))
       
       self.canvas.create_rectangle( 406.0, 202.0, 479.0, 275.0, fill="#FFFFFF", outline="")
       self.canvas.create_rectangle( 699.0, 202.0, 772.0, 275.0, fill="#FFFFFF", outline="")
       self.canvas.create_rectangle( 1009.0, 202.0, 1082.0, 275.0, fill="#FFFFFF", outline="")
       self.canvas.create_rectangle( 1012.0, 481.0, 1085.0, 554.0, fill="#FFFFFF", outline="")
       self.canvas.create_rectangle( 703.0, 481.0, 776.0, 554.0, fill="#FFFFFF", outline="")
       self.canvas.create_rectangle( 406.0, 481.0, 479.0, 554.0, fill="#FFFFFF", outline="")
       
       #TEXT_ITEMS that show friends in the main page
       self.text_item0 = self.canvas.create_text( 260.0, 210.0, anchor="nw", text="-", fill="#000000", font=("Inter", 30 * -1))
       self.text_item1 = self.canvas.create_text( 560.0, 210.0, anchor="nw", text="-", fill="#000000", font=("Inter", 30 * -1))
       self.text_item2 = self.canvas.create_text( 860.0, 210.0, anchor="nw", text="-", fill="#000000", font=("Inter", 30 * -1))
       self.text_item3 = self.canvas.create_text( 260.0, 489.0, anchor="nw", text="-", fill="#000000", font=("Inter", 30 * -1))
       self.text_item4 = self.canvas.create_text( 560.0, 489.0, anchor="nw", text="-", fill="#000000", font=("Inter", 30 * -1))
       self.text_item5 = self.canvas.create_text( 860.0, 489.0, anchor="nw", text="-", fill="#000000", font=("Inter", 30 * -1))
       
       self.searchfriend = SearchFriends(self.canvas, self.db, self.text_item0, self.text_item1, self.text_item2,
                                          self.text_item3, self.text_item4, self.text_item5)
       
       #SEARCH
       entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
       entry_bg_1 = self.canvas.create_image(585.0,45.0,image=entry_image_1)
       self.search_entry = tk.Entry(self.window,bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
       self.search_entry.pack()
       self.search_entry.bind("<KeyRelease>", self.get_by_username)
       self.search_entry.place(x=484.0,y=18.0,width=202.0,height=52.0)

       #BUTTONS
       self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
       self.button_1 = Button(image=self.button_image_1,borderwidth=0,highlightthickness=0,command=lambda: self.button_pressed(self.text_item0),relief="flat")
       self.button_1.place( x=292.0, y=341.0, width=142.0, height=44.0)

       self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
       self.button_2 = Button( image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: self.button_pressed(self.text_item1), relief="flat")
       self.button_2.place( x=609.0, y=341.0, width=131.0, height=44.0)

       self.button_image_3 = PhotoImage( file=relative_to_assets("button_3.png"))
       self.button_3 = Button(image=self.button_image_3,borderwidth=0,highlightthickness=0,command=lambda: self.button_pressed(self.text_item2),relief="flat")
       self.button_3.place( x=909.0, y=338.0, width=131.0, height=47.0)

       self.button_image_4 = PhotoImage( file=relative_to_assets("button_4.png"))
       self.button_4 = Button( image=self.button_image_4, borderwidth=0, highlightthickness=0, command=lambda: self.button_pressed(self.text_item5), relief="flat")
       self.button_4.place(x=909.0,y=596.0,width=131.0,height=47.0)

       self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
       self.button_5 = Button(image=self.button_image_5,borderwidth=0,highlightthickness=0,command=lambda: self.button_pressed(self.text_item4),relief="flat")
       self.button_5.place( x=609.0, y=596.0, width=123.0, height=47.0)

       self.button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
       self.button_6 = Button( image=self.button_image_6, borderwidth=0, highlightthickness=0, command=lambda: self.button_pressed(self.text_item3), relief="flat")
       self.button_6.place( x=303.0, y=596.0, width=131.0, height=47.0)


    def retrieve_data(self):
       query = "SELECT username FROM account"
       cursor = self.db.execute_query(query)
       rows = cursor.fetchall()
       
       self.canvas.itemconfig(self.text_item0, text=rows[0])
       self.canvas.itemconfig(self.text_item1, text=rows[1])
       self.canvas.itemconfig(self.text_item2, text=rows[2])
       self.canvas.itemconfig(self.text_item3, text=rows[3])
       self.canvas.itemconfig(self.text_item4, text=rows[4])
       self.canvas.itemconfig(self.text_item5, text=rows[5])

   
    def get_by_username(self, event):
         search_term = event.widget.get()
         self.searchfriend.search(search_term) 


    def button_pressed(self, text_item):
        self.new_friend = Notifications(self.canvas, self.db, self.text_item_user)
        print(f"button clicked!")
        self.new_friend.send_friend_req(text_item)

if __name__ == "__main__":
     root = tk.Tk()
     app = MyApplication(root)
     root.mainloop()
