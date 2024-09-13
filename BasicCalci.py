import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math

window = tk.Tk()
window.title('Calculator')

frame = tk.Frame(master=window, bg="silver", padx=50, pady=30)
frame.pack()

label1 = tk.Label(master=frame, text='BASIC CALCULATOR', bg='orange', foreground='white')
label1.grid(row=0, column=0, columnspan=4)

label2 = tk.Label(master=frame, text='\n', bg='silver')
label2.grid(row=0, column=0)

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=4, width=31)
entry.grid(row=1, column=0, columnspan=4, ipady=2, pady=2, rowspan=2)

def touch(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)
    
def delete():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

    
def root():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
        
def sin_operation():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
        
def cos_operation():
    try:
        result =math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
        
def tan_operation():
    try:
        result =math.tan(math.radians(int(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

num1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=6, height=2, command=lambda: touch(1))
num1.grid(row=5, column=0)

num2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=6, height=2, command=lambda: touch(2))
num2.grid(row=5, column=1)

num3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=6, height=2, command=lambda: touch(3))
num3.grid(row=5, column=2)

add = tk.Button(master=frame, text="+", padx=15, pady=5, width=6, height=2, command=lambda: touch('+'))
add.grid(row=5, column=3)

num4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=6, height=2, command=lambda: touch(4))
num4.grid(row=6, column=0)

num5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=6, height=2, command=lambda: touch(5))
num5.grid(row=6, column=1)

num6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=6, height=2, command=lambda: touch(6))
num6.grid(row=6, column=2)

subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=6, height=2, command=lambda: touch('-'))
subtract.grid(row=6 ,column=3)

num7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=6, height=2, command=lambda: touch(7))
num7.grid(row=7, column=0)

num8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=6, height=2, command=lambda: touch(8))
num8.grid(row=7, column=1)

num9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=6, height=2, command=lambda: touch(9))
num9.grid(row=7, column=2)

multiply = tk.Button(master=frame, text="x", padx=15, pady=5, width=6, height=2, command=lambda: touch('*'))
multiply.grid(row=7, column=3)

num0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=6, height=2, command=lambda: touch(0))
num0.grid(row=8, column=1)

div = tk.Button(master=frame, text="/", padx=15, pady=5, width=6, height=2, command=lambda: touch('/'))
div.grid(row=8, column=3)

modulus = tk.Button(master=frame, text="%", padx=15, pady=5, width=6, height=2, command=lambda: touch('%'))
modulus.grid(row=8, column=2)

point = tk.Button(master=frame, text=".", padx=15, pady=5, width=6, height=2, command=lambda: touch('.'))
point.grid(row=8, column=0)

button_delete= tk.Button(master=frame, text="delete", padx=15, pady=5, width=6, height=2, command=delete)
button_delete.grid(row=3, column=0)

button_clear = tk.Button(master=frame, text="clear", padx=15, pady=5, width=6, height=2, command=clear)
button_clear.grid(row=3, column=1)

button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=14, height=2, command=equal)
button_equal.grid(row=3, column=2,columnspan=2)

button_sin = tk.Button(master=frame, text="sin", padx=15, pady=5, width=6, height=2, command=sin_operation)
button_sin.grid(row=4, column=0)

button_cos = tk.Button(master=frame, text="cos", padx=15, pady=5, width=6, height=2, command=cos_operation)
button_cos.grid(row=4, column=1)

button_tan = tk.Button(master=frame, text="tan", padx=15, pady=5, width=6, height=2, command=tan_operation)
button_tan.grid(row=4, column=2)

button_root= tk.Button(master=frame, text="√", padx=15, pady=5, width=6, height=2, command=root)
button_root.grid(row=4, column=3)

window.mainloop()
