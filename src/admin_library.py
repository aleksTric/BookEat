from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, Label, Scrollbar, VERTICAL, RIGHT, Y, LEFT, BOTH, NW
from tkinter import ttk
from classes import Admin, Library_Form

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def search():
    search_query = entry_1.get()
    
    results = admin.search_bycateg(search_query)
    print(results)
    display_results(results)  # Call display_results immediately after retrieving the search results


def display_results(results):
    for widget in results_frame.winfo_children():
        widget.destroy()

    for i, item in enumerate(results):
        item_frame = Frame(results_frame, bg="#FFFFFF", padx=15, pady=10)
        item_frame.pack(fill='x', padx=10, pady=10)

        for col, (key, value) in enumerate(item.items()):
            label = Label(item_frame, text=f"{key.capitalize()}: ", font=("Inter", 15), bg="white", fg="black", width=7, anchor="w")
            label.grid(row=i, column=col*2, padx=5, pady=5, sticky="w")

            entry_bg_color = "#EEEEEE"
            entry = Entry(item_frame, bd=0, bg=entry_bg_color, fg="#000000", font=("Inter", 15), width=10)
            entry.insert(0, str(value))
            entry.grid(row=i, column=col*2+1, padx=5, pady=5, sticky="w")

            if i >= len(entries):
                entries.append({})
            entries[i][key] = entry

        # Create and place update button
        update_button = Button(item_frame, text="Update", command=lambda idx=i: update_item(idx))  # Pass index 'i' to the update_item function
        update_button.grid(row=i, column=col*2+2, padx=5, pady=5, sticky="w", columnspan=2)

def update_item(idx):
    updated_values = {}
    for key, entry in entries[idx].items():
        updated_values[key] = entry.get()
    print("Updated values for record", idx+1, ":", updated_values)


def display_categories():
    categories = admin.library_form.get_categories()
    global category_combobox
    category_combobox = ttk.Combobox(window, values=categories, font=("Inter", 16))
    category_combobox.set("All")  # Default value
    category_combobox.place(
        x=900.0,
        y=21.0,
        width=100.0,
        height=37.0
    )

admin = Admin()

window = Tk()
window.geometry("1237x856")
window.configure(bg="#D9D9D9")
window.title("Library")
window.iconphoto(True, PhotoImage(file="./assets/login/bookeat_icon.png"))
# Calculate the position to center the window
window_position_x = window.winfo_screenwidth() // 2 - 600  # Half of window width (500 / 2)
window_position_y = window.winfo_screenheight() // 2 - 450  # Half of window height (800 / 2)

# Set the window geometry with the calculated position
window.geometry("1237x856+{}+{}".format(window_position_x, window_position_y))

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
    file=relative_to_assets("entry-1.png"))
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
    file=relative_to_assets("search.png"))
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
results_frame.place(x=50, y=100, width=1140, height=700)

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

# Creating an instance of Library_Form to fetch data from the database
library = Library_Form()

display_categories()


window.resizable(False, False)
window.mainloop()