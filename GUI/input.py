from tkinter import *
root=Tk()

a=Entry(root,width=50,fg="green",borderwidth=5)
a.pack()
a.insert(1,"Enter your name: ")

def clickme():
    l=int(len(a.get()))
    mylabel=Label(root,text="Hello "+a.get()+" !")
    mylabel1=Label(root,text="Length of your name: ")
    mylabel2=Label(root,text=l)
    mylabel.pack()
    mylabel1.pack()
    mylabel2.pack()

button=Button(root,text="Insert",command=clickme)
button.pack()
root.mainloop()