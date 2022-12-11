# Libraries Used
from tkinter import *
import math as m
root = Tk()
# required functions
def click(number):
    current = input_space.get()
    input_space.delete(0,END)
    input_space.insert(0,str(current)+str(number))
def clear():
    input_space.delete(0,END)
def add(): 
    a1 = input_space.get()
    global g
    global ops
    ops = "add"
    g = int(a1)
    input_space.delete(0,END)
def subs():
    a1 = input_space.get()
    global g
    global ops
    ops="subs"
    g = int(a1)
    input_space.delete(0,END)
def divide():
    a1 = input_space.get()
    global g
    global ops
    ops="div"
    g = int(a1)
    input_space.delete(0,END)
def multi():
    a1 = input_space.get()
    global g
    global ops
    ops="mult"
    g = int(a1)
    input_space.delete(0,END)
def square():
    a1 = input_space.get()
    global g
    global ops
    ops="sq"
    g = int(a1)
    input_space.delete(0,END)
def root1():
    a1 = input_space.get()
    global g
    global ops
    ops="root"
    g = int(a1)
    input_space.delete(0,END)
def sin():
    a1 = input_space.get()
    global g
    global ops
    ops="sin"
    g = int(a1)
    input_space.delete(0,END)
def cos():
    a1 = input_space.get()
    global g
    global ops
    ops="cos"
    g = int(a1)
    input_space.delete(0,END)
def equal():
    a2 = input_space.get()
    input_space.delete(0,END)
    if ops=="add":
        input_space.insert(0,g+int(a2))
    if ops=="subs":
        input_space.insert(0,g-int(a2))
    if ops=="div":
        # input_space.insert(0,g/int(a2))
        input_space.insert(0,"Bhag bhosideke")
    if ops=="mult":
        input_space.insert(0,g*int(a2))
    if ops=="sq":
        input_space.insert(0,g**2)
    if ops=="root":
        input_space.insert(0,g**(1/2))
    if ops=="sin":
        input_space.insert(0,m.asin(g))
    if ops=="cos":
        input_space.insert(0,m.acos(g))
# initialiazing buttons and entry space
input_space = Entry(root,width=50,borderwidth=7)
button1 = Button(root,text = 1,padx=80,pady=15,command = lambda: click(1))
button2 = Button(root,text = 2,padx=80,pady=15,command = lambda: click(2))
button3 = Button(root,text = 3,padx=80,pady=15,command = lambda: click(3))
button4 = Button(root,text = 4,padx=80,pady=15,command = lambda: click(4))
button5 = Button(root,text = 5,padx=80,pady=15,command = lambda: click(5))
button6 = Button(root,text = 6,padx=80,pady=15,command = lambda: click(6))
button7 = Button(root,text = 7,padx=80,pady=15,command = lambda: click(7))
button8 = Button(root,text = 8,padx=80,pady=15,command = lambda: click(8))
button9 = Button(root,text = 9,padx=80,pady=15,command = lambda: click(9))
button0 = Button(root,text = 0,padx=80,pady=15,command = lambda: click(0))
button_add = Button(root,text = "+",padx=80,pady=15,command = lambda: add())
button_substract = Button(root,text = "-",padx=80,pady=15,command = lambda: subs())
button_mult = Button(root,text = "x",padx=80,pady=15,command = lambda: multi())
button_div = Button(root,text = "/",padx=80,pady=15,command = lambda: divide())
button_square = Button(root,text = "x**2",padx=73,pady=15,command = lambda: square())
button_root = Button(root,text = "root(x)",padx=70,pady=15,command = lambda: root1())
button_sin = Button(root,text = "sinX",padx=70,pady=15,command = lambda: sin())
button_cos = Button(root,text = "cosX",padx=70,pady=15,command = lambda: cos())
button_clear = Button(root,text="clear",padx=75,pady=15,command = clear)
button_equals = Button(root,text="=",padx=80,pady=15,command = lambda: equal())

# adding grids
input_space.grid(row=0,column=1,columnspan=3)
button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)
button7.grid(row=3,column=1)
button8.grid(row=3,column=2)
button9.grid(row=3,column=3)
button0.grid(row=4,column=1)
button_add.grid(row=4,column=2)
button_substract.grid(row=4,column=3)
button_mult.grid(row=5,column=1)
button_div.grid(row=5,column=2)
button_square.grid(row=5,column=3)
button_root.grid(row=6,column=1)
button_sin.grid(row=6,column=2)
button_cos.grid(row=6,column=3)
button_clear.grid(row=7,column=1)
button_equals.grid(row=7,column=3)


# loop end
root.mainloop()
