import mysql.connector
from tkinter import messagebox


class Notifications:
    def __init__(self, canvas, db, ):
       self.canvas = canvas 
       self.db = db

    def send_notification(self, user_id, friend_id, content, status, notification_type):
       
       query = "INSERT INTO notifications(user_id,friend_id,content,status,notification_type) VALUES (%s,%s,%s,%s,%s)"
       cursor = self.db.execute_query(query, (user_id, friend_id, '%'+content+'%','%'+status+'%', '%'+notification_type+'%'))
       
       if cursor:
           messagebox.showinfo("Success", "Friend request sent")
          
       else:
           messagebox("Error", "No request")

    #def get_request_reply():
           
    #def get_bookreq_reply():
    
   # def delete_notification():
