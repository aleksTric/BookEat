from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, Label, Scrollbar, VERTICAL, RIGHT, Y, LEFT, BOTH, NW

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\lessons\BookEat\src\assets2\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def search():
    search_query = entry_1.get()
    # Simulate search results
    results = [
        {"title": "Book 1", "category": "Fiction", "author": "Author 1", "date": "2023-01-01", "quantity": 10},
        {"title": "Book 2", "category": "Non-Fiction", "author": "Author 2", "date": "2022-12-31", "quantity": 5},
        {"title": "Book 3", "category": "Science Fiction", "author": "Author 3", "date": "2023-02-01", "quantity": 2},
    ]
    display_results(results)


def display_results(results):
    for widget in results_frame.winfo_children():
        widget.destroy()
    
    for i, item in enumerate(results):
        item_frame = Frame(results_frame, bg="#FFFFFF", padx=5, pady=5)
        item_frame.pack(fill='x', padx=5, pady=2)

        for key, value in item.items():
            label = Label(item_frame, text=f"{key.capitalize()}: ", font=("Inter", 12), bg="#FFFFFF", width=10, anchor="e")
            label.pack(side=LEFT)

            entry_bg_color = "#EEEEEE"
            entry = Entry(item_frame, bd=0, bg=entry_bg_color, fg="#000000", font=("Inter", 12), width=10)
            entry.insert(0, value)
            entry.pack(side=LEFT)

            # Add entry widget to a list of dictionaries, where each dictionary contains entries for one record
            if i >= len(entries):
                entries.append({})
            entries[i][key] = entry

        # Create "Update" button after all attributes
        update_button = Button(item_frame, text="Update", command=lambda idx=i: update_item(idx))
        update_button.pack(side=LEFT, padx=10)

def update_item(idx):
    updated_values = {}
    for key, entry in entries[idx].items():
        updated_values[key] = entry.get()
    print("Updated values for record", idx+1, ":", updated_values)
    # Perform saving operation here for the record at index 'idx'


window = Tk()
window.geometry("1237x856")
window.configure(bg="#D9D9D9")

canvas = Canvas(
    window,
    bg="#D9D9D9",
    height=856,
    width=1237,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    610.0,
    37.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_1.place(
    x=372.0,
    y=18.0,
    width=476.0,
    height=37.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=search,
    relief="flat"
)
button_1.place(
    x=294.0,
    y=12.0,
    width=50.0,
    height=50.0
)

# Adding a Frame to hold the results and a Scrollbar for search results
results_frame = Frame(window, bg="#FFFFFF")
results_frame.place(x=50, y=100, width=1137, height=700)

scrollbar = Scrollbar(results_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

results_canvas = Canvas(results_frame, bg="#FFFFFF", yscrollcommand=scrollbar.set)
results_canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=results_canvas.yview)

results_container = Frame(results_canvas, bg="#FFFFFF")
results_canvas.create_window((0, 0), window=results_container, anchor=NW)

def on_frame_configure(event):
   if results_canvas.winfo_exists():  # Check if results_canvas exists
        results_canvas.configure(scrollregion=results_canvas.bbox("all"))

# List to hold entry widgets
entries = []

# List to hold keys for search results
search_keys = []

window.resizable(False, False)
window.mainloop()