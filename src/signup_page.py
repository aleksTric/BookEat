from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import tkinter.font as tkFont
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/kostaskaplanis/Desktop/build/assets/login")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Define entry widgets before using them in other functions
entry_1 = None
entry_2 = None
entry_3 = None

# Function to validate username
def validate_username(username):
    if not username:
        messagebox.showerror("Error", "Username cannot be empty.")
        return False
    elif len(username) < 4:
        messagebox.showerror("Error", "Username must be at least 4 characters long.")
        return False
    # Add more validation logic if needed
    return True

# Function to validate password
def validate_password(password):
    if not password:
        messagebox.showerror("Error", "Password cannot be empty.")
        return False
    # Add more validation logic if needed
    return True

# Function to validate repeated password
def validate_repeat_password(password, repeat_password):
    if password != repeat_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return False
    return True

def sign_up_user():
    global entry_1, entry_2, entry_3  # Declare variables as global so they can be accessed in this function
    username = entry_1.get()
    password = entry_2.get()
    repeat_password = entry_3.get()

    if not validate_username(username):
        return

    if not validate_password(password):
        return

    if not validate_repeat_password(password, repeat_password):
        return

    messagebox.showinfo("Success", "Registration successful!")  # Display success message

def open_login_page():
    
    window.destroy()  # Close the current window
    subprocess.Popen(["python3", "login_page.py"])

window = Tk()
window.wm_iconname("BookEat")
window.title("Create a Free Account")
window.iconphoto(True, PhotoImage(file="./assets/login/bookeat_icon.png"))
window.geometry("754x701")
window.configure(bg="#FFFFFF")

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
    644.0,
    anchor="nw",
    text="Already Registered ? ",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

button_login = Button(
    window,
    text="Sign in",
    font=("Inter Medium", 20),
    bg="#7B3BE3",
    fg="#333333",
    bd=0,
    command=open_login_page,
    relief="flat",
    cursor="heart"
)
button_login.place(x=435, y=640)  # Moved the button down

image_path = relative_to_assets("bookeat_github_logo2.png")
image = PhotoImage(file=image_path)
canvas.create_image(392.5, 152, anchor="center", image=image)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=sign_up_user,
    relief="flat"
)
button_2.place(
    x=257.0,
    y=550.0,
    width=283.0,
    height=76.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    398.0,
    341.5,
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
    y=340.0,
    width=264.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_2 = canvas.create_image(
    398.0,
    421.5,
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
    x=266.0,
    y=420.0,
    width=264.0,
    height=30.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_3 = canvas.create_image(
    398.0,
    511.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    insertbackground="#000000",
    font=tkFont.Font(family="Terminal", size=20),  
    show="*"
)
entry_3.place(
    x=266.0,
    y=510.0,
    width=264.0,
    height=30.0
)

canvas.create_text(
    339.0,
    310.0,
    anchor="nw",
    text="Username",
    fill="#333333",
    font=("Inter Bold", 24),
)

canvas.create_text(
    339.0,
    390.0,
    anchor="nw",
    text="Password",
    fill="#333333",
    font=("Inter Bold", 24),
)

canvas.create_text(
    309.0,
    480.0,
    anchor="nw",
    text="Repeat Password",
    fill="#333333",
    font=("Inter Bold", 24),
)

window.resizable(False, False)
window.mainloop()
