import mysql.connector
from categories import Categories


class Books(Categories):
    def __init__(self, title, category, author, date):
        self.__title = title
        self.__category = category
        self.__author = author
        self.__date = date

    def  get_title(self):
         return self.__title
    
    def  get_categ(self):
         return self.__category
    
    def get_author(self):
         return self.__author

    def get_date(self):
         return self.__date
    
    def get_book(title):
        # Establish a connection to the MySQL database
        
        try:
            conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bookeat"
            )
        
            cursor = conn.cursor()

           
            query = "SELECT COUNT(*) FROM books WHERE title= %s"
            cursor.execute(query, (title,))
            book_count = cursor.fetchone()[0]
            return book_count > 0 
        
        except mysql.connector.Error as error:
            print("Failed to insert book:", error)   
        finally:
            
            if conn.is_connected():
               cursor.close()
               conn.close()
        