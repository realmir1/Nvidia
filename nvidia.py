from customtkinter import *
from PIL import Image
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox

nvd= CTk()

nvd.geometry("600x700")

nvd.resizable(0,0)


canvas = CTkCanvas(master=nvd, width=600, height=700)
canvas.grid(row=0, column=0)
background_image = PhotoImage(file="/Users/aliemirsertbas/Desktop/VSCO1prjct/CustomTKprjct.py/nvdia.png")
canvas.create_image(0, 0, image=background_image, anchor="nw")




newframe = CTkFrame(master=nvd,
                    width=560,
                    height=360,
                    corner_radius=30,
                    border_width=6,
                    border_color="#76B903",
                    fg_color="white",
                    bg_color="white"
                    )
newframe.place(relx=0.5,rely=0.53, anchor="center")


option1 = CTkOptionMenu(master=newframe,width=300)
option1.place(anchor="center", relx=0.5, rely=0.5)
nvd.mainloop()