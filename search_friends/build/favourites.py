from tkinter import messagebox

class Favourites():
    def __init__(self, canvas, db, user_id):
        self.canvas = canvas
        self.db = db
        self.user_id = user_id

    def check_favourites(self, book_id):
        books = []
        books = self.get_favourites()

        query = "SELECT title FROM books WHERE book_id = %s"
        cursor = self.db.execute_query(query, (book_id,))
        title = cursor.fetchall()
        book_title = title[0][0]
        reply = self.is_on_favourites(book_title, books)
        #print(f"Reply from check_favourites:", reply)
        return reply
        

    def get_favourites(self):
        query = "SELECT book_id FROM favourites WHERE user_id LIKE %s"
        cursor = self.db.execute_query(query, (self.user_id,))
        books_in_favs = cursor.fetchall()
        book_titles = [None]*len(books_in_favs)

        if books_in_favs:
            for i in range(len(books_in_favs)):
                id = books_in_favs[i][0]
                query = "SELECT title FROM books WHERE book_id LIKE %s"
                cursor1 = self.db.execute_query(query, (id,))
                info = cursor1.fetchone()

                if info:
                   book_titles[i] = info[0]
            for title in book_titles:
                print(f"Books from get_favourites:",  title)
            return book_titles
        else:
            return 0
                 
                
    def insert_to_favourites(self, book_id):
        query = "INSERT INTO favourites(user_id, book_id) VALUES (%s, %s)"
        self.db.execute_query(query, (self.user_id,book_id))
        self.db.commit_query()

    def is_on_favourites(self, book_title, books):
        if books:
            for i in range(len(books)):
                    if book_title==books[i]:
                        messagebox.showinfo("NOTE", "Book is already in favourites")
                        return book_title
                    else:
                        print("this book is not in favourites")
                        return 0 
        else:
            print("no books in favourites from the is_on_favourites")
            #messagebox.showinfo("Not in favourites", "The book can be added to favourites")
            return 0
            
