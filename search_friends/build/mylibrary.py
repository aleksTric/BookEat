from wishlist import Wishlist
from favourites import Favourites
import mysql.connector

class MyLibrary:
    def __init__(self, canvas, db, user_id):
        self.canvas = canvas 
        self.db = db
        self.user_id = user_id
     
    #def get_user_books():

    #def send_book_request():

    #def is_book_fav_want():

    #def add_book_favs():

    #def del_book_wants():

    def delete_from_wishlist(self, book_id):
        self.wishlist = Wishlist(self.canvas, self.db, self.user_id)
        reply = self.wishlist.check_wishlist(book_id)
        print(f"reply from del_to_wishlist: {reply}")
        if reply:
            query = "DELETE FROM wishlist WHERE book_id = %s"
            self.db.execute_query(query, (book_id,))
            self.db.commit_query()

    def delete_from_favourites(self, book_id):
        self.favourites = Favourites(self.canvas, self.db, self.user_id)
        reply = self.favourites.check_favourites(book_id)
        print(f"reply from del_to_favourites: {reply}")
        if reply:
            query = "DELETE FROM favourites WHERE book_id = %s"
            self.db.execute_query(query, (book_id,))
            self.db.commit_query()