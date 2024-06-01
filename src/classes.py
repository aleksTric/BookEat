import mysql.connector # type: ignore
import json
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
class Library_Form:
    def __init__(self):
        pass

    def get_categories(self):
        categories = []
        try:
            conn = mysql.connector.connect(**db_config)
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

    def get_books(self, category):
        books = []
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)
            query = """
            SELECT title, category_name as Category, author, date, quantity
            FROM books
            INNER JOIN categories ON cat_id = category_id
            LEFT JOIN warehouse ON books.book_id = warehouse.id_book
            WHERE category_name LIKE %s
            """
            params = [f"%{category}%"]
            cursor.execute(query, params)
            books = cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to fetch books:", error)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
        return books


class Admin:
    def __init__(self):
        self.db = Database()
        self.library_form = Library_Form()
    def add_category(self, category_name):
        try:
            query = "INSERT INTO categories (category_name) VALUES (%s)"
            self.db.submit(query, (category_name,))
            print(f"Category '{category_name}' added successfully.")
        except mysql.connector.Error as err:
            print(f"Error adding category: {err}")

    def add_book(self, title, category, author, date):
        try:
            query = """
            INSERT INTO books (title, cat_id, author, date) 
            VALUES (%s, (SELECT category_id FROM categories WHERE category_name = %s), %s, %s)
            """
            self.db.submit(query, (title, category, author, date))
            print(f"Book '{title}' added successfully.")
        except mysql.connector.Error as err:
            print(f"Error adding book: {err}")

    def upload_json(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if 'books' not in data:
                    raise ValueError("JSON does not contain 'books' key")
                if not isinstance(data['books'], list):
                    raise ValueError("'books' should be a list")
                
                for book in data['books']:
                    if not isinstance(book, dict):
                        raise ValueError(f"Each book entry should be a dictionary. Found: {type(book)}")
                    required_attributes = {'title', 'category', 'author', 'date'}
                    missing_attributes = required_attributes - book.keys()
                    if missing_attributes:
                        raise ValueError(f"Book entry missing attributes: {missing_attributes}")
                    
                    self.add_book(book['title'], book['category'], book['author'], book['date'])
            print(f"Data from '{file_path}' uploaded successfully.")
        except Exception as err:
            print(f"Error uploading JSON data: {err}")
    
    def search_bycateg(self,categ):
       
       books =self.library_form.get_books(categ)
       return books

