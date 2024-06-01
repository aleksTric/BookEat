import mysql.connector
from database import Database 
from user import User

class SearchFriends:
     def __init__(self, canvas, db, text_item0, text_item1, text_item2, text_item3, text_item4, text_item5):
         self.canvas = canvas
         self.db = db
         self.text0 = text_item0
         self.text1 = text_item1
         self.text2 = text_item2
         self.text3 = text_item3
         self.text4 = text_item4
         self.text5 = text_item5

     def get_by_username(self, search_term):
          query = "SELECT username FROM account WHERE username LIKE %s"
          cursor = self.db.execute_query(query, ('%' + search_term + '%',))
          rows = cursor.fetchall()
          return rows
   
     def search(self, list):
            
            self.canvas.itemconfig(self.text0, text="")
            self.canvas.itemconfig(self.text1, text="")
            self.canvas.itemconfig(self.text2, text="")
            self.canvas.itemconfig(self.text3, text="")
            self.canvas.itemconfig(self.text4, text="")
            self.canvas.itemconfig(self.text5, text="")

            self.canvas.itemconfig(self.text0, text=list[0])
            self.canvas.itemconfig(self.text1, text=list[1])
            self.canvas.itemconfig(self.text2, text=list[2])
            self.canvas.itemconfig(self.text3, text=list[3])
            self.canvas.itemconfig(self.text4, text=list[4])
            self.canvas.itemconfig(self.text5, text=list[5])

     def get_user(self, text_item):
        self.user = User(self.canvas, self.db)
        friend_email = self.user.is_user(text_item)
        print(f"friend email: {friend_email}")
        return friend_email
    