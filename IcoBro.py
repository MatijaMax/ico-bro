import os
from PIL import Image, ImageTk
import tkinter as tk 
from tkinter import filedialog, messagebox
from customtkinter import *

class IcoBro:
    def __init__(self, root):
        root.title("ICO Bro")
        root.geometry("500x350")
        root.eval('tk::PlaceWindow . center')
        root.resizable(False, False)
        set_appearance_mode("dark")
        bg_image = CTkImage(Image.open("truckbg.jpg"), size=(500, 350))
        label_bg = CTkLabel( root, image = bg_image, text="") 
        label_bg.place(x = 0, y = 0) 

        self.btn_convert = CTkButton(master=root, command=self.convert_image,  text="Convert to ICO",corner_radius=1,  fg_color="darkred", hover_color="orange", font=("Arial", 16))
        self.btn_convert.place(relx=0.7, rely=0.9, anchor="center")
        self.btn_convert.configure(state=DISABLED)

        self.btn_upload = CTkButton(master=root, command=self.upload_image, text="Upload Image",corner_radius=1,  fg_color="darkred", hover_color="orange", font=("Arial", 16))
        self.btn_upload.place(relx=0.3, rely=0.9, anchor="center")

        self.file_path = None
        self.loaded_image = None


    def upload_image(self):
        self.file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.file_path:
            self.loaded_image = CTkImage(Image.open(self.file_path), size=(100, 100))
            label = CTkLabel( root, image = self.loaded_image, text="") 
            label.place(x = 25, y = 25) 
            self.btn_convert.configure(state=NORMAL)

    def convert_image(self):
        if self.loaded_image:
            directory =filedialog.askdirectory(title="Choose Directory to Save Converted Image")
            if self.file_path:
                try:
                    img = Image.open(self.file_path)
                    directory = os.path.join(directory, 'IcoBro.ico')
                    img.save(directory)
                    messagebox.showinfo("Conversion Complete", "Image has been converted to ICO format and saved.")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("No Image Selected", "Please select an image first.")

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    window.geometry(f"+{x_coordinate}+{y_coordinate}")


if __name__ == "__main__":
    root = CTk()
    IcoBroApp = IcoBro(root)
    root.mainloop()