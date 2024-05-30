

class RecommendedBooks:
    def __init__(self, canvas, db, user_id):
        self.canvas = canvas
        self.db = db
        self.user_id = user_id


    def get_books(self):
        query = "SELECT book_id FROM recommendedBooks WHERE user_id LIKE %s "
        cursor = self.db.execute_query(query, (self.user_id,))
        ids = cursor.fetchall()
        titles = [None]*len(ids)
        if ids:
            for i in range(len(ids)):
                id = ids[i][0]
                query = "SELECT title FROM books WHERE book_id LIKE %s"
                cursor1 = self.db.execute_query(query, (id,))
                info = cursor1.fetchall()
                titles[i] = info[0][0]

        return titles

        