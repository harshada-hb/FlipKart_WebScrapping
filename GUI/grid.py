from tkinter import *
root=Tk()
mylabel=Label(root,text="Hello Python")
mylabel1=Label(root,text="My Name Is Harshada")
mylabel2=Label(root,text="Today is Wednesday")

mylabel.grid(row=0,column=5)
mylabel1.grid(row=5,column=5)
mylabel2.grid(row=10,column=5)
root.mainloop()