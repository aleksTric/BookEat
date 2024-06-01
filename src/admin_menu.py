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

    window_position_x = confirm_window.winfo_screenwidth() // 2 - 250
    window_position_y = confirm_window.winfo_screenheight() // 2 - 250
    confirm_window.geometry("500x500+{}+{}".format(window_position_x, window_position_y))

    text_padding = 30
    button_padding = 20
    font_size = 20

    confirm_window.config(bg="#7B3BE3")

    confirm_label = Label(confirm_window, text="Are you sure you want to log out?", bg="#7B3BE3", fg="#FFFFFF", font=("Inter", font_size))
    confirm_label.pack(pady=text_padding, padx=text_padding)

    yes_button = Button(confirm_window, text="Yes", command=confirm_window.destroy, bg="#FFFFFF", fg="#7B3BE3", font=("Inter", font_size), padx=button_padding, pady=button_padding)
    yes_button.pack(side="left", padx=button_padding)

    no_button = Button(confirm_window, text="No", command=confirm_window.destroy, bg="#FFFFFF", fg="#7B3BE3", font=("Inter", font_size), padx=button_padding, pady=button_padding)
    no_button.pack(side="right", padx=button_padding)

    confirm_window.grab_set()

    def on_yes_clicked():
        window.destroy()
        subprocess.Popen(["python3", "login_page.py"])

    yes_button.config(command=on_yes_clicked)
    confirm_window.eval(f'tk::PlaceWindow {str(confirm_window)} center')

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display_home_content():
    print("Home content displayed")
    toggle_button_image(button_1)
    subprocess.Popen(["python3", "admin_home_page.py"])

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

def display_announcements_content():
    print("Announcements content displayed")
    subprocess.Popen(["python3", "announcements_form.py"])
    toggle_button_image(button_22)

window = Tk()
window.title('Menu')
window.geometry("600x800")  # Increased width for more space
window.configure(bg="#7B3BE3")
window.iconphoto(True, PhotoImage(file="./assets/login/bookeat_icon.png"))

window_position_x = window.winfo_screenwidth() // 2 - 300  # Adjusted for increased width
window_position_y = window.winfo_screenheight() // 2 - 400
window.geometry("600x800+{}+{}".format(window_position_x, window_position_y))

canvas = Canvas(
    window,
    bg="#7B3BE3",
    height=800,
    width=600,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(relx=0.5, rely=0.5, anchor="center")

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

button_image_22 = PhotoImage(file=relative_to_assets("announcements-normal.png"))
button_22 = Button(
    canvas,
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=display_announcements_content,
    relief="flat",
    width=270,
    height=50,
    bg="#7B3BE3"
)
button_22.configure(bg="#7B3BE3")

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

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))

image_1 = canvas.create_image(
    300.0,  # Center X-coordinate adjusted for increased width
    55.0,  # Adjusted Y-coordinate to place at the top
    image=image_image_1
)

buttons = [button_1, button_2, button_22, button_3, button_4, button_5, button_6, button_7, button_8]
total_buttons = len(buttons)
initial_rely = 0.2  # Starting position for the first button
spacing = (0.95 - initial_rely) / (total_buttons - 1)  # Calculate spacing between buttons

for index, button in enumerate(buttons):
    button.place(relx=0.5, rely=initial_rely + index * spacing, anchor="center")

button_images = {
    button_1: {"normal": PhotoImage(file=relative_to_assets("home_normal.png")), "white": PhotoImage(file=relative_to_assets("home_white.png"))},
    button_2: {"normal": PhotoImage(file=relative_to_assets("users_normal.png")), "white": PhotoImage(file=relative_to_assets("users_white.png"))},
    button_22: {"normal": PhotoImage(file=relative_to_assets("announcements-normal.png")), "white": PhotoImage(file=relative_to_assets("announcements-white.png"))},
    button_3: {"normal": PhotoImage(file=relative_to_assets("add_book_normal.png")), "white": PhotoImage(file=relative_to_assets("add_book_white.png"))},
    button_4: {"normal": PhotoImage(file=relative_to_assets("library_normal.png")), "white": PhotoImage(file=relative_to_assets("library_white.png"))},
    button_5: {"normal": PhotoImage(file=relative_to_assets("study_rooms_normal.png")), "white": PhotoImage(file=relative_to_assets("study_rooms_white.png"))},
    button_6: {"normal": PhotoImage(file=relative_to_assets("book_requests_normal.png")), "white": PhotoImage(file=relative_to_assets("book_requests_white.png"))},
    button_7: {"normal": PhotoImage(file=relative_to_assets("notifications_normal.png")), "white": PhotoImage(file=relative_to_assets("notifications_white.png"))},
    button_8: {"normal": PhotoImage(file=relative_to_assets("logout_normal.png"))},
}

def toggle_button_image(button):
    button.config(image=button_images[button]["white"])
    for btn in button_images:
        if btn != button:
            btn.config(image=button_images[btn]["normal"])

window.resizable(False, False)
window.mainloop()
