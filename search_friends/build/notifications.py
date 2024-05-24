import mysql.connector
from tkinter import messagebox
from user import User


class Notifications:
    def __init__(self, canvas, db):
       self.canvas = canvas 
       self.db = db

    def send_friend_req(self, text_item):
      # self.number = int
       self.friend = User(self.canvas, self.db)
       
       email = self.friend.get_user(text_item)
       print(f"{email}")
       

