import tkinter as tk
from tkcalendar import DateEntry # type: ignore
from database import Database, Book_Details
from config import db_config

class BookFrame(tk.Frame):
    def __init__(self, master, book_data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.book_data = book_data
        self.filtered_books = book_data

        self.db = Database()  # Initialize Database instance with the config from config.py
        self.book_details = Book_Details(self.db)  # Initialize Book_Details instance with the Database instance
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Available Books", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=4, pady=10)

        search_label = tk.Label(self, text="Search:", font=("Helvetica", 12))
        search_label.grid(row=1, column=0, padx=(10, 5), pady=5)

        self.search_var = tk.StringVar()
        search_entry = tk.Entry(self, textvariable=self.search_var, font=("Helvetica", 12))
        search_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=5)
        search_entry.bind('<KeyRelease>', self.update_book_display)

        self.book_display_frame = tk.Frame(self)
        self.book_display_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

        self.book_widgets = []
        self.update_book_display()

    def update_book_display(self, event=None):
        search_text = self.search_var.get().lower()
        if search_text:
            self.filtered_books = [book for book in self.book_data if search_text in book['title'].lower()]
        else:
            self.filtered_books = self.book_data

        for widget in self.book_widgets:
            widget.destroy()
        self.book_widgets.clear()

        for i, book in enumerate(self.filtered_books):
            title = book['title']
            title_label = tk.Label(self.book_display_frame, text=title, font=("Helvetica", 12))
            title_label.grid(row=i, column=0, padx=10, pady=5)

            button = tk.Button(self.book_display_frame, text="View", command=lambda b=book: self.view_book(b))
            button.grid(row=i, column=1, padx=10, pady=5)

            image_path = book['image_path']
            photo = tk.PhotoImage(file=image_path)

            image_label = tk.Label(self.book_display_frame, image=photo)
            image_label.image = photo
            image_label.grid(row=i, column=2, padx=10, pady=5)

            self.book_widgets.append(title_label)
            self.book_widgets.append(button)
            self.book_widgets.append(image_label)

    def view_book(self, book):
        book_window = tk.Toplevel(self.master)
        book_window.title(book['title'])

        book_id = book.get('book_id')
        book_details = self.book_details.get_book_details(book_id)

        if book_details:
            title_label = tk.Label(book_window, text=book_details['title'], font=("Helvetica", 16))
            title_label.pack(pady=10)

            description_label = tk.Label(book_window, text=book_details['description'], font=("Helvetica", 12))
            description_label.pack(pady=5)

            category_name = book_details.get('category_name')
            if category_name:
                category_label = tk.Label(book_window, text=f"Category: {category_name}", font=("Helvetica", 12))
                category_label.pack(pady=5)
            else:
                category_label = tk.Label(book_window, text="Category: N/A", font=("Helvetica", 12))
                category_label.pack(pady=5)

            return_date_entry = DateEntry(book_window, width=12, background="darkblue", foreground="white", borderwidth=2)
            return_date_entry.pack(pady=5)
            
            quantity_label = tk.Label(book_window, text="Select Quantity:", font=("Helvetica", 12))
            quantity_label.pack(pady=5)
            
            quantity_var = tk.IntVar(value=1)
            quantity_spinbox = tk.Spinbox(book_window, from_=1, to=book_details.get('quantity', 5), textvariable=quantity_var, width=5)
            quantity_spinbox.pack(pady=5)
            
            borrow_button = tk.Button(book_window, text="Borrow Now!", command=lambda: self.borrow_book(book_details, quantity_var.get()))
            borrow_button.pack(pady=10)

        else:
            error_label = tk.Label(book_window, text="Error: Book details not found!", font=("Helvetica", 12))
            error_label.pack(pady=10)

    def borrow_book(self, book, quantity):
        success_window = tk.Toplevel(self.master)
        success_window.title("Success")
        success_label = tk.Label(success_window, text=f"Successfully borrowed {quantity} copies of '{book['title']}'!", font=("Helvetica", 12))
        success_label.pack(pady=10)
        success_window.after(2000, success_window.destroy)

# Create main window
root = tk.Tk()
root.title("Book List")

# Create Database instance
db = Database()
db.connect_to_database()

if db.is_connected:
    print("Connected to the database!")

# Create Book_Details instance
book_details = Book_Details(db)

# Fetch books from the database
books = book_details.get_books()

# Close the connection
db.close_connection()

# Create and pack BookFrame
book_frame = BookFrame(root, book_data=books)
book_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

root.mainloop()
