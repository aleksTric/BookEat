import tkinter as tk
from tkcalendar import DateEntry  # type: ignore
from database import Database, Book_Details
from config import db_config
from datetime import datetime
import time
import threading



class BookFrame(tk.Frame):
    def __init__(self, master, book_data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.book_data = book_data
        self.filtered_books = book_data

        self.db = Database()  # Initialize Database instance with the config from config.py
        self.book_details = Book_Details(self.db)  # Initialize Book_Details instance with the Database instance

        self.configure(bg="#DADADA")  # Set the background color of the frame
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Available Books", font=("Helvetica", 24, "bold"), bg="#DADADA", fg="black", )
        title_label.place(relx=0.5, y=20, anchor=tk.CENTER)

        search_label = tk.Label(self, text="Search:", font=("Helvetica", 18), bg="#DADADA", fg="black")
        search_label.place(relx=0.3, y=60, anchor=tk.CENTER)  # Adjust x position for search label

        self.search_var = tk.StringVar()
        search_entry = tk.Entry(self, textvariable=self.search_var, font=("Helvetica", 16),bg="white", fg="black", width=30)
        search_entry.place(relx=0.5, y=60, anchor=tk.CENTER)  # Adjust x position and y value for search entry
        search_entry.bind('<KeyRelease>', self.update_book_display)

        self.book_display_frame = tk.Frame(self, bg="#DADADA")
        self.book_display_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  # Adjust relx and rely for book display

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

        columns = 4  # Number of columns in the grid
        for i, book in enumerate(self.filtered_books):
            row = i // columns
            col = i % columns

            title = book['title']
            title_label = tk.Label(self.book_display_frame, text=title, font=("Helvetica", 16), bg="#DADADA", fg="black")
            title_label.grid(row=row*3, column=col, padx=10, pady=5)

            button = tk.Button(self.book_display_frame, text="View", font=("Helvetica", 16), command=lambda b=book: self.view_book(b))
            button.grid(row=row*3+1, column=col, padx=10, pady=5)

            image_path = book['image_path']
            photo = tk.PhotoImage(file=image_path)

            image_label = tk.Label(self.book_display_frame, image=photo, bg="#DADADA")
            image_label.image = photo
            image_label.grid(row=row*3+2, column=col, padx=10, pady=5)

            self.book_widgets.append(title_label)
            self.book_widgets.append(button)
            self.book_widgets.append(image_label)

    def view_book(self, book):
        book_window = tk.Toplevel(self.master)
        book_window.title(book['title'])
        # book_window.geometry("400x600")  # Adjust the size of the book details window
        book_window.configure(bg="#DADADA")
        book_window.iconphoto(True, tk.PhotoImage(file="./assets/login/bookeat_icon.png"))

        # Calculate the position to center the window
        window_position_x = self.master.winfo_screenwidth() // 2 - 200  # Half of window width (400 / 2)
        window_position_y = self.master.winfo_screenheight() // 2 - 300  # Half of window height (600 / 2)

        # Set the window geometry with the calculated position
        book_window.geometry("400x600+{}+{}".format(window_position_x, window_position_y))


        book_id = book.get('book_id')
        book_details = self.book_details.get_book_details(book_id)

        if book_details:
            # Load book image
            image_path = book_details.get('image_path', 'assets/home/book-pixel-art.png')  # Provide a default image path if not available
            photo = tk.PhotoImage(file=image_path)
            image_label = tk.Label(book_window, image=photo, bg="#DADADA")
            image_label.image = photo
            image_label.pack(pady=10)

            title_label = tk.Label(book_window, text=book_details['title'], font=("Helvetica", 16, "bold"), bg="#DADADA", fg="black")
            title_label.pack(pady=10)

            author_label = tk.Label(book_window, text=f"Author: {book_details['author']}", font=("Helvetica", 16), bg="#DADADA", fg="black")
            author_label.pack(pady=5)

            description_label = tk.Label(book_window, text=book_details['description'], font=("Helvetica", 16), bg="#DADADA", fg="black", wraplength=380)
            description_label.pack(pady=5)

            category_name = book_details.get('category_name')
            if category_name:
                category_label = tk.Label(book_window, text=f"Category: {category_name}", font=("Helvetica", 16), bg="#DADADA", fg="black")
                category_label.pack(pady=5)
            else:
                category_label = tk.Label(book_window, text="Category: N/A", font=("Helvetica", 16), bg="#DADADA", fg="black")
                category_label.pack(pady=5)

            return_date_entry = DateEntry(book_window, width=12, background="darkblue", foreground="white", borderwidth=2, font=("Helvetica", 16))
            return_date_entry.pack(pady=5)
            
            quantity_label = tk.Label(book_window, text="Select Quantity:", font=("Helvetica", 16), bg="#DADADA", fg="black")
            quantity_label.pack(pady=5)
            
            quantity_var = tk.IntVar(value=1)
            quantity_spinbox = tk.Spinbox(book_window, from_=1, to=book_details.get('quantity', 5), textvariable=quantity_var, width=5, font=("Helvetica", 16))
            quantity_spinbox.pack(pady=5)
            
            # Borrow Now button
            borrow_button = tk.Button(book_window, text="Borrow Now!", font=("Helvetica", 16), command=lambda: self.submit_borrow_form(book_details, quantity_var.get(), borrow_button))
            borrow_button.pack(pady=10)

    def submit_borrow_form(self, book, quantity, borrow_button):
        book_id = book['book_id']
        user_id = 1  # Assuming a default user ID for demonstration
        request_content = f"Request for {quantity} copies of '{book['title']}'"  # Request details
        request_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO requested_books (user_id, request_content, request_date, book_id) VALUES (%s, %s, %s, %s)"
        params = (user_id, request_content, request_date, book_id)
        self.db.submit(query, params)
        self.show_message(f"Successfully requested {quantity} copies of '{book['title']}'!")
        # Disable the borrow button after successful request
        borrow_button.config(state=tk.DISABLED)




    def show_message(self, message):
        success_window = tk.Toplevel(self.master)
        success_window.title("Success")
        success_window.configure(bg="#DADADA")
        # Calculate the position to center the window
        window_position_x = self.master.winfo_screenwidth() // 2 - 200  # Half of window width (400 / 2)
        window_position_y = self.master.winfo_screenheight() // 2 - 200  # Half of window height (400 / 2)

        # Set the window geometry with the calculated position
        success_window.geometry("400x200+{}+{}".format(window_position_x, window_position_y))


        # Create a styled label for the message
        success_label = tk.Label(success_window, text=message, font=("Helvetica", 16), bg="#DADADA", fg="black")
        success_label.pack(pady=10)

        # Create a label for the tick symbol
        tick_label = tk.Label(success_window, text="✔️", font=("Arial", 48), bg="#DADADA", fg="green")
        tick_label.pack(pady=10)

        # Destroy the success message after 5 seconds
        threading.Timer(4, success_window.destroy).start()


       



# Create main window
root = tk.Tk()
root.title("Book List")
# root.geometry("1232x856")  # Set the window size
root.configure(bg="#DADADA")  # Set the background color of the main window
root.iconphoto(True, tk.PhotoImage(file="./assets/login/bookeat_icon.png"))

# Calculate the position to center the window
window_position_x = root.winfo_screenwidth() // 2 - 616  # Half of window width (1232 / 2)
window_position_y = root.winfo_screenheight() // 2 - 428  # Half of window height (856 / 2)

# Set the window geometry with the calculated position
root.geometry("1232x856+{}+{}".format(window_position_x, window_position_y))
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
book_frame.pack(expand=True, fill=tk.BOTH)

root.mainloop()
