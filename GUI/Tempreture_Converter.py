import tkinter as tk
from tkinter import messagebox
from functools import partial

temp_var="Celcius"
def temp_list(set_temp):
    global temp_var
    temp_var=set_temp

def temp_convert(label1,inputn):
    temp=inputn.get()
    if temp_var=="Celcius":
        f=((float(float(temp*9/5)))+35)
        label1.config(text="%.1f Farenheit" %f)
        messagebox.showinfo("Temperature Converter","Successfully Converted to Farenheit")
    if temp_var=="Farenheit":
        f=float((float(temp))-35*5/9)
        label1.config(text="%.1f Celcius" %f)
        messagebox.showinfo("Temperature Converter","Successfully Converted to Celcius")

root=tk.Tk()
root.geometry("400x250")
root.title("Temperature Converter")

root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(1,weight=1)
inputnum=tk.StringVar()
var=tk.StringVar()
input_label=tk.Label(root,text="Enter the temperature value: ")
input_entry=tk.Entry(root,textvariable=inputnum)
input_label.grid(row=1)
input_entry.grid(row=1,column=1)
result_label=tk.Label(root)
result_label.grid(row=3,columnspan= 4)

drop_down_list=["Celcius","Farenheit"]
drop_down=tk.OptionMenu(root,var,*drop_down_list,command=temp_list)

var.set(drop_down_list[0])
drop_down.grid(row=1,column=2)
temp_convert=partial(temp_convert,result_label,inputnum)
result_button=tk.Button(root,text="Convert",command=temp_convert)
result_button.grid(row=2,columnspan=2)

root.mainloop()