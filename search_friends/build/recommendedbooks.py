

class RecommendedBooks:
    def __init__(self, canvas, db):
        self.canvas = canvas
        self.db = db

    def get_books(self, item1, item2, item3, item4):
        
        query = "SELECT title FROM books"
        cursor = self.db.execute_query(query)
        rows = cursor.fetchall()
        
        self.canvas.itemconfig(item1, text=rows[0])
        self.canvas.itemconfig(item2, text=rows[1])
        self.canvas.itemconfig(item3, text=rows[2])
        self.canvas.itemconfig(item4, text=rows[3])

        