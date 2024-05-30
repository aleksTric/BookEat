import subprocess
from tkinter import Tk, Canvas, Button, Entry, PhotoImage, Toplevel, Label, Scrollbar
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/kostaskaplanis/Desktop/Bookeat/src/assets/admin")

def logout():
    confirm_window = Toplevel(window)
    confirm_window.title("Logout Confirmation")
    confirm_window.config(bg="#7B3BE3")
    confirm_window.iconphoto(True, PhotoImage(file="./assets/login/bookeat_icon.png"))

    # Calculate the position to center the window
    window_position_x = confirm_window.winfo_screenwidth() // 2 - 250  # Half of window width (500 / 2)
    window_position_y = confirm_window.winfo_screenheight() // 2 - 250  # Half of window height (500 / 2)

    # Set the window geometry with the calculated position
    confirm_window.geometry("500x500+{}+{}".format(window_position_x, window_position_y))


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

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display_home_content():
    print("Home content displayed")
    toggle_button_image(button_1)
    subprocess.Popen(["python3", "admin_home_page.py"])

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(588.0, 48.0, image=entry_image_1)

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
        outline=""
    )

    canvas.create_rectangle(
        1116.0,
        51.0,
        1336.0,
        61.0,
        fill="#000000",
        outline=""
    )

def display_users_content():
    print("Friends content displayed")
    toggle_button_image(button_2)

def display_add_book_content():
    print("Add Book content displayed")
    toggle_button_image(button_3)
    subprocess.Popen(["python3", "admin_add_book.py"])

def display_library_content():
    print("Library content displayed")
    toggle_button_image(button_4)
    subprocess.Popen(["python3", "admin_library.py"])

def display_study_rooms_content():
    print("Study Rooms content displayed")
    toggle_button_image(button_5)
    subprocess.Popen(["python3", "rooms_admin.py"])


def display_book_requests_content():
    print("Book Requests content displayed")
    toggle_button_image(button_6)
    subprocess.Popen(["python3", "admin_book_requests_page.py"])

def display_notifications_content():
    print("Notifications content displayed")
    toggle_button_image(button_7)
    # subprocess.Popen(["python3", "admin_notifications_page.py"])


def display_announcements_content():
    print("Announcements content displayed")

window = Tk()
window.title('Menu')
window.geometry("500x800")  # Resize window
window.configure(bg="#7B3BE3")  # Set background color to purple
window.iconphoto(True, PhotoImage(file="./assets/login/bookeat_icon.png"))

# Calculate the position to center the window
window_position_x = window.winfo_screenwidth() // 2 - 250  # Half of window width (500 / 2)
window_position_y = window.winfo_screenheight() // 2 - 400  # Half of window height (800 / 2)

# Set the window geometry with the calculated position
window.geometry("500x800+{}+{}".format(window_position_x, window_position_y))

canvas = Canvas(
    window,
    bg="#7B3BE3",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(relx=0.5, rely=0.5, anchor="center")  # Center the canvas

button_image_1 = PhotoImage(file=relative_to_assets("home_normal.png"))
button_1 = Button(
    canvas,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=display_home_content,
    relief="flat",
    width=150,
    height=50
)
button_1.place(relx=0.5, rely=0.2, anchor="center")  # Center the button vertically

button_image_2 = PhotoImage(file=relative_to_assets("users_normal.png"))
button_2 = Button(
    canvas,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=display_users_content,
    relief="flat",
    width=150,
    height=50
)
button_2.place(relx=0.5, rely=0.3, anchor="center")  # Center the button vertically
button_image_3 = PhotoImage(file=relative_to_assets("add_book_normal.png"))
button_3 = Button(
    canvas,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=display_add_book_content,
    relief="flat",
    width=150,
    height=50
)
button_3.place(relx=0.5, rely=0.3, anchor="center")  # Center the button vertically

button_image_4 = PhotoImage(file=relative_to_assets("library_normal.png"))
button_4 = Button(
    canvas,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=display_library_content,
    relief="flat",
    width=160,
    height=50
)
button_4.place(relx=0.5, rely=0.4, anchor="center")  # Center the button vertically

button_image_5 = PhotoImage(file=relative_to_assets("study_rooms_normal.png"))
button_5 = Button(
    canvas,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=display_study_rooms_content,
    relief="flat",
    width=170,
    height=50
)
button_5.place(relx=0.5, rely=0.5, anchor="center")  # Center the button vertically
button_image_6 = PhotoImage(file=relative_to_assets("book_requests_normal.png"))
button_6 = Button(
    canvas,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=display_book_requests_content,
    relief="flat",
    width=190,
    height=50
)
button_6.place(relx=0.5, rely=0.5, anchor="center")  # Center the button vertically

button_image_7 = PhotoImage(file=relative_to_assets("notifications_normal.png"))
button_7 = Button(
    canvas,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=display_notifications_content,
    relief="flat",
    width=180,
    height=50
)
button_7.place(relx=0.4, rely=0.6, anchor="center")  # Center the button vertically

button_image_8 = PhotoImage(file=relative_to_assets("logout_normal.png"))
button_8 = Button(
    canvas,
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat",
    width=150,
    height=50
)
button_8.place(relx=0.5, rely=0.8, anchor="center")  # Center the button vertically

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))

# Place the image at the center and above all buttons
image_1 = canvas.create_image(
    400.0,  # Adjusted X-coordinate to place at the center horizontally
    55.0,  # Adjusted Y-coordinate to place at the center vertically
    image=image_image_1
)

button_1.place(relx=0.5, rely=0.25, anchor="center")  # Adjusted Y-coordinate for button_1
button_2.place(relx=0.5, rely=0.35, anchor="center")  # Adjusted Y-coordinate for button_2
button_3.place(relx=0.5, rely=0.45, anchor="center")  # Adjusted Y-coordinate for button_2

button_4.place(relx=0.5, rely=0.55, anchor="center")  # Adjusted Y-coordinate for button_4
button_5.place(relx=0.5, rely=0.65, anchor="center")  # Adjusted Y-coordinate for button_5
button_6.place(relx=0.5, rely=0.75, anchor="center")  # Adjusted Y-coordinate for button_5
button_7.place(relx=0.5, rely=0.85, anchor="center")  # Adjusted Y-coordinate for button_7

button_8.place(relx=0.5, rely=0.95, anchor="center")  # Adjusted Y-coordinate for button_8


# Dictionary to store button images and their corresponding alternate images
button_images = {
    button_1: {"normal": PhotoImage(file=relative_to_assets("home_normal.png")), "white": PhotoImage(file=relative_to_assets("home_white.png"))},
    button_2: {"normal": PhotoImage(file=relative_to_assets("users_normal.png")), "white": PhotoImage(file=relative_to_assets("users_white.png"))},
    button_3: {"normal": PhotoImage(file=relative_to_assets("add_book_normal.png")), "white": PhotoImage(file=relative_to_assets("add_book_white.png"))},
    button_4: {"normal": PhotoImage(file=relative_to_assets("library_normal.png")), "white": PhotoImage(file=relative_to_assets("library_white.png"))},
    button_5: {"normal": PhotoImage(file=relative_to_assets("study_rooms_normal.png")), "white": PhotoImage(file=relative_to_assets("study_rooms_white.png"))},
    button_6: {"normal": PhotoImage(file=relative_to_assets("book_requests_normal.png")), "white": PhotoImage(file=relative_to_assets("book_requests_white.png"))},
    button_7: {"normal": PhotoImage(file=relative_to_assets("notifications_normal.png")), "white": PhotoImage(file=relative_to_assets("notifications_white.png"))},
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

# button_1.invoke()
window.resizable(False, False)
window.mainloop()
