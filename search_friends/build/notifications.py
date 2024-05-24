import mysql.connector
from tkinter import messagebox
from user import User


class Notifications:
    def __init__(self, canvas, db, text_item_user):
       self.canvas = canvas 
       self.db = db
       self.text_item_user = text_item_user

    def send_friend_req(self, text_item):
       self.friend = User(self.canvas, self.db)
       self.logged_user = User(self.canvas, self.db)

       user_email = self.logged_user.is_user(self.text_item_user)
       friend_email = self.friend.get_user(text_item)
       
       query = "SELECT user_id FROM account WHERE email LIKE %s"
       cursor = self.db.execute_query(query, ('%' + user_email + '%',))
       user_id = cursor.fetchall()

       query = "SELECT user_id FROM account WHERE email LIKE %s"
       cursor = self.db.execute_query(query, ('%' + friend_email + '%',))
       friend_id = cursor.fetchall()
       
       content = 'Friend Request!!'
       status = 0
       not_type = 'friend request'
       query = "INSERT INTO notifications(user_id,friend_id,content,status,notification_type) VALUES (%s,%s,%s,%s,%s)"
       cursor = self.db.execute_query(query, (user_id[0][0], friend_id[0][0], '%'+content+'%', status, '%'+not_type+'%'))
       
       if cursor:
             messagebox.showinfo("Success", "Friend request sent")
          
       else:
           messagebox("Error", "No request")

    #def get_request_reply():

    def get_bookreq_reply():
    
    def delete_not():
