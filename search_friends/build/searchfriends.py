import mysql.connector
from database import Database 

class SearchFriends:
    def __init__(self, canvas, db, text_item0, text_item1, text_item2, text_item3, text_item4, text_item5):
         self.canvas = canvas
         self.db = db
         self.text_item0 = text_item0
         self.text_item1 = text_item1
         self.text_item2 = text_item2
         self.text_item3 = text_item3
         self.text_item4 = text_item4
         self.text_item5 = text_item5

    def search(self, search_term):
            
            query = "SELECT username FROM account WHERE username LIKE %s"
            cursor = self.db.execute_query(query, ('%' + search_term + '%',))
            rows = cursor.fetchall()
            
            self.canvas.itemconfig(self.text_item0, text="")
            self.canvas.itemconfig(self.text_item1, text="")
            self.canvas.itemconfig(self.text_item2, text="")
            self.canvas.itemconfig(self.text_item3, text="")
            self.canvas.itemconfig(self.text_item4, text="")
            self.canvas.itemconfig(self.text_item5, text="")

            self.canvas.itemconfig(self.text_item0, text=rows[0])
            self.canvas.itemconfig(self.text_item1, text=rows[1])
            self.canvas.itemconfig(self.text_item2, text=rows[2])
            self.canvas.itemconfig(self.text_item3, text=rows[3])
            self.canvas.itemconfig(self.text_item4, text=rows[4])
            self.canvas.itemconfig(self.text_item5, text=rows[5])
