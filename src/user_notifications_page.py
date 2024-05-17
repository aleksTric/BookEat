import tkinter as tk

class NotificationWindow:
    def __init__(self):
        self.notification_window = tk.Tk()
        self.notification_window.title("Notifications")

        self.notification_listbox = tk.Listbox(self.notification_window, font=("Helvetica", 12), width=50)
        self.notification_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.notification_listbox.bind("<Double-Button-1>", self.show_notification_details)

        self.close_button = tk.Button(self.notification_window, text="Close", command=self.close_notification_window)
        self.close_button.pack(pady=10)

    def add_notification(self, notification):
        self.notification_listbox.insert(tk.END, notification)

    def show_notification_details(self, event):
        selected_index = self.notification_listbox.curselection()
        if selected_index:
            selected_notification = self.notification_listbox.get(selected_index)
            notification_details_window = tk.Toplevel(self.notification_window)
            notification_details_window.title("Notification Details")

            # Extract book details from the notification string (assuming it's formatted correctly)
            book_details = selected_notification.split(": ")[1]
            book_title, book_quantity, return_date = book_details.split(", ")

            # Label for book title
            title_label = tk.Label(notification_details_window, text=f"Book Title: {book_title}", font=("Helvetica", 12))
            title_label.pack(padx=20, pady=5)

            # Label for book quantity
            quantity_label = tk.Label(notification_details_window, text=f"Quantity: {book_quantity}", font=("Helvetica", 12))
            quantity_label.pack(padx=20, pady=5)

            # Label for return date
            return_date_label = tk.Label(notification_details_window, text=f"Date of Return: {return_date}", font=("Helvetica", 12))
            return_date_label.pack(padx=20, pady=5)

            # Button to return the book
            return_button = tk.Button(notification_details_window, text="Return Book", command=lambda: self.return_book(book_title, notification_details_window))
            return_button.pack(padx=20, pady=10)

    def return_book(self, book_title, notification_details_window):
        # Create a new window for success message
        success_window = tk.Toplevel(self.notification_window)
        success_window.title("Success")

        # Label to display success message
        success_label = tk.Label(success_window, text=f"Book '{book_title}' returned successfully ✓", font=("Helvetica", 12))
        success_label.pack(padx=20, pady=10)

        # Destroy success window after 2 seconds
        success_window.after(2000, success_window.destroy)

        # Close notification details window
        notification_details_window.destroy()

    def close_notification_window(self):
        self.notification_window.destroy()

# Example usage
notification_window = NotificationWindow()
notification_window.add_notification("New notification: You have a new message!")
notification_window.add_notification("Book return reminder: Book 1, 2, 2024-05-30")

notification_window.notification_window.mainloop()
