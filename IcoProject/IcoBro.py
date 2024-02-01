import os
from PIL import Image, ImageTk
import tkinter as tk 
from tkinter import filedialog
from customtkinter import *

class IcoBro:
    def __init__(self, root):
        root.title("ICO Bro")
        root.geometry("500x350")
        root.eval('tk::PlaceWindow . center')
        root.resizable(False, False)
        set_appearance_mode("dark")

        btn_upload = CTkButton(master=root,  text="Upload Image", corner_radius=32, fg_color="darkblue", hover_color="blue", font=("Arial", 16))
        btn_upload.place(relx=0.3, rely=0.5, anchor="center")
        btn_convert = CTkButton(master=root, text="Convert Image", corner_radius=32, fg_color="darkblue", hover_color="blue", font=("Arial", 16))
        btn_convert.place(relx=0.7, rely=0.5, anchor="center")

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