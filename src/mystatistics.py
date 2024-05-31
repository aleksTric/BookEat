import mysql.connector

class Statistics:

    def __init__(self, requested_books, latest_books,popular_books):
        self.__requested_books = requested_books
        self.__latest_books=latest_books
        self.__popular_books = popular_books
        
    def estimate():
        pass
    
    def display():
        pass

    def get_requested_books():
       
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="bookeat"
            )

            cursor = conn.cursor(dictionary=True)

            query ="SELECT title,
            
            params = [f"%{categ}%"]
            cursor.execute(query, params)
            books = cursor.fetchall()
            

        except mysql.connector.Error as error:
            print("Failed to fetch books:", error)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                
        return books