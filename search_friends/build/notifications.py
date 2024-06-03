import mysql.connector
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
from friendslist import FriendsList

class Notifications:
    def __init__(self, db, sender_id, receiver_id):
       self.db = db
       self.sender_id = sender_id
       self.receiver_id = receiver_id

       
    def create_nots(self):
        #self.canvas.create_rectangle( 0.0, 0.0, 837.0, 656.0, fill="#D9D9D9", outline="")
        #self.canvas.create_rectangle( 36.0, 137.0, 801.0, 630.0, fill="#FFFFFF", outline="")

        button_fav = Button(self.new_window, text="Add friend", command= lambda: self.get_request_reply(1))
        button_fav.place( x=100.0, y=450.0, width=142.0, height=44.0)
        
        button_wishlist = Button(self.new_window, text="Deny request", command= lambda: self.get_request_reply(0))
        button_wishlist.place( x=300.0, y=450.0, width=142.0, height=44.0)

    def send_notification(self, sender_id, receiver_id, content, status, notification_type):
       query = "INSERT INTO notifications(user_id,friend_id,content,status,notification_type) VALUES (%s,%s,%s,%s,%s)"
       self.db.execute_query(query, (sender_id, receiver_id, '%'+content+'%','%'+status+'%', '%'+notification_type+'%'))
       reply = self.db.commit_query()
      
       if reply==1:
           messagebox.showinfo("Success", "Friend request sent")
          
       else:
           messagebox("Error", "No request")

    def get_request_reply(self,reply):
           if reply==1:
               print("friend request accepted!")
               self.friendslist = FriendsList(self.canvas, self.db, self.sender_id, self.receiver_id)
               self.friendslist.add_friend()
           if reply==0:
               print("friend request denied!")

    #def get_bookreq_reply():
    
    def delete_notification(self,notification_id):
        query = "DELETE FROM notifications WHERE notification_id = %s"
        self.db.execute_query(query, (notification_id,))
        self.db.commit_query()