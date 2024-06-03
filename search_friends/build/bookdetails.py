from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
from favourites import Favourites
from wishlist import Wishlist
from mylibrary import MyLibrary

class BookDetails:
    def __init__(self, db, root, user_id, book_id):
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

        query = "SELECT description FROM books WHERE book_id LIKE %s"
        cursor = self.db.execute_query(query, (self.book_id,))
        desc = cursor.fetchall()
        self.description = desc[0][0]

        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Book Details")
        self.new_window.geometry("837x656")
        label = tk.Label(self.new_window, text="Book details go here.")
        label.pack(pady=20)

        self.canvas = Canvas(self.new_window, bg = "#FFFFFF", height = 856, width = 1237, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.wishlist = Wishlist(self.new_window, self.db, self.user_id)
        self.favs = Favourites(self.new_window, self.db, self.user_id)


    def get_book(self):
        
        self.canvas.create_rectangle( 0.0, 0.0, 837.0, 656.0, fill="#D9D9D9", outline="")
        self.canvas.create_rectangle( 36.0, 137.0, 801.0, 630.0, fill="#FFFFFF", outline="")

        self.text_title = self.canvas.create_text( 101.0, 157.0, anchor="nw", text="Title: "+self.title, fill="#000000", font=("Inter Medium", 25 * -1))
        self.text_author = self.canvas.create_text( 101.0, 207.0, anchor="nw", text="Author: " +self.author, fill="#000000", font=("Inter Medium", 25 * -1))
        self.wrap_text(self.description, 50, 101.0, 257.0)

        button_fav = Button(self.new_window, text="Add to favourites", command= lambda: self.add_to_favourites())
        button_fav.place( x=100.0, y=450.0, width=142.0, height=44.0)

        button_fav_del = Button(self.new_window, text=" Remove from favourites", command= lambda: self.remove_from_favourites())
        button_fav_del.place( x=100.0, y=550.0, width=142.0, height=44.0)

        button_wishlist = Button(self.new_window, text="Add to wishlist", command= lambda: self.add_to_wishlist())
        button_wishlist.place( x=300.0, y=450.0, width=142.0, height=44.0)

        button_wishlist_del = Button(self.new_window, text="Remove from wishlist", command= lambda: self.remove_from_wishlist())
        button_wishlist_del.place( x=300.0, y=550.0, width=142.0, height=44.0)

        
    def add_to_wishlist(self):
        reply = self.wishlist.check_wishlist(self.book_id)
        print(f"reply from add_to_wishlist: {reply}")
        if reply==0:
            self.wishlist.insert_to_wishlist(self.book_id)
            messagebox.showinfo("ADD", "Added to wishlist!!")
        
        query = "DELETE FROM recommendedBooks WHERE book_id = %s"
        self.db.execute_query(query, (self.book_id,))
        self.db.commit_query()
        
        
    def add_to_favourites(self):
        reply = self.favs.check_favourites(self.book_id)
        print(f"reply from add_to_favourites: {reply}")
        if reply==0:
            self.favs.insert_to_favourites(self.book_id)
            messagebox.showinfo("ADD", "Added to favourites!!")
            
        query = "DELETE FROM recommendedBooks WHERE book_id = %s"
        self.db.execute_query(query, (self.book_id,))
        self.db.commit_query()

    def remove_from_favourites(self):
        self.users_library = MyLibrary(self.canvas, self.db, self.user_id)
        self.users_library.delete_from_favourites(self.book_id)
        
    def remove_from_wishlist(self):
        self.users_library = MyLibrary(self.canvas, self.db, self.user_id)
        self.users_library.delete_from_wishlist(self.book_id)

    def wrap_text(self, text, wrap_length, x, y):
        words = text.split(' ')
        lines = []
        current_line = ''
        
        for word in words:
            if len(current_line) + len(word) + 1 > wrap_length:
                lines.append(current_line)
                current_line = word
            else:
                if current_line:
                    current_line += ' ' + word
                else:
                    current_line = word
        
        lines.append(current_line) 

        for line in lines:
            self.canvas.create_text(x, y, anchor="nw", text=line, font=("Arial", 16), fill="black")
            y += 20 