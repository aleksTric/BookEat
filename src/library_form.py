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

    def get_books():
     pass

    def show_books():
     pass