

class BookReviews():
    def __init__ (self, db, review_id, review_text, book_id, user_id, stars):
        self.db = db
        self.review_id = review_id
        self.review_text = review_text
        self.book_id = book_id
        self.user_id = user_id
        self.stars = stars

    #def check_if_borrowed(self):
         
    #def valid_stars():