import mysql.connector # type: ignore #
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
            query = "SELECT quantity FROM warehouse WHERE id_book = %s"
            result = self.database.query(query, (book_id,))
            return result[0]['quantity'] if result else 0
        except mysql.connector.Error as err:
            print(f"Error checking stock in the warehouse: {err}")
            return 0

    def remove_quantity(self, book_id, quantity):
        try:
            query = """
            UPDATE warehouse
            SET quantity = quantity - %s
            WHERE id_book = %s
            """
            self.database.submit(query, (quantity, book_id))
        except mysql.connector.Error as err:
            print(f"Error removing quantity from warehouse: {err}")


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
            return category_name[0]['category_name'] if category_name else None
        except mysql.connector.Error as err:
            print(f"Error fetching category name from database: {err}")
            return None

    def is_available(self, book_id):
        warehouse = Warehouse(self.database)
        quantity = warehouse.check_stock(book_id)
        return quantity

    def check_borrowed_books(self, book_id):
        try:
            query = "SELECT quantity FROM warehouse WHERE id_book = %s"
            result = self.database.query(query, (book_id,))
            if result:
                quantity = result[0]['quantity']
                return quantity >= 5
            return False
        except mysql.connector.Error as err:
            print(f"Error checking borrowed books: {err}")
            return True

    def show_accept_message(self, request_id):
        print(f"Request {request_id} has been accepted.")

    def show_reject_message(self, request_id):
        print(f"Request {request_id} has been rejected.")

class Requested_Books:
    def __init__(self, database):
        self.database = database
        self.warehouse = Warehouse(database)

    def remove_quantity(self, book_id, quantity):
        self.warehouse.remove_quantity(book_id, quantity)
        
    def accept_borrow_req(self, request_id, book_id, quantity):
        try:
            self.remove_quantity(book_id, quantity)
            query = "UPDATE requested_books SET status = 'accepted' WHERE request_id = %s"
            self.database.submit(query, (request_id,))
            book_details = Book_Details(self.database)
            book_details.show_accept_message(request_id)
        except mysql.connector.Error as err:
            print(f"Error accepting borrow request: {err}")


    


class Recommended_Books:
    def __init__(self, database):
        self.database = database

    def get_books(self):
        try:
            query = """
            SELECT * FROM recommended_books
            """
            return self.database.query(query)
        except mysql.connector.Error as err:
            print(f"Error fetching recommended books: {err}")
            return []

    def show_books(self):
        books = self.get_books()
        for book in books:
            print(f"Book ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}")

    def show_book(self, book_id):
        book = self.get_book_details(book_id)
        if book:
            print(f"Book ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}")
        else:
            print("Book not found.")
