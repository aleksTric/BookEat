import tkinter as tk
from tkinter import ttk, messagebox
import threading
from classes import Database, Book_Details, Requested_Books  # Ensure this is your database connection class
from config import db_config  # Ensure this is your database configuration

class AdminNotificationsPanel(tk.Tk):
    def __init__(self, db, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = db
        self.book_details = Book_Details(db)
        self.requested_books = Requested_Books(db)
        self.title("Admin Notifications")
        self.geometry("1232x856")
        self.configure(bg="#DADADA")
        self.center_window()
        self.create_widgets()
        self.load_requests()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Pending Requests", font=("Helvetica", 24, "bold"), bg="#DADADA", fg="black")
        self.title_label.pack(pady=20)

        self.requests_frame = tk.Frame(self, bg="#DADADA")
        self.requests_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        label_frame = tk.Frame(self.requests_frame, bg="#DADADA")  # Create a label frame
        label_frame.pack(fill=tk.X)  # Pack it at the top of the requests_frame

        # Add labels for each column
        labels = ["request_id", "username", "request_content", "request_date", "book_id", "quantity"]  # Added quantity label
        for label_text in labels:
            label = tk.Label(label_frame, text=label_text.capitalize(), font=("Helvetica", 16, "bold"), bg="#DADADA", fg="black")
            label.pack(side=tk.LEFT, padx=10, pady=5)

    def load_requests(self):
        requests = self.fetch_requests()

        for widget in self.requests_frame.winfo_children():
            widget.destroy()

        label_frame = tk.Frame(self.requests_frame, bg="#DADADA")  # Create a label frame
        label_frame.pack(fill=tk.X)  # Pack it at the top of the requests_frame

        # Add labels for each column again after clearing the frame
        labels = ["request_id", "username", "request_content", "request_date", "book_id", "quantity"]  # Added quantity label
        for label_text in labels:
            label = tk.Label(label_frame, text=label_text.capitalize(), font=("Helvetica", 16, "bold"), bg="#DADADA", fg="black")
            label.pack(side=tk.LEFT, padx=10, pady=5)

        if not requests:
            no_requests_label = tk.Label(self.requests_frame, text="No pending requests.", font=("Helvetica", 16), bg="#DADADA", fg="black")
            no_requests_label.pack(pady=20)
            return

        for i, request in enumerate(requests):
            self.create_request_row(request)
            if i < len(requests) - 1:
                ttk.Separator(self.requests_frame, orient="horizontal").pack(fill="x", pady=5)

    def fetch_requests(self):
        query = """
        SELECT rb.request_id, rb.request_content, rb.request_date, rb.book_id, a.username, rb.quantity, rb.status
        FROM requested_books rb
        JOIN account a ON rb.user_id = a.user_id
        WHERE rb.status = 'pending'
        """
        return self.db.query(query)

    def create_request_row(self, request):
        request_frame = tk.Frame(self.requests_frame, bg="#DADADA")
        request_frame.pack(fill=tk.X)

        request_info = f"{request['request_id']}, {request['username']}, {request['request_content']}, {request['request_date']}, {request['book_id']}, {request['quantity']}"  # Added quantity

        request_label = tk.Label(request_frame, text=request_info, font=("Helvetica", 16), bg="#DADADA", fg="black")
        request_label.pack(side=tk.LEFT, padx=10)

        accept_button = tk.Button(request_frame, text="Accept", font=("Helvetica", 16), command=lambda: self.accept_borrow_req(request['request_id'], request['book_id'], request['quantity']))  # Passing quantity directly

        accept_button.pack(side=tk.RIGHT, padx=5)

        decline_button = tk.Button(request_frame, text="Decline", font=("Helvetica", 16), command=lambda: self.decline_borrow_req(request['request_id']))
        decline_button.pack(side=tk.RIGHT, padx=5)

    def show_message(self, message):
        success_window = tk.Toplevel(self)
        success_window.title("Success")
        success_window.configure(bg="#DADADA")
        # Calculate the position to center the window
        window_position_x = self.winfo_screenwidth() // 2 - 200  # Half of window width (400 / 2)
        window_position_y = self.winfo_screenheight() // 2 - 200  # Half of window height (400 / 2)

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

    def accept_borrow_req(self, request_id, book_id, quantity):
        self.requested_books.accept_borrow_req(request_id, book_id, quantity)
        self.show_message(f"Request {request_id} has been accepted.")
        self.load_requests()

    def decline_borrow_req(self, request_id):
        self.requested_books.decline_borrow_req(request_id)
        self.show_message(f"Request {request_id} has been declined.")
        self.load_requests()

# Initialize Database instance
db = Database(db_config)
db.connect_to_database()

# Open Admin Notifications Panel
admin_notifications_panel = AdminNotificationsPanel(db)
admin_notifications_panel.mainloop()
