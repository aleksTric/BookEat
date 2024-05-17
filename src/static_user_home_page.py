import tkinter as tk
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar

class BookFrame(tk.Frame):
    def __init__(self, master, book_data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.book_data = book_data
        self.filtered_books = book_data
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Available Books", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Search bar label
        search_label = tk.Label(self, text="Search:", font=("Helvetica", 12))
        search_label.grid(row=1, column=0, padx=(10, 5), pady=5)

        # Search bar
        self.search_var = tk.StringVar()
        
        search_entry = tk.Entry(self, textvariable=self.search_var, font=("Helvetica", 12))
        search_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=5)
        search_entry.bind('<KeyRelease>', self.update_book_display)

        # Book display area
        self.book_display_frame = tk.Frame(self)
        self.book_display_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

        self.book_widgets = []

        # Initially, display all books
        self.update_book_display()

    def update_book_display(self, event=None):
        search_text = self.search_var.get().lower()
        if search_text:
            self.filtered_books = [book for book in self.book_data if search_text in book['title'].lower()]
        else:
            self.filtered_books = self.book_data

        # Clear existing book widgets
        for widget in self.book_widgets:
            widget.destroy()
        self.book_widgets.clear()

        # Display filtered books
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

        title_label = tk.Label(book_window, text=book['title'], font=("Helvetica", 16))
        title_label.pack(pady=10)

        description_label = tk.Label(book_window, text=book['description'], font=("Helvetica", 12))
        description_label.pack(pady=5)
        
        category_label = tk.Label(book_window, text=f"Category: {book['category']}", font=("Helvetica", 12))
        category_label.pack(pady=5)
        
        return_date_label = tk.Label(book_window, text="Date of Return:", font=("Helvetica", 12))
        return_date_label.pack(pady=5)
        
        # Date Entry widget for Date of Return
        return_date_entry = DateEntry(book_window, width=12, background="darkblue", foreground="white", borderwidth=2)
        return_date_entry.pack(pady=5)
        
        # Label for selecting quantity
        quantity_label = tk.Label(book_window, text="Select Quantity:", font=("Helvetica", 12))
        quantity_label.pack(pady=5)
        
        # Spinbox for selecting quantity
        quantity_var = tk.IntVar(value=1)
        quantity_spinbox = tk.Spinbox(book_window, from_=1, to=book.get('quantity', 5), textvariable=quantity_var, width=5)
        quantity_spinbox.pack(pady=5)

        borrow_button = tk.Button(book_window, text="Borrow Now!", command=lambda: self.borrow_book(book, quantity_var.get()))
        borrow_button.pack(pady=10)


    def borrow_book(self, book, quantity):
        # Create a new window for success message
        success_window = tk.Toplevel(self.master)
        success_window.title("Success")

        # Label to display success message
        success_label = tk.Label(success_window, text=f"{quantity} copy/copies of '{book['title']}' requested successfully ✓", font=("Helvetica", 12))
        success_label.pack(padx=20, pady=10)

        # Destroy success window after 2 seconds
        success_window.after(2000, success_window.destroy)

# Example book data
books = [
    {'title': 'Book 1', 'description': 'Description of Book 1', 'category': 'Category 1', 'image_path': 'assets/home/book-pixel-art.png', 'quantity': 5},
    {'title': 'Book 2', 'description': 'Description of Book 2', 'category': 'Category 2', 'image_path': 'assets/home/book-pixel-art.png'},
    {'title': 'Book 3', 'description': 'Description of Book 3', 'category': 'Category 3', 'image_path': 'assets/home/book-pixel-art.png'},
    {'title': 'Book 4', 'description': 'Description of Book 4', 'category': 'Category 4', 'image_path': 'assets/home/book-pixel-art.png'},
    {'title': 'Book 5', 'description': 'Description of Book 5', 'category': 'Category 5', 'image_path': 'assets/home/book-pixel-art.png'},
    {'title': 'Book 6', 'description': 'Description of Book 6', 'category': 'Category 6', 'image_path': 'assets/home/book-pixel-art.png'},
    {'title': 'Book 7', 'description': 'Description of Book 7', 'category': 'Category 7', 'image_path': 'assets/home/book-pixel-art.png'},
    {'title': 'Book 8', 'description': 'Description of Book 8', 'category': 'Category 8', 'image_path': 'assets/home/book-pixel-art.png'}
]

# Create main window
root = tk.Tk()
root.title("Book List")

# Create and pack BookFrame
book_frame = BookFrame(root, book_data=books)
book_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

root.mainloop()
