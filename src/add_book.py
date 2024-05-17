import tkinter as tk
from pathlib import Path
from admin import Admin
import tkinter.messagebox
from tkinter import filedialog


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\lessons\BookEat\src\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MyApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("My Application")
        self.master.geometry("1237x856")
        self.master.configure(bg="#FFFFFF")
        self.admin = Admin()
        self.create_widgets()
        

    def create_widgets(self):
        self.canvas = tk.Canvas(
            self.master,
            bg="#FFFFFF",
            height=856,
            width=1237,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack()

        # Define and place other GUI elements here using self.canvas.create_XXX methods

        # Example:
        self.button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = tk.Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.upload_json,
            relief="flat"
        )
        self.button_1.place(x=173.0, y=157.0, width=324.0, height=44.0)

        # Continue defining other GUI elements similarly
        
        self.button_image_2 = tk.PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 =tk.Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_book,
            relief="flat"
        )
        self.button_2.place(x=509.0, y=671.0, width=248.0, height=90.0)

        self.button_image_3 = tk.PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 =tk.Button(
            self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_category,
            relief="flat"
        )
        self.button_3.place(x=746.0, y=157.0, width=329.0, height=59.0)

        self.button_image_4 = tk.PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_4 =tk.Button(
            self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(x=173.0, y=100.0, width=150.0, height=34.0)

        self.canvas.place(x=0, y=0)
        # Create a rectangle on the canvas
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1454.0,
            856.0,
            fill="#D9D9D9",
            outline=""
        ) 
        
        self.canvas.create_rectangle(
             59.0,
            23.0,
            1136.0,
            844.0,
           fill="#FFFFFF",
           outline="")

        self.canvas.create_text(
            230.0,
            212.0,
            anchor="nw",
            text="JSON",
            fill="#333333",
            font=("Inter Light", 15 * -1)
        )

        self.canvas.create_rectangle(
            204.0,
            212.0,
            219.0,
            227.0,
            fill="#9B9B9B",
            outline="")
        
        self.canvas.create_rectangle(
            152.0,
            237.0,
            1082.0,
            822.0,
            fill="#D9D9D9",
            outline="")
        
         # Create a PhotoImage object and store it as an attribute
        self.image_1_photo = tk.PhotoImage(file=relative_to_assets("image_1.png"))

        # Create an image on the canvas using the stored PhotoImage object
        self.image_1 = self.canvas.create_image(
            633.0,
            276.0,
            image=self.image_1_photo
        )

        # Create a PhotoImage object for the entry background image and store it as an attribute
        self.entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))

        # Create an image on the canvas as the entry background using the stored PhotoImage object
        self.entry_bg_1 = self.canvas.create_image(
            614.0,
            504.5,
            image=self.entry_image_1
        )

        # Create an Entry widget
        self.entry_1 = tk.Entry(
            self.master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 20)
        )
        self.entry_1.place(
            x=175.0,
            y=481.0,
            width=878.0,
            height=45.0
        )

        self.entry_image_2 = tk.PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            617.0,
            421.5,
            image=self.entry_image_2
        )
        self.entry_2 = tk.Entry(
            self.master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 20)
        )
        self.entry_2.place(
            x=178.0,
            y=398.0,
            width=878.0,
            height=45.0
        )

        self.entry_image_3 = tk.PhotoImage(file=relative_to_assets("entry_3.png"))
        self.entry_bg_3= self.canvas.create_image(
            617.0,
            335.5,
            image=self.entry_image_3
        )
        self.entry_3 = tk.Entry(
            self.master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 20)
        )
        self.entry_3.place(
            x=178.0,
            y=312.0,
            width=878.0,
            height=45.0
        )

        self.entry_image_4 = tk.PhotoImage(file=relative_to_assets("entry_4.png"))
        self.entry_bg_4= self.canvas.create_image(
            613.5,
            599.5,
            image=self.entry_image_4
        )
        self.entry_4 = tk.Entry(
            self.master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 20)
        )
        self.entry_4.place(
            x=175.0,
            y=576.0,
            width=878.0,
            height=45.0
        )
        
        self.canvas.create_text(
        174.0,
        280.0,
        anchor="nw",
        text=" Title",
        fill="#333333",
        font=("Inter Light", 30 * -1)
        )

        self.canvas.create_text(
        180.0,
        360.0,
        anchor="nw",
        text="Category",
        fill="#333333",
        font=("Inter Light", 30 * -1)
        )

        self.canvas.create_text(
        180.0,
        445.0,
        anchor="nw",
        text="Author",
        fill="#333333",
        font=("Inter Light", 30 * -1)
        )

        self.canvas.create_text(
        174.0,
        539.0,
        anchor="nw",
        text=" Date",
        fill="#333333",
        font=("Inter Light", 30 * -1)
        )

        self.canvas.create_text(
        195.0,
        69.0,
        anchor="nw",
        text="file :",
        fill="#000000",
        font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
        786.0,
        48.0,
        anchor="nw",
        text="category:",
        fill="#333333",
        font=("Inter Light", 32 * -1)
        )

        self.canvas.create_rectangle(
        777.0,
        88.0,
        1051.0,
        143.0,
        fill="#D9D9D9",
        outline="")

        self.entry_image_5 = tk.PhotoImage(file=relative_to_assets("entry_5.png"))
        self.entry_bg_5= self.canvas.create_image(
            914.5,
            116.0,
            image=self.entry_image_5
        )
        self.entry_5 = tk.Entry(
            self.master,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 16)
        )
        self.entry_5.place(
            x=791.0,
            y=98.0,
            width=247.0,
            height=34.0
        )
    
    def add_category(self):
       # Clear the text of entry_5
        if(self.entry_5.get() ==""):
          tkinter.messagebox.showerror("Error", "You need to fill all fields.")
          return
        else:
         category =self.entry_5.get()
         self.admin.add_category(category)
         self.entry_5.delete(0, tk.END)

    def add_book(self):
        if (self.entry_1.get() == "" or self.entry_2.get() == "" or self.entry_3.get() == "" or self.entry_4.get() == ""):
         tkinter.messagebox.showerror("Error", "You need to fill all fields.")
         return
        else:
         
         title = self.entry_3.get()
         category= self.entry_2.get()
         author=self.entry_1.get()
         date=self.entry_4.get()
         
         self.admin.add_book(title,category,author,date)
         self.entry_1.delete(0, tk.END)
         self.entry_2.delete(0, tk.END)
         self.entry_3.delete(0, tk.END)
         self.entry_4.delete(0, tk.END)
   
    def upload_json(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("File selected:", file_path)
            self.admin.upload_json(file_path)

def main():
    root = tk.Tk()
    app = MyApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()