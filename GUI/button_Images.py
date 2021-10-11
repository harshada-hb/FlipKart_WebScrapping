from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Icon and Images")

mylabel=Label(root,text="Panda",font=20)
mylabel.pack()
img=ImageTk.PhotoImage(Image.open("panda.jpg"))
mylabel1=Label(image=img)
mylabel1.pack()
button_quit=Button(root,text='Exit',padx=5,pady=5,borderwidth=5,command=root.quit)
button_quit.pack()

root.mainloop()