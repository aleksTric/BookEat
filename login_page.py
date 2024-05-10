from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Label
import tkinter.font as tkFont
import subprocess
import time
import math

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/kostaskaplanis/Desktop/build/assets/login")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Default account credentials
DEFAULT_USER = {"username": "user1", "password": "user1"}
DEFAULT_ADMIN = {"username": "admin", "password": "admin"}

from tkinter import Tk, Canvas, Label
import math

def open_welcome_window(username, user_type):
    welcome_window = Tk()
    welcome_window.geometry("400x200")
    welcome_window.title("Welcome")
    welcome_window.config(bg="#7B3BE3")

    # Create and pack the welcome label
    welcome_label = Label(welcome_window, text=f"Welcome, {username}!", font=("Inter Medium", 20), padx=20, pady=20, bg="#7B3BE3", fg="#FFFFFF")
    welcome_label.pack()

    # Create and pack the canvas for the loading animation
    canvas = Canvas(welcome_window, width=100, height=100, bg="#7B3BE3", highlightthickness=0)
    canvas.pack(pady=20)

    # Draw the loading animation
    def draw_loading():
        canvas.delete("loading")
        x_center, y_center = 50, 50
        radius = 30
        num_lines = 12
        angle_increment = 360 / num_lines
        line_length = 20

        for i in range(num_lines):
            angle_degrees = i * angle_increment
            angle_radians = math.radians(angle_degrees)
            x_start = x_center + radius * math.cos(angle_radians)
            y_start = y_center + radius * math.sin(angle_radians)
            x_end = x_center + (radius + line_length) * math.cos(angle_radians)
            y_end = y_center + (radius + line_length) * math.sin(angle_radians)
            canvas.create_line(x_start, y_start, x_end, y_end, fill="#FFFFFF", width=3, tags="loading")

        canvas.after(100, animate_loading)

    def animate_loading():
        canvas.move("loading", 0, 0)
        canvas.update()
        canvas.after(100, animate_loading)

    draw_loading()

    # Close the welcome window and open user home or admin home after 3 seconds
    if user_type == "user":
        welcome_window.after(3000, lambda: (welcome_window.destroy(), open_user_home()))
    elif user_type == "admin":
        welcome_window.after(3000, lambda: (welcome_window.destroy(), open_admin_home()))
    else:
        print("Unknown user type.")

    welcome_window.mainloop()


def open_user_home():
    window.destroy()  # Close the current window
    subprocess.Popen(["python3", "user_home.py"])

def open_admin_home():
    window.destroy()  # Close the current window
    subprocess.Popen(["python3", "admin_home.py"])

def user_exists_in_database(username):
    # Check if the provided username and password match the default user credentials
    if username == DEFAULT_USER["username"]:
        return True
    elif username == DEFAULT_ADMIN["username"]:
        return True
    return False

def validate_login(username, password):
    # Validate the login credentials against the default user
    if username == DEFAULT_USER["username"] and password == DEFAULT_USER["password"]:
        return True
    elif username == DEFAULT_ADMIN["username"] and password == DEFAULT_ADMIN["password"]:
        return True
    return False

def open_sign_up_page():
    window.destroy()  # Close the current window
    subprocess.Popen(["python3", "signup_page.py"])

def login_user():
    username = entry_1.get()
    password = entry_2.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    if not user_exists_in_database(username):
        messagebox.showerror("Error", "User does not exist.")
        return

    if not validate_login(username, password):
        messagebox.showerror("Error", "Invalid username or password.")
        return

    if username == DEFAULT_USER["username"]:  # Check if the logged-in user is the default user
        open_welcome_window(username, "user")
    elif username == DEFAULT_ADMIN["username"]:  # Check if the logged-in user is the default admin
        open_welcome_window(username, "admin")
    else:
        # Handle other cases if needed
        print("Invalid user type.")




window = Tk()
window.title("Login")
window.geometry("754x701")
window.configure(bg="#FFFFFF")
window.iconphoto(True, PhotoImage(file="./assets/login/bookeat_icon.png"))

canvas = Canvas(
    window,
    bg="#7B3BE3",
    height=881,
    width=780,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0, 
    793.0,
    781.0, 
    fill="#7B3BE3",
    outline=""
)

canvas.create_text(
    219.0,
    614.0,
    anchor="nw",
    text="Not Registered? ",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

button_signup = Button(
    window,
    text="Create a free account",
    font=("Inter Medium", 20),
    bg="#7B3BE3",
    fg="#333333",
    bd=0,
    command=open_sign_up_page,
    relief="flat",
    cursor="heart"
)
button_signup.place(x=375, y=610)

image_path = relative_to_assets("bookeat_github_logo2.png")
image = PhotoImage(file=image_path)
canvas.create_image(392.5, 162, anchor="center", image=image)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login_user,
    relief="flat"
)
button_1.place(
    x=257.0,
    y=522.0,
    width=283.0,
    height=76.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    398.0,
    361.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    insertbackground="#000000",
    font=tkFont.Font(family="System", size=20) 
)
entry_1.place(
    x=266.0,
    y=360.0,
    width=264.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_2 = canvas.create_image(
    402.0,
    451.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    insertbackground="#000000",
    font=tkFont.Font(family="Terminal", size=20),
    show="*"
)
entry_2.place(
    x=270.0,
    y=451.0,
    width=264.0,
    height=30.0
)

canvas.create_text(
    339.0,
    330.0,
    anchor="nw",
    text="Username",
    fill="#333333",
    font=("Inter Bold", 24),
)

canvas.create_text(
    339.0,
    420.0,
    anchor="nw",
    text="Password",
    fill="#333333",
    font=("Inter Bold", 24),
)

window.resizable(False, False)
window.mainloop()
