from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
from favourites import Favourites
from wishlist import Wishlist

class BookDetails:
    def __init__(self, db, root, user_id, book_id):
        #self.canvas = canvas
        self.db = db
        self.root = root
        self.user_id = user_id
        self.book_id = book_id
        
        query = "SELECT title FROM books WHERE book_id LIKE %s"
        cursor = self.db.execute_query(query, (self.book_id,))
        title = cursor.fetchall()
        self.title = title[0][0]

        query = "SELECT author FROM books WHERE book_id LIKE %s"
        cursor = self.db.execute_query(query, (self.book_id,))
        author = cursor.fetchall()
        self.author = author[0][0]

        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Book Details")
        self.new_window.geometry("837x656")
        label = tk.Label(self.new_window, text="Book details go here.")
        label.pack(pady=20)

        self.canvas = Canvas(self.new_window, bg = "#FFFFFF", height = 856, width = 1237, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

    def get_book(self):
        
        self.canvas.create_rectangle( 0.0, 0.0, 837.0, 656.0, fill="#D9D9D9", outline="")
        self.canvas.create_rectangle( 36.0, 137.0, 801.0, 630.0, fill="#FFFFFF", outline="")

        self.text_title = self.canvas.create_text( 101.0, 207.0, anchor="nw", text=self.title, fill="blue", font=("Inter Medium", 25 * -1))
        self.text_author = self.canvas.create_text( 101.0, 307.0, anchor="nw", text=self.author, fill="blue", font=("Inter Medium", 25 * -1))

        button_fav = Button(self.new_window, text="Add to favourites", command= lambda: self.add_to_favourites())
        button_fav.place( x=100.0, y=500.0, width=142.0, height=44.0)

        button_wishlist = Button(self.new_window, text="Add to wishlist", command= lambda: self.add_to_wishlist())
        button_wishlist.place( x=300.0, y=500.0, width=142.0, height=44.0)

        
    def add_to_wishlist(self):
        self.wishlist = Wishlist(self.new_window, self.db, self.user_id)
        reply = self.wishlist.check_wishlist(self.book_id)
        print(f"reply from add_to_wishlist: {reply}")
        if reply==0:
            self.wishlist.insert_to_wishlist(self.book_id)
            messagebox.showinfo("ADD", "Added to wishlist!!")
        
        
    def add_to_favourites(self):
        self.favs = Favourites(self.new_window, self.db, self.user_id)
        reply = self.favs.check_favourites(self.book_id)
        print(f"reply from add_to_favourites: {reply}")
        if reply==0:
            self.favs.insert_to_favourites(self.book_id)
            messagebox.showinfo("ADD", "Added to favourites!!")
        
