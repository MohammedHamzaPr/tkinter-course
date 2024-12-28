from tkinter import Tk
from PIL import Image, ImageTk
root - Tk()
root.geometry('500x500+450+100')
root.title('Tkinter with Mohammed')
root.config(background="#262626')
photo_app = ImageTk. Photo Image (Image.open('icon.png'))
root.iconphoto(True, photo_app)
root.resizable (width=False,height=False)
root.mainloop()