import subprocess
from tkinter import Tk, Canvas, Button, Entry, PhotoImage, Toplevel, Label
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/kostaskaplanis/Desktop/build/assets/home")


def logout():
    confirm_window = Toplevel(window)
    confirm_window.title("Logout Confirmation")
    confirm_window.geometry("500x500")

    # Calculate padding and font size for larger window
    text_padding = 30
    button_padding = 20
    font_size = 20

    # Set background color to purple
    confirm_window.config(bg="#7B3BE3")

    confirm_label = Label(confirm_window, text="Are you sure you want to log out?", bg="#7B3BE3", fg="#FFFFFF", font=("Inter", font_size))  # Set text color to white and font size
    confirm_label.pack(pady=text_padding, padx=text_padding)

    yes_button = Button(confirm_window, text="Yes", command=confirm_window.destroy, bg="#FFFFFF", fg="#7B3BE3", font=("Inter", font_size), padx=button_padding, pady=button_padding)  # Set button color to white, text color to purple, and font size
    yes_button.pack(side="left", padx=button_padding)

    no_button = Button(confirm_window, text="No", command=confirm_window.destroy, bg="#FFFFFF", fg="#7B3BE3", font=("Inter", font_size), padx=button_padding, pady=button_padding)  # Set button color to white, text color to purple, and font size
    no_button.pack(side="right", padx=button_padding)

    confirm_window.grab_set()

    # If "Yes" is clicked, destroy the current window and open the login page using subprocess
    def on_yes_clicked():
        window.destroy()
        subprocess.Popen(["python3", "login_page.py"])

    yes_button.config(command=on_yes_clicked)

    # Center the window
    confirm_window.eval(f'tk::PlaceWindow {str(confirm_window)} center')


def delete_elements_greater_than_x(x_limit):
    # Get all items on the canvas
    all_items = canvas.find_all()
    for item in all_items:
        # Get the coordinates of the current item
        coords = canvas.coords(item)
        if coords and coords[0] > x_limit:
            # Delete the item if its x-coordinate is greater than the limit
            canvas.delete(item)
    
    # Also, delete buttons and entries based on their x-coordinate
    for widget in window.winfo_children():
        if widget.winfo_class() == "Button" or widget.winfo_class() == "Entry":
            x_position = widget.winfo_x()
            if x_position > x_limit:
                widget.destroy()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_book_details():
    # Open book details page using subprocess
    subprocess.Popen(["python3", "book_details_page.py"])
def display_home_content():
   
    print("Home content displayed")
    toggle_button_image(button_1)
    delete_elements_greater_than_x(220.0)
   
   

    canvas.create_text(
    304.0,
    95.0,
    anchor="nw",
    text="Recently Added",
    fill="#333333",
    font=("Inter Bold", 25 * -1),
    tags="red_rectangle"
    )

    canvas.create_text(
        292.0,
        279.0,
        anchor="nw",
        text="Recommended",
        fill="#333333",
        font=("Inter Bold", 25 * -1),
        tags="red_rectangle"
    )
    canvas.create_text(
        308.0,
        442.0,
        anchor="nw",
        text="Announcements",
        fill="#333333",
        font=("Jura SemiBold", 25 * -1)
    )
    canvas.create_rectangle(
    297.0,
    143.0,
    1250.0,
    254.0,
    fill="#FFFFFF",
    outline="",
    tags="red_rectangle")

    canvas.create_rectangle(
        296.0,
        330.0,
        1249.0,
        434.0,
        fill="#FFFFFF",
        outline="",
        tags="red_rectangle")

    canvas.create_rectangle(
        297.0,
        489.0,
        1250.0,
        760.0,
        fill="#FFFFFF",
        outline="",
        tags="red_rectangle")


    canvas.create_rectangle(
        1085.0,
        13.0,
        1445.0,
        113.0,
        fill="#FFFFFF",
        outline="",
        tags="red_rectangle")
    
    
    entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
    )
    entry_1.place(
        x=487.0,
        y=21.0,
        width=202.0,
        height=52.0
    )

    canvas.create_rectangle(
        330.0,
        162.0,
        408.0,
        235.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        330.0,
        346.0,
        408.0,
        419.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        331.0,
        505.0,
        588.0,
        764.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        643.0,
        505.0,
        900.0,
        764.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        955.0,
        504.0,
        1212.0,
        763.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        662.0,
        162.0,
        740.0,
        235.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        662.0,
        346.0,
        740.0,
        419.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        978.0,
        162.0,
        1056.0,
        235.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        978.0,
        346.0,
        1056.0,
        419.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        496.0,
        162.0,
        574.0,
        235.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        496.0,
        346.0,
        574.0,
        419.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        828.0,
        162.0,
        906.0,
        235.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        828.0,
        346.0,
        906.0,
        419.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        1118.0,
        162.0,
        1196.0,
        235.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        1118.0,
        346.0,
        1196.0,
        419.0,
        fill="#D9D9D9",
        outline="")

    entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
    588.0,
    48.0,
    image=entry_image_1
    )

    canvas.create_text(
        533.0,
        30.0,
        anchor="nw",
        text="Search...",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas.create_text(
        1178.0,
        18.0,
        anchor="nw",
        text="Kostas",
        fill="#000000",
        font=("Inter SemiBold", 25 * -1)
    )

    canvas.create_rectangle(
        1349.0,
        21.0,
        1436.0,
        100.0,
        fill="#000000",
        outline="")

    

    canvas.create_rectangle(
        1116.0,
        51.0,
        1336.0,
        61.0,
        fill="#000000",
        outline=""
    )
    entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
    )
    entry_1.place(
        x=487.0,
        y=21.0,
        width=202.0,
        height=52.0
    )
    



def display_friends_content():
    print("Friends content displayed")
    toggle_button_image(button_3)
    # Clear the canvas
    #canvas.delete("red_rectangle")
    delete_elements_greater_than_x(220.0)
    
    # Add your new content for the Friends page
    canvas.create_text(
        250.0,
        100,
        anchor="nw",
        text="Friends List",
        fill="#333333",
        font=("Inter Bold", 25)
    )


def display_library_content():
    print("Library content displayed")
    delete_elements_greater_than_x(220.0)
    toggle_button_image(button_4)
    canvas.create_text(
        250.0,
        100,
        anchor="nw",
        text="My Library Page",
        fill="#333333",
        font=("Inter Bold", 25)
    )

def display_study_rooms_content():
    print("Study Rooms content displayed")
    delete_elements_greater_than_x(220.0)
    toggle_button_image(button_5)

    canvas.create_text(
        250.0,
        100,
        anchor="nw",
        text="Study Rooms Page",
        fill="#333333",
        font=("Inter Bold", 25)
    )

def display_notifications_content():
    print("Notifications content displayed")
    delete_elements_greater_than_x(220.0)
    toggle_button_image(button_6)

    canvas.create_text(
        250.0,
        100,
        anchor="nw",
        text="Notifications Page",
        fill="#333333",
        font=("Inter Bold", 25)
    )

def display_announcements_content():
    print("Announcements content displayed")
    delete_elements_greater_than_x(220.0)

    canvas.create_text(
        250.0,
        100,
        anchor="nw",
        text="Announcements Page",
        fill="#333333",
        font=("Inter Bold", 25)
    )


window = Tk()
window.geometry("1454x856")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=856,
    width=1454,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    220.0,
    0.0,
    1454.0,
    856.0,
    fill="red",
    outline="",
    tags="red_rectangle"
)

canvas.create_rectangle(
    0.0,
    0.0,
    219.0,
    856.0,
    fill="#7B3BE3",
    outline="")






button_image_1 = PhotoImage(
    file=relative_to_assets("home_white.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=display_home_content,
    relief="flat"
)
button_1.place(
    x=1.0,
    y=152.0,
    width=170.0,
    height=52.0
)



button_image_3 = PhotoImage(
    file=relative_to_assets("friends_normal.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=display_friends_content,
    relief="flat"
)
button_3.place(
    x=1.0,
    y=235.0,
    width=170.0,
    height=52.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("my_library_normal.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=display_library_content,
    relief="flat"
)
button_4.place(
    x=1.0,
    y=300.0,
    width=170.0,
    height=52.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("study_rooms_normal.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=display_study_rooms_content,
    relief="flat"
)
button_5.place(
    x=1.0,
    y=363.0,
    width=170.0,
    height=52.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("notifications_normal.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=display_notifications_content,
    relief="flat"
)
button_6.place(
    x=1.0,
    y=434.0,
    width=170.0,
    height=52.0
)
button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))

button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat"
    )
button_8.place(
    x=1.0,
    y=606.0,
    width=150,
    height=45.0
)

image_image_1 = PhotoImage( file=relative_to_assets("image_1.png"))
    
image_1 = canvas.create_image(
    81.0,
    72.0,
    image=image_image_1
)


# Dictionary to store button images and their corresponding alternate images
button_images = {
    button_1: {"normal": PhotoImage(file=relative_to_assets("home_normal.png")), "white": PhotoImage(file=relative_to_assets("home_white.png"))},
    button_3: {"normal": PhotoImage(file=relative_to_assets("friends_normal.png")), "white": PhotoImage(file=relative_to_assets("friends_white.png"))},
    button_4: {"normal": PhotoImage(file=relative_to_assets("my_library_normal.png")), "white": PhotoImage(file=relative_to_assets("my_library_white.png"))},
    button_5: {"normal": PhotoImage(file=relative_to_assets("study_rooms_normal.png")), "white": PhotoImage(file=relative_to_assets("study_rooms_white.png"))},
    button_6: {"normal": PhotoImage(file=relative_to_assets("notifications_normal.png")), "white": PhotoImage(file=relative_to_assets("notifications_white.png"))},
    
}

# Define a function to toggle button images
def toggle_button_image(button):
    # Set the clicked button to its white state
    button.config(image=button_images[button]["white"])
    # Iterate through all other buttons
    for btn in button_images:
        if btn != button:
            # Set other buttons to their normal state
            btn.config(image=button_images[btn]["normal"])



button_1.invoke()
window.resizable(False, False)
window.mainloop()
