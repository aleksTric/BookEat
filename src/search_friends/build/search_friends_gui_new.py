
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
        self.conn = self.db.connect_to_database()
        
        self.window = root
        self.window.geometry("1237x856")
        self.window.configure(bg = "#FFFFFF")

        self.canvas = Canvas( self.window, bg = "#FFFFFF", height = 856, width = 1237, bd = 0, highlightthickness = 0, relief = "ridge")

        self.canvas.place(x = 0, y = 0)
        self.create_ui()
        self.searchfriend = SearchFriends(self.canvas, self.db, self.friend0, self.friend1, self.friend2, self.friend3, self.friend4, self.friend5)
        self.current_user = User(self.canvas, self.db)
        

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
       self.user_name = self.canvas.itemcget(self.text_item_user, 'text')
       # friend user
       self.friend_user = User(self.canvas, self.db)

       self.canvas.create_rectangle( 881.0, 65.0, 1101.0, 75.0, fill="#000000", outline="")
       self.canvas.create_text( 200.0, 100.0, anchor="nw", text="Suggested Friends", fill="#000000", font=("Inter", 30 * -1))
       self.user_friends = self.get_users()
       if self.user_friends:
           for i in range(len(self.user_friends)):
               if i==0:
                   self.canvas.create_rectangle( 406.0, 202.0, 479.0, 275.0, fill="#FFFFFF", outline="")   
                   self.friend0=self.canvas.create_text( 260.0, 210.0, anchor="nw", text=self.user_friends[0], fill="#000000", font=("Inter", 30 * -1))
                   self.button_1 = Button(text ="ADD FRIEND",borderwidth=0,highlightthickness=0,command=lambda: self.button_pressed(self.user_friends[0],self.user_name),relief="flat")
                   self.button_1.place( x=292.0, y=341.0, width=142.0, height=44.0)
               if i==1:
                   self.canvas.create_rectangle( 699.0, 202.0, 772.0, 275.0, fill="#FFFFFF", outline="")
                   self.friend1=self.canvas.create_text( 560.0, 210.0, anchor="nw", text=self.user_friends[1], fill="#000000", font=("Inter", 30 * -1))
                   self.button_2 = Button( text = "ADD FRIEND", borderwidth=0, highlightthickness=0, command=lambda: self.button_pressed(self.user_friends[1],self.user_name), relief="flat")
                   self.button_2.place( x=609.0, y=341.0, width=131.0, height=44.0)
               if i==2:
                   self.canvas.create_rectangle( 1009.0, 202.0, 1082.0, 275.0, fill="#FFFFFF", outline="")
                   self.friend2=self.canvas.create_text( 860.0, 210.0, anchor="nw", text=self.user_friends[2], fill="#000000", font=("Inter", 30 * -1))
                   self.button_3 = Button(text = "ADD FRIEND",borderwidth=0,highlightthickness=0,command=lambda: self.button_pressed(self.user_friends[2],self.user_name),relief="flat")
                   self.button_3.place( x=909.0, y=338.0, width=131.0, height=47.0)
               if i==3:
                   self.canvas.create_rectangle( 406.0, 481.0, 479.0, 554.0, fill="#FFFFFF", outline="")
                   self.friend3=self.canvas.create_text( 860.0, 489.0, anchor="nw", text=self.user_friends[3], fill="#000000", font=("Inter", 30 * -1))
                   self.button_6 = Button( text = "ADD FRIEND", borderwidth=0, highlightthickness=0, command=lambda: self.button_pressed(self.user_friends[3],self.user_name), relief="flat")
                   self.button_6.place( x=303.0, y=596.0, width=131.0, height=47.0)
               if i==4:
                   self.canvas.create_rectangle( 703.0, 481.0, 776.0, 554.0, fill="#FFFFFF", outline="")
                   self.friend4=self.canvas.create_text( 560.0, 489.0, anchor="nw", text=self.user_friends[4], fill="#000000", font=("Inter", 30 * -1))
                   self.button_5 = Button(text="ADD FRIEND",borderwidth=0,highlightthickness=0,command=lambda: self.button_pressed(self.user_friends[4],self.user_name),relief="flat")
                   self.button_5.place( x=609.0, y=596.0, width=123.0, height=47.0)
               if i==5:
                   self.canvas.create_rectangle( 1012.0, 481.0, 1085.0, 554.0, fill="#FFFFFF", outline="")
                   self.friend5=self.canvas.create_text( 260.0, 489.0, anchor="nw", text=self.user_friends[5], fill="#000000", font=("Inter", 30 * -1))
                   self.button_4 = Button( text = "ADD FRIEND", borderwidth=0, highlightthickness=0, command=lambda: self.button_pressed(self.user_friends[5], self.user_name), relief="flat")
                   self.button_4.place(x=909.0,y=596.0,width=131.0,height=47.0)
       
       #SEARCH
       entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
       entry_bg_1 = self.canvas.create_image(585.0,45.0,image=entry_image_1)
       self.search_entry = tk.Entry(self.window,bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
       self.search_entry.pack()
       self.search_entry.bind("<KeyRelease>", self.searching)
       self.search_entry.place(x=484.0,y=18.0,width=202.0,height=52.0)

   
    def searching(self, event):
         search_term = event.widget.get()
         names = self.searchfriend.get_by_username(search_term)
         self.searchfriend.search(names)

    def button_pressed(self, friend_name, user_name):
        self.new_friend = User(self.canvas, self.db)
        print(f"button clicked!")
        self.new_friend.send_friend_req(friend_name, user_name)

    def get_users(self):
        query = "SELECT (username) FROM account"
        cursor = self.db.execute_query(query)
        friends = cursor.fetchall()
        if friends:
            friends_names = [None]*len(friends)
            for i in range(len(friends)):
                friends_names[i]=friends[i][0]
        print("friends:", friends_names)
        return friends_names
    
if __name__ == "__main__":
     root = tk.Tk()
     app = MyApplication(root)
     root.mainloop()