from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk

class BookDetails:
    def __init__(self, canvas, db, root, user_id, book_id):
        #self.canvas = canvas
        self.db = db
        self.root = root
        self.user_id = user_id
        self.book_id = book_id
        #get book details
        query = "SELECT title FROM books WHERE book_id LIKE %s"
        cursor = self.db.execute_query(query, (self.book_id,))
        title = cursor.fetchall()
        self.title = title[0][0]

        query = "SELECT author FROM books WHERE book_id LIKE %s"
        cursor = self.db.execute_query(query, (self.book_id,))
        author = cursor.fetchall()
        self.author = author[0][0]

    def get_book(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Book Details")
        new_window.geometry("837x656")
        label = tk.Label(new_window, text="Book details go here.")
        label.pack(pady=20)

        canvas = Canvas(new_window, bg = "#FFFFFF", height = 856, width = 1237, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)
        canvas.create_rectangle( 0.0, 0.0, 837.0, 656.0, fill="#D9D9D9", outline="")
        canvas.create_rectangle( 36.0, 137.0, 801.0, 630.0, fill="#FFFFFF", outline="")

        self.text_title = canvas.create_text( 101.0, 207.0, anchor="nw", text=self.title, fill="blue", font=("Inter Medium", 25 * -1))
        self.text_author = canvas.create_text( 101.0, 307.0, anchor="nw", text=self.author, fill="blue", font=("Inter Medium", 25 * -1))

        button_fav = Button(new_window, text="Add to favourites", command= lambda: self.add_to_favourites())
        button_fav.place( x=100.0, y=500.0, width=142.0, height=44.0)

        button_wishlist = Button(new_window, text="Add to wishlist", command= lambda: self.add_to_wishlist())
        button_wishlist.place( x=300.0, y=500.0, width=142.0, height=44.0)

        
    def add_to_wishlist(self):
        query = "INSERT INTO wishlist VALUES (%s, %s)"
        self.db.execute_query(query, (self.user_id, self.book_id))
        messagebox.showinfo("ADD", "Added to wishlist!!")
        
    def add_to_favourites(self):
        query = "INSERT INTO favourites VALUES (%s, %s)"
        self.db.execute_query(query, (self.user_id, self.book_id))
        messagebox.showinfo("ADD", "Added to favourites!!")
