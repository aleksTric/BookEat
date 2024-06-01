import mysql.connector

class Statistics:

    def __init__(self,requested_books,latest_books,popular_books):
        self.__requested_books=requested_books
        self.__latest_books = latest_books
        self.__popular_books = popular_books
        
    def estimate():
        pass
    
    
    def display():
        pass
    
    def get_requested_books(self):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="bookeat"
            )

            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT b.title AS Title, COUNT(r.book_id) AS Requests
            FROM books b
            INNER JOIN requested_books r ON b.book_id = r.book_id
            GROUP BY b.title
            """
            
            cursor.execute(query)
            books = cursor.fetchall()

        except mysql.connector.Error as error:
            print("Failed to fetch books:", error)
            books = []
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                
        return books