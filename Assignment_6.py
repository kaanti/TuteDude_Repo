# Calculator app

from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Calculator")
e = Entry(root, width=60, borderwidth=6)
e.place(x = 0, y = 0)

#Buttons

def click(x):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(x))

def add():
    n1 = e.get()
    global math
    math = 'add'
    global i
    i = float(n1)
    e.delete(0, END)

def sub():
    n1 = e.get()
    global math
    math = 'sub'
    global i
    i = float(n1)
    e.delete(0, END)

def mul():
    n1 = e.get()
    global math
    math = 'mul'
    global i
    i = float(n1)
    e.delete(0, END)

def div():
    n1 = e.get()
    global math
    math = 'div'
    global i
    i = float(n1)
    e.delete(0, END) 

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == 'add':
        e.insert(0, i + float(n2))
    elif math == 'sub':
        e.insert(0, i - float(n2))
    elif math == 'mul':
        e.insert(0, i * float(n2))
    elif math == 'div':
        e.insert(0, i / float(n2))

def clear():
    e.delete(0, END)

    

b = Button(root, text='7', width=8, command = lambda:click(7))
b.place(x = 0, y = 50)

b = Button(root, text='8', width=8, command = lambda:click(8))
b.place(x = 100, y = 50)

b = Button(root, text='9', width=8, command = lambda:click(9))
b.place(x = 200, y = 50)

b = Button(root, text='/', width=8, command = div)
b.place(x = 300, y = 50)

b = Button(root, text='4', width=8, command = lambda:click(4))
b.place(x = 0, y = 100)

b = Button(root, text='5', width=8, command = lambda:click(5))
b.place(x = 100, y = 100)

b = Button(root, text='6', width=8, command = lambda:click(6))
b.place(x = 200, y = 100)

b = Button(root, text='X', width=8, command = mul)
b.place(x = 300, y = 100)

b = Button(root, text='1', width=8, command = lambda:click(1))
b.place(x = 0, y = 150)

b = Button(root, text='2', width=8, command = lambda:click(2))
b.place(x = 100, y = 150)

b = Button(root, text='3', width=8, command = lambda:click(3))
b.place(x = 200, y = 150)

b = Button(root, text='+', width=8, command = add)
b.place(x = 300, y = 150)

b = Button(root, text='0', width=8, command = lambda:click(0))
b.place(x = 0, y = 200)

b = Button(root, text='.', width=8, command = lambda:click("."))
b.place(x = 100, y = 200)

b = Button(root, text='AC', width=8, command = clear)
b.place(x = 200, y = 200)

b = Button(root, text='=', width=8, command = equal)
b.place(x = 300, y = 200)

b = Button(root, text='-', width=8, command = sub)
b.place(x = 300, y = 250)

root.mainloop()