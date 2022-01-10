import tkinter as tk
import math
from tkinter import messagebox 
# Basic Display
root= tk.Tk()

root.title("PyCalc Tk")
root.configure(bg='#c3c3c3')

canvas1 = tk.Canvas(root, width = 375, height = 375 , bg='#c3c3c3')
canvas1.pack()

entry1 = tk.Entry (root , bg='#c3c3c3')
canvas1.create_window(210, 100, window=entry1)

entry2 = tk.Entry (root , bg='#c3c3c3')
canvas1.create_window(210, 140, window=entry2)

entry3 = tk.Entry (root , bg='#c3c3c3')
canvas1.create_window(210, 300, window=entry3)  
canvas1.delete('entry3')

label0 = tk.Label(root, text='Calculator')
label0.config(font=('monospace', 14) , bg='#c3c3c3')
canvas1.create_window(200, 45, window=label0)

label1 = tk.Label(root, text='Input1:')
label1.config(font=('monospace', 10) , bg='#c3c3c3')
canvas1.create_window(100, 100, window=label1)

label2 = tk.Label(root, text='Input2:')
label2.config(font=('monospace', 10) , bg='#c3c3c3')
canvas1.create_window(100, 140, window=label2)

label3 = tk.Label(root, text='Result:')
label3.config(font=('monospace', 10) , bg='#c3c3c3')
canvas1.create_window(100, 300, window=label3)


def add():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or  v2 == '':
        messagebox.showerror('Please try again?' , 'Please enter any input on both the entry boxes.')
    else:    
        label4 = tk.Label(root, text= float(v1)+float(v2),font=('monospace', 10, 'bold'),bg='#c3c3c3')
        canvas1.create_window(210, 300, window=label4)

buttonAdd = tk.Button(text='+', command=add, bg='#010081', fg='#c3c3c3', font=('monospace', 12, 'bold'), width = 5)
canvas1.create_window(90, 190, window=buttonAdd)

def sub():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
         messagebox.showerror('Please try again?' , 'Please enter any input on both the entry boxes.')
    else:        
        label5 = tk.Label(root, text= float(v1)-float(v2),font=('monospace', 10, 'bold'),bg='#c3c3c3')
        canvas1.create_window(210, 300, window=label5)

buttonSub = tk.Button(text='-', command=sub, bg='#010081', fg='#c3c3c3', font=('iosevka', 12, 'bold'), width = 5)
canvas1.create_window(140, 190, window=buttonSub)

def mul():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
        messagebox.showerror('Please try again?' , 'Please enter any input on both the entry boxes')
    else:    
        label6 = tk.Label(root, text= float(v1)*float(v2),font=('monospace', 10, 'bold'),bg='#c3c3c3')
        canvas1.create_window(210, 300, window=label6)

buttonMul = tk.Button(text='x', command=mul, bg='#010081', fg='#c3c3c3', font=('monospace', 12, 'bold'), width = 5)
canvas1.create_window(190, 190, window=buttonMul)

def div():
    v1 = entry1.get()
    v2 = entry2.get()
    if v2 == "0" or v1 == '0':
        messagebox.showerror('Please try again?' , 'Please enter any number except 0 in the entry boxes.')
    elif v1 == '' or v2 == '':
        messagebox.showerror('Please try again?' , 'Please enter any input on the entry boxes')    
    else:
        label7 = tk.Label(root, text= float(v1)/float(v2),font=('monospace', 10, 'bold'),bg='#c3c3c3' ,)
        canvas1.create_window(210, 300, window=label7)
buttonDiv = tk.Button(text='/', command=div, bg='#010081', fg='#c3c3c3', font=('monospace', 12, 'bold'), width = 5)
canvas1.create_window(240, 190, window=buttonDiv)

def sqrt_f():
    v1 = entry1.get()
    v2 = entry2.get()
    if v2 == str(v2):
        messagebox.showinfo('Information' , 'Please enter your specified input on the first entry box for operations like cbrt or sqrt')
        label8 =  tk.Label(root , text = math.sqrt(float(v1)),font = ('monospace' , 10, 'bold' ), bg = '#c3c3c3')
        canvas1.create_window(210 , 300, window=label8)
    else:
        label8 = tk.Label(root , text = math.sqrt(float(v1)),font = ('monospace' , 10, 'bold' ), bg = '#c3c3c3')
        canvas1.create_window(210 , 300, window=label8)

buttonSqrt = tk.Button(text='sqrt', command=sqrt_f , bg='#010081', fg='#c3c3c3', font=('monospace' , 10 , 'bold'), width = 5)
canvas1.create_window(100 , 220 , window=buttonSqrt)

def cbrt_f():
    v1 = entry1.get()

    label9 = tk.Label(root , text=float(v1)**(1./3),font = ('monospace' , 10, 'bold' ), bg = '#c3c3c3')
    canvas1.create_window(210 , 300, window=label9)

buttonCbrt = tk.Button(text='cbrt', command=cbrt_f , bg='#010081', fg='#c3c3c3', font=('monospace' , 10 , 'bold'), width = 5)
canvas1.create_window(160 , 220 , window=buttonCbrt)

def pwr_f():
    v1 = entry1.get()
    v2 = entry2.get()

    label10 = tk.Label(root , text=float(v1)**float(v2),font=('monospace' , 10, 'bold' ), bg = '#c3c3c3')
    canvas1.create_window(210 , 300, window=label10)

buttonPwr = tk.Button(root, text='pwr', command=pwr_f , bg='#010081' , fg='#c3c3c3' , font=('monospace' , 10 , 'bold'), width = 5)
canvas1.create_window(220 , 220, window=buttonPwr)

def sin_f():
    v1 = entry1.get()
    v2 = entry2.get()
    
    label11 = tk.Label(root , text=math.sin(float(v1)) , font=('monospace' , 12))
ButtonSin = tk.Button(root , text='sin' ,command=sin_f , bg='#010081' , fg='#c3c3c3' , font=('monospace' , 12) , width = 5)
def cos_f():
    v1 = entry1.get()

    label12 = tk.Label(root , text=math.cos(float(v1)) , font=('monospace' , 12))
ButtonCos = tk.Button(root , text='cos' , command=cos_f , bg='#010081' , fg='#c3c3c3' , font=('monospace' , 12) , width= 5)
# Clear Function
def clear_f():
	label7 = tk.Label(root, text= "                                       " , bg = '#c3c3c3' , fg = '#c3c3c3')
	canvas1.create_window(210, 300, window = label7)

buttonClean = tk.Button(root , text='Clear' , command=clear_f , bg='#010081' ,fg='white' , width='5' , font=('monospace' , 12))
canvas1.create_window(330, 300, window=buttonClean)
root.mainloop()

