
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from mystatistics import Statistics


          

# Create a pie chart from the data
def create_pie_chart(data):
    df = pd.DataFrame(data, columns=['Title', 'Requests'])
    fig = Figure(figsize=(6, 6), dpi=100)
    ax = fig.add_subplot(111)
    ax.pie(df['Requests'], labels=df['Title'], autopct='%1.1f%%', startangle=140)
    ax.set_title('Percentage of Book Requests')
    return fig

# Create the main application window
class BookStatisticsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Top Requested Books")
        self.stats = Statistics()
        # Create a frame to hold the plot
        self.plot_frame = ttk.Frame(root)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)
        
        # Load and display the data
        self.load_data()

    def load_data(self):
        try:
            data = self.stats.get_requested_books()
            if data:
                self.display_chart(data)
            else:
                messagebox.showwarning("No Data", "No data found in the database.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

    def display_chart(self, data):
        fig = create_pie_chart(data)
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BookStatisticsApp(root)
    root.geometry("800x600")
    root.mainloop()