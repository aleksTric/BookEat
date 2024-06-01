from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, Label, Scrollbar, VERTICAL, RIGHT, Y, LEFT, BOTH, NW
from tkinter import ttk
from admin import Admin
from library_form import Library_Form

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\lessons\BookEat\src\assets2\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def search():
    search_query = entry_1.get()
    
    results = admin.search_bycateg(search_query)
    print(results)
    display_results(results)

def display_results(results):
    for widget in results_frame.winfo_children():
        widget.destroy()
    
    # Display each result
    for i, item in enumerate(results):
        item_frame = Frame(results_frame, bg="#FFFFFF", padx=2, pady=2)
        item_frame.pack(fill='x', padx=2, pady=2)

        for col, (key, value) in enumerate(item.items()):
            # Create and place label
            label = Label(item_frame, text=f"{key.capitalize()}: ", font=("Inter", 12), bg="#FFFFFF", width=7, anchor="w")
            label.grid(row=i, column=col*2, padx=10, pady=10, sticky="w")

            # Create and place entry
            entry_bg_color = "#EEEEEE"
            entry = Entry(item_frame, bd=0, bg=entry_bg_color, fg="#000000", font=("Inter", 12), width=10)
            entry.insert(0, str(value))  # Ensure value is a string
            entry.grid(row=i, column=col*2+1, padx= 5, pady=5, sticky="w")

            # Add entry to the entries list
            if i >= len(entries):
                entries.append({})
            entries[i][key] = entry

        # Create and place update button
        update_button = Button(item_frame, text="Update", command=lambda idx=i: update_item(idx))
        update_button.grid(row=i, column=(col+1)*2, padx=5, pady=5, sticky="w")

def update_item(idx):
    updated_values = {}
    for key, entry in entries[idx].items():
        updated_values[key] = entry.get()
    print("Updated values for record", idx+1, ":", updated_values)
    

def display_categories():
    categories = library.get_categories()
    global category_combobox
    category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 10))
    category_combobox.set("All")  # Default value
    category_combobox.place(
        x=900.0,
        y=21.0,
        width=100.0,
        height=37.0
    )

admin= Admin()
library =Library_Form()

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
   if results_canvas.winfo_exists():  
        results_canvas.configure(scrollregion=results_canvas.bbox("all"))


entries = []


search_keys = []

display_categories()


window.resizable(False, False)
window.mainloop()