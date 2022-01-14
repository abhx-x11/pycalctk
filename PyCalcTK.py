import tkinter as tk
import math
from tkinter import *
from tkinter import messagebox
# Basic Display
root= tk.Tk()

root.title("PyCalc TK 1.0 Dev")
root.geometry('400x375')

canvas1 = tk.Canvas(root, width = 400, height = 375)
canvas1.pack()

entry1 = tk.Entry (root)
canvas1.create_window(210, 100, window=entry1)

entry2 = tk.Entry (root)
canvas1.create_window(210, 140, window=entry2)

entry3 = tk.Entry (root)
canvas1.create_window(210, 300, window=entry3)  
canvas1.delete('entry3')

label0 = tk.Label(root, text='Calculator')
label0.config(font=('monospace', 14))
canvas1.create_window(200, 40, window=label0)

label1 = tk.Label(root, text='Input1:')
label1.config(font=('monospace', 10))
canvas1.create_window(85, 100, window=label1)

label2 = tk.Label(root, text='Input2:')
label2.config(font=('monospace', 10))
canvas1.create_window(85, 140, window=label2)

label3 = tk.Label(root, text='Result:')
label3.config(font=('monospace', 10))
canvas1.create_window(85, 300, window=label3)

#Activating operations
def add():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
        messagebox.askretrycancel("Try Again?", "Please enter an input on both the entry boxes")
    else:
        label4 = tk.Label(root, text= float(v1)+float(v2),font=('monospace', 12))
        canvas1.create_window(210, 300, window=label4)      

buttonAdd = tk.Button(text='+', command=add, bg='blue', font=('monospace', 12, 'bold'), width = 4)
canvas1.create_window(100, 190, window=buttonAdd)

def sub():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
        messagebox.askretrycancel("Try Again?", "Please enter an input on both the entry boxes")
    else:    
        label5 = tk.Label(root, text= float(v1)-float(v2),font=('monospace', 12),bg='#c3c3c3')
        canvas1.create_window(210, 300, window=label5)

buttonSub = tk.Button(text='-', command=sub, bg='blue' , fg='white', font=('monospace', 12, 'bold'), width = 4)
canvas1.create_window(150, 190, window=buttonSub)

def mul():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on both the entry boxes')
    else:
        label6 = tk.Label(root, text= float(v1)*float(v2),font=('monospace', 12),bg='#c3c3c3')
        canvas1.create_window(210, 300, window=label6)

buttonMul = tk.Button(text='x', command=mul, bg='blue', fg='white', font=('monospace', 12, 'bold'), width = 4)
canvas1.create_window(220, 190, window=buttonMul)

def div():
    v1 = entry1.get()
    v2 = entry2.get()
    if v2 == "0" or v1 == '0':
        messagebox.askretrycancel('ZeroDivisionError' , 'Please enter any number except 0 in the entry boxes for the division operation.')
    elif v1 == '' or v2 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on both the entry boxes')
    else:
        label7 = tk.Label(root, text= float(v1)/float(v2),font=('monospace', 12),bg='#c3c3c3' ,)
        canvas1.create_window(210, 300, window=label7)

buttonDiv = tk.Button(text='/', command=div, bg='blue', fg='white', font=('monospace', 12, 'bold'), width = 4)
canvas1.create_window(280, 190, window=buttonDiv)

def sqrt_f():
    v1 = entry1.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on the first entry box')
    else:     
        label8 = tk.Label(root , text = math.sqrt(float(v1)),font = ('monospace' , 10, 'bold' ), )
        canvas1.create_window(210 , 300, window=label8)

buttonSqrt = tk.Button(text='sqrt', command=sqrt_f , bg='blue', fg='white', font=('monospace' , 10 , 'bold'), width = 3)
canvas1.create_window(150 , 220 , window=buttonSqrt)

def cbrt_f():
    v1 = entry1.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on the first entry box')
    else:    
        label9 = tk.Label(root , text=float(v1)**(1./3),font = ('monospace' , 10, 'bold' ), )
        canvas1.create_window(210 , 300, window=label9)

buttonCbrt = tk.Button(text='cbrt', command=cbrt_f , bg='blue', fg='white', font=('monospace' , 10 , 'bold'), width = 3)
canvas1.create_window(200 , 220 , window=buttonCbrt)

def pwr_f():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on both the entry boxes')
    else:        
        label10 = tk.Label(root , text=float(v1)**float(v2),font=('monospace' , 10, 'bold' ), )
        canvas1.create_window(210 , 300, window=label10)

buttonPwr = tk.Button(root, text='pwr', command=pwr_f , bg='blue' , fg='white' , font=('monospace' , 10 , 'bold'), width = 3)
canvas1.create_window(250 , 220, window=buttonPwr)

def sin_f():
    v1 = entry1.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on the first entry box')
    else:    
        label11 = tk.Label(root , text=math.sin(float(v1)) , font=('monospace' , 12))
        canvas1.create_window(210 , 300, window=label11)

ButtonSin = tk.Button(root , text='sin' , command=sin_f , bg='blue' , fg='white' , font=('monospace' , 12) , width = 3)
canvas1.create_window(150 , 250, window=ButtonSin)

def cos_f():
    v1 = entry1.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on the first entry box')
    else:    
        label12 = tk.Label(root , text=math.cos(float(v1)) , font=('monospace' , 12))
        canvas1.create_window(210 , 300, window=label12)

ButtonCos = tk.Button(root , text='cos' , command=cos_f , bg='blue' , fg='white' , font=('monospace' , 12) , width = 3)
canvas1.create_window(250 ,250, window=ButtonCos)

def tan_f():
    v1 = entry1.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again' , 'Please enter an input on the first')
    else:    
        label13 = tk.Label(root , text=math.tan(float(v1)) , font=('monospace' , 12))
        canvas1.create_window(210, 300, window=label13)

ButtonTan = tk.Button(root , text='tan' , command=tan_f , bg='blue' , fg='white' , font=('monospace' , 12) , width = 3)
canvas1.create_window(200 , 250, window=ButtonTan)    
# Clear Function
def clear_f():
	label7 = tk.Label(root, text= "                                             ")
	canvas1.create_window(210, 300, window = label7)

buttonClean = tk.Button(root , text='Clear' , command=clear_f , bg='blue' ,fg='white' , width='5' , font=('monospace' , 12))
canvas1.create_window(350, 300, window=buttonClean)
#Help functions
def helpadd_f():
    messagebox.showinfo('Help' , 'In the first and the second entry boxes enter the numbers and by clicking the + button you get the answer ')
def helpsub_f():
    messagebox.showinfo('Help' , 'In the first entry box you need to enter the bigger number and in the second entry you need to enter the small number and you can get the answer by clicking the - button.')
def helpmul_f():
   messagebox.showinfo('Help' , 'In the first and the second entry boxes enter any number you want and to get the answer click on the X button to get the product.')
def helpdiv_f():
    messagebox.showinfo('Help' , 'In the first entry enter any number(except 0) for dividend and in the second entry enter any number(except 0) for dividend and to get the quotient you have to click on the / button')    
def about():
    messagebox.showinfo('About' , 'PyCalc Dev 1.0 https://github.com/abhx-x11/pycalctk')
#Help Menu    
menubar = Menu(root)
helpmenu = Menu(menubar , tearoff=0)
helpmenu.add_command(label = 'Addition Help' , command=helpadd_f)
helpmenu.add_command(label = 'Subtraction Help' , command=helpsub_f)
helpmenu.add_command(label = 'Multiplication Help' , command=helpmul_f)
helpmenu.add_command(label = 'Division Help' , command=helpdiv_f)
helpmenu.add_separator()
helpmenu.add_command(label = 'About PyCalc TK' , command=about)
menubar.add_cascade(label = 'Help' , menu=helpmenu)
#Execution
root.config(menu=menubar)
root.mainloop()
