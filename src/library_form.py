import mysql.connector


class Library_Form:

    def __init__(self):
     pass

    def get_categories(self):
        categories = []
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="bookeat"
            )

            cursor = conn.cursor()

            query = "SELECT category_name FROM categories"
            cursor.execute(query)
            categories = [row[0] for row in cursor.fetchall()]
            
        except mysql.connector.Error as error:
            print("Failed to fetch categories:", error)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                
        return categories
      

    def show_categories():
     pass

    def get_books(self,categ):
       
        books = []
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="bookeat"
            )

            cursor = conn.cursor(dictionary=True)

            query ="SELECT title,category_name as Category,author,date,quantity FROM books INNER JOIN categories ON cat_id=category_id LEFT JOIN warehouse ON books.book_id = warehouse.id_book WHERE category_name LIKE %s"
            
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

    def show_books():
     pass