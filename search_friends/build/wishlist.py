from tkinter import messagebox
import mysql.connector

class Wishlist():
    def __init__ (self, canvas, db, user_id):
        self.canvas = canvas
        self.db = db 
        self.user_id = user_id

    def check_wishlist(self, book_id):
        books = []
        books = self.get_wishlist()

        query = "SELECT title FROM books WHERE book_id LIKE %s"
        cursor = self.db.execute_query(query, (book_id,))
        title = cursor.fetchall()
       # if title:
        book_title = title[0][0]
        reply = self.is_on_wishlist(book_title, books)
        return reply

    def get_wishlist(self):
        query = "SELECT book_id FROM wishlist WHERE user_id LIKE %s"
        cursor = self.db.execute_query(query, (self.user_id,))
        idbooks_in_wishlist = cursor.fetchall()
        book_titles = [None]*len(idbooks_in_wishlist)

        if idbooks_in_wishlist:
            for i in range(len(idbooks_in_wishlist)):
                id = idbooks_in_wishlist[i][0]
                query = "SELECT title FROM books WHERE book_id = %s ;"
                cursor1 = self.db.execute_query(query, (id,))
                info = cursor1.fetchone()
                if info:
                  book_titles[i] = info[0]
            for title in book_titles:
                print(f"Books from get_favourites:",  title)
            return book_titles
        else:
            return 0
        
    def is_on_wishlist(self, book_title, books):
        if books:
            for i in range(len(books)):
                    if books[i]==book_title:
                        messagebox.showinfo("NOTE", "Book is already in wishlist")
                        return book_title
                    else:
                        print("this book is not in wishlist")
                        return 0 
        else:
            print("no books in wishlist from the is_on_wishlist")
            #messagebox.showinfo("Not in favourites", "The book can be added to favourites")
            return 0
            
            
    def insert_to_wishlist(self, book_id):
        query = "INSERT INTO wishlist(user_id, book_id) VALUES (%s, %s)"
        self.db.execute_query(query, (self.user_id, book_id))
        self.db.commit_query()

