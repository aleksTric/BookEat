
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import mysql.connector
import tkinter as tk
from database import Database
from recommendedbooks import RecommendedBooks
from bookdetails import BookDetails
from user import User 


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Aleks\Desktop\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MyApplication:
    def __init__(self, root):
        self.db = Database("localhost", "root", "abbe8ccf9d", "bookeat")
        self.conn = self.db.connect_to_database()
        self.window = root
        self.window.geometry("1237x856")
        self.window.configure(bg = "#FFFFFF")
        
        self.create_library()
        self.rec_books = RecommendedBooks(self.canvas, self.db)
        self.rec_books.get_books(self.text_item1, self.text_item2, self.text_item3, self.text_item4)
        self.user = User(self.canvas, self.db)
        self.user_id = self.user.is_user(self.text_user)
        

    def create_library(self):

        self.canvas = Canvas(self.window, bg = "#FFFFFF", height = 856, width = 1237, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle( 0.0, 0.0, 1237.0, 856.0, fill="#D9D9D9", outline="")

        self.canvas.create_rectangle( 816.0, 9.0, 1176.0, 109.0, fill="#FFFFFF", outline="")
        self.text_user = self.canvas.create_text( 842.0, 22.0, anchor="nw", text="Kostas", fill="#000000", font=("Inter Medium", 25 * -1))

        self.canvas.create_rectangle( 832.0, 65.0, 1052.0, 75.0, fill="#000000", outline="")
        self.canvas.create_rectangle( 36.0, 137.0, 1201.0, 830.0, fill="#FFFFFF", outline="")
        self.canvas.create_text(81.0, 59.0, anchor="nw", text="My Library\n", fill="#000000", font=("Inter Medium", 25 * -1))
        self.canvas.create_text( 70.0, 153.0, anchor="nw", text="Recommended Books", fill="#000000", font=("Inter Medium", 25 * -1))

        self.canvas.create_rectangle( 81.0, 193.0, 321.0, 280.0, fill="#D9D9D9", outline="")
        self.canvas.create_rectangle( 360.0, 193.0, 600.0, 280.0, fill="#D9D9D9", outline="")
        self.canvas.create_rectangle( 651.0, 193.0, 891.0, 280.0, fill="#D9D9D9", outline="")
        self.canvas.create_rectangle( 936.0, 193.0, 1176.0, 280.0, fill="#D9D9D9", outline="")
       
        self.text_item1=self.canvas.create_text( 101.0, 207.0, anchor="nw", text="-", fill="blue", font=("Inter Medium", 25 * -1))
        self.button1 = Button(self.window, text="Show book", command= lambda: self.show_book_details(self.text_item1))
        self.button1.place( x=220.0, y=240.0, width=80.0, height=30.0)

        self.text_item2=self.canvas.create_text( 382.0, 207.0, anchor="nw", text="-", fill="#000000", font=("Inter Medium", 25 * -1))
        self.button2 = Button(self.window, text="Show book", command= lambda: self.show_book_details(self.text_item2))
        self.button2.place( x=500.0, y=240.0, width=80.0, height=30.0)

        self.text_item3=self.canvas.create_text( 671.0, 207.0, anchor="nw", text="-", fill="#000000", font=("Inter Medium", 25 * -1))
        self.button3 = Button(self.window, text="Show book", command= lambda: self.show_book_details(self.text_item3))
        self.button3.place( x=790.0, y=240.0, width=80.0, height=30.0)

        self.text_item4=self.canvas.create_text( 961.0, 207.0, anchor="nw", text="-", fill="#000000", font=("Inter Medium", 25 * -1))
        self.button4 = Button(self.window, text="Show book", command= lambda: self.show_book_details(self.text_item4))
        self.button4.place( x=1080.0, y=240.0, width=80.0, height=30.0)


    def show_book_details(self, text_book):
        book_title = self.canvas.itemcget(text_book, 'text')
        print(f"{book_title}")
        query = "SELECT book_id FROM books WHERE title LIKE %s"
        cursor = self.db.execute_query(query, ('%' + book_title + '%',))
        info = cursor.fetchall()
        book_id = info[0][0]
        self.book_details = BookDetails(self.canvas, self.db, root, self.user_id, book_id)
        self.book_details.get_book()
    
if __name__ == "__main__":
     root = tk.Tk()
     app = MyApplication(root)
     root.mainloop()