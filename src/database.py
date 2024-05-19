import mysql.connector
from config import db_config

class Database:
    def __init__(self, config=db_config):
        self.config = config
        self.connection = None
        self.cursor = None
        self.is_connected = False

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            print("Connected to the database!")
            self.cursor = self.connection.cursor(dictionary=True)
            self.is_connected = True
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            self.is_connected = False

    def close_connection(self):
        if self.is_connected:
            self.cursor.close()
            self.connection.close()
            print("Connection to the database closed.")
            self.is_connected = False

    def query(self, query, params=None):
        if not self.is_connected:
            self.connect_to_database()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def submit(self, query, params=None):
        if not self.is_connected:
            self.connect_to_database()
        self.cursor.execute(query, params)
        self.connection.commit()

class Warehouse:
    def __init__(self, database):
        self.database = database

    def check_stock(self, book_id):
        try:
            query = """
            SELECT quantity FROM warehouse
            WHERE id_book = %s
            """
            result = self.database.query(query, (book_id,))
            if result:
                return result[0]['quantity']
            return 0  # If no result found, return 0 indicating no stock
        except mysql.connector.Error as err:
            print(f"Error checking stock in the warehouse: {err}")
            return 0  # Return 0 by default in case of an error

class Book_Details:
    def __init__(self, database):
        self.database = database

    def get_books(self):
        try:
            query = """
            SELECT books.*, categories.category_name 
            FROM books 
            JOIN categories ON books.cat_id = categories.category_id
            """
            books = self.database.query(query)
            for book in books:
                book['image_path'] = 'assets/home/book-pixel-art.png'
            return books
        except mysql.connector.Error as err:
            print(f"Error fetching books from database: {err}")
            return []

    def get_book_details(self, book_id):
        try:
            query = """
            SELECT books.*, categories.category_name 
            FROM books 
            JOIN categories 
            ON books.cat_id = categories.category_id 
            WHERE book_id = %s
            """
            book_details = self.database.query(query, (book_id,))
            return book_details[0] if book_details else None
        except mysql.connector.Error as err:
            print(f"Error fetching book details from database: {err}")
            return None

    def get_category_name(self, category_id):
        try:
            query = "SELECT category_name FROM categories WHERE category_id = %s"
            category_name = self.database.query(query, (category_id,))
            if category_name:
                return category_name[0]['category_name']
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error fetching category name from database: {err}")
            return None

    def isAvailable(self, book_id):
        warehouse = Warehouse(self.database)
        quantity = warehouse.check_stock(book_id)
        return quantity

    def check_borrowed_books(self, book_id):
        try:
            query = """
            SELECT quantity FROM warehouse
            WHERE id_book = %s
            """
            result = self.database.query(query, (book_id,))
            if result:
                quantity = result[0]['quantity']
                if quantity >= 5:
                    return True  # Book is already borrowed 5 or more times
            return False  # Book is available for borrowing
        except mysql.connector.Error as err:
            print(f"Error checking borrowed books: {err}")
            return True  # Return True by default in case of an error




