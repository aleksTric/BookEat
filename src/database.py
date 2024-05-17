import mysql.connector

class Database:
    def __init__(self, config):
        self.config = config
        self.connection = None
        self.cursor = None
        self.is_connected = False

    def connect_to_database(self):
        try:
            # Attempt to connect to the database using the provided config
            self.connection = mysql.connector.connect(**self.config)
            print("Connected to the database!")

            # Create a cursor object
            self.cursor = self.connection.cursor(dictionary=True)

            # Set is_connected attribute to True
            self.is_connected = True

        except mysql.connector.Error as err:
            # Handle errors
            print(f"Error connecting to MySQL: {err}")
            self.is_connected = False

    def close_connection(self):
        if self.is_connected:
            # Close cursor and connection
            self.cursor.close()
            self.connection.close()
            print("Connection to the database closed.")
            self.is_connected = False

    def get_books(self):
        try:
            if not self.is_connected:
                self.connect_to_database()

            query = "SELECT books.*, categories.category_name FROM books JOIN categories ON books.cat_id = categories.category_id"
            self.cursor.execute(query)
            books = self.cursor.fetchall()

            # Add default image path for books
            for book in books:
                book['image_path'] = 'assets/home/book-pixel-art.png'

            return books

        except mysql.connector.Error as err:
            print(f"Error fetching books from database: {err}")
            return []

    def get_book_details(self, book_id):
        try:
            if not self.is_connected:
                self.connect_to_database()

            query = """
            SELECT books.*, categories.category_name 
            FROM books 
            JOIN categories 
            ON books.cat_id = categories.category_id 
            WHERE book_id = %s
            """
            self.cursor.execute(query, (book_id,))
            book_details = self.cursor.fetchone()

            return book_details

        except mysql.connector.Error as err:
            print(f"Error fetching book details from database: {err}")
            return None


    def get_category_name(self, category_id):
        try:
            if not self.is_connected:
                self.connect_to_database()

            query = "SELECT category_name FROM categories WHERE category_id = %s"
            self.cursor.execute(query, (category_id,))
            category_name = self.cursor.fetchone()

            if category_name:
                return category_name[0]
            else:
                return None

        except mysql.connector.Error as err:
            print(f"Error fetching category name from database: {err}")
            return None


# Create a Database instance with the provided config
config = {
    'user': 'kostas',
    'password': 'kostas1234',
    'host': '127.0.0.1',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'bookeat',  # Use the correct database name here
    'raise_on_warnings': True
}

db = Database(config)

# Connect to the database
db.connect_to_database()

# Check if connected
if db.is_connected:
    print("Connected to the database!")
else:
    print("Failed to connect to the database.")

# Fetch books from the database
books = db.get_books()
print("Books from the database:")
for book in books:
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Date: {book['date']}")
    print(f"Description: {book['description']}")
    print(f"Category: {book['category_name']}")
    print(f"Image Path: {book['image_path']}")
    print()

# Close the connection
db.close_connection()
