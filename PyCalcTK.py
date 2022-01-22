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
        label4 = tk.Label(root, text= "                                              ")
        canvas1.create_window(210 , 300, window=label4)
        label4 = tk.Label(root, text= float(v1)+float(v2),font=('monospace', 12))
        canvas1.create_window(210, 300, window=label4)

buttonAdd = tk.Button(text='+', command=add, bg='blue', fg='white' , font=('monospace', 12, 'bold'), width = 4)
canvas1.create_window(100, 190, window=buttonAdd)

def sub():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
        messagebox.askretrycancel("Try Again?", "Please enter an input on both the entry boxes")
    else:
        label5 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210 , 300, window=label5)
        label5 = tk.Label(root, text= float(v1)-float(v2),font=('monospace', 12))
        canvas1.create_window(210, 300, window=label5)

buttonSub = tk.Button(text='–', command=sub, bg='blue' , fg='white', font=('monospace', 12, 'bold'), width = 4)
canvas1.create_window(150, 190, window=buttonSub)

def mul():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on both the entry boxes')
    else:
        label6 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210 , 300 , window=label6)
        label6 = tk.Label(root, text= float(v1)*float(v2),font=('monospace', 12))
        canvas1.create_window(210, 300, window=label6)

buttonMul = tk.Button(text='x', command=mul, bg='blue', fg='white', font=('monospace', 12, 'bold'), width = 4)
canvas1.create_window(220, 190, window=buttonMul)

def div():
    v1 = entry1.get()
    v2 = entry2.get()
    if v2 == "0" or v1 == '0':
        messagebox.askretrycancel('ZeroDivisionError Try Again?' , 'Please enter any number except 0 in the entry boxes for the division operation.')
    elif v1 == '' or v2 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on both the entry boxes')
    else:
        label7 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210 , 300, window=label7)
        label7 = tk.Label(root, text= float(v1)/float(v2),font=('monospace', 12))
        canvas1.create_window(210, 300, window=label7)

buttonDiv = tk.Button(text='/', command=div, bg='blue', fg='white', font=('monospace', 12, 'bold'), width = 4)
canvas1.create_window(280, 190, window=buttonDiv)

def sqrt_f():
    v1 = entry1.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter the specified input on the first entry box')
    else:
        label8 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210 , 300, window=label8)
        label8 = tk.Label(root , text = math.sqrt(float(v1)),font = ('monospace' , 12, 'bold' ))
        canvas1.create_window(210 , 300, window=label8)

buttonSqrt = tk.Button(text='sqrt', command=sqrt_f , bg='blue', fg='white', font=('monospace' , 10 , 'bold'), width = 3)
canvas1.create_window(150 , 220 , window=buttonSqrt)

def cbrt_f():
    v1 = entry1.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter the specified input on the first entry box')
    else:
        label9 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210, 300, window=label9)
        label9 = tk.Label(root , text=float(v1)**(1./3),font = ('monospace' , 12, 'bold' ))
        canvas1.create_window(210 , 300, window=label9)

buttonCbrt = tk.Button(text='cbrt', command=cbrt_f , bg='blue', fg='white', font=('monospace' , 10 , 'bold'), width = 3)
canvas1.create_window(200 , 220 , window=buttonCbrt)

def pwr_f():
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '' or v2 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on both the entry boxes')
    else:
        label10 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210 , 300, window=label10)
        label10 = tk.Label(root , text=float(v1)**float(v2),font=('monospace' , 12, 'bold' ))
        canvas1.create_window(210 , 300, window=label10)

buttonPwr = tk.Button(root, text='pwr', command=pwr_f , bg='blue' , fg='white' , font=('monospace' , 10 , 'bold'), width = 3)
canvas1.create_window(250 , 220, window=buttonPwr)

def logarithm_f(event):
    v1 = entry1.get()
    v2 = entry2.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter the specified input on entry1')
    elif v1 == str(v1):
        label14 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210, 300 , window=label14)
        label14 = tk.Label(text=math.log(float(v1)) , font=('monospace' , 12))
        canvas1.create_window(210 , 300 , window=label14)
    else:
        label14 = tk.Label(text=math.sin(float(float(v1) , float(v2))) , font=('monospace' , 12))
        canvas1.create_window(210 , 300, window=label14)
def sin_f():
    v1 = entry1.get()
    if v1 == '':
         messagebox.askretrycancel('Try Again?' , 'Please enter an input on the first entry box')
    else:
        label11 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210, 300, window=label11)
        label11 = tk.Label(root , text=math.sin(float(v1)) , font=('monospace' , 12))
        canvas1.create_window(210 , 300, window=label11)

ButtonSin = tk.Button(root , text='sin' , command=sin_f , bg='blue' , fg='white' , font=('monospace' , 12) , width = 3)
canvas1.create_window(150 , 250, window=ButtonSin)

def cos_f():
    v1 = entry1.get()
    if v1 == '':
         messagebox.askretrycancel('Try Again?' , 'Please enter an input on the first entry box')
    else:
        label12 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210, 300, window=label12)
        label12 = tk.Label(root , text=math.cos(float(v1)) , font=('monospace' , 12))
        canvas1.create_window(210 , 300, window=label12)

ButtonCos = tk.Button(root , text='cos' , command=cos_f , bg='blue' , fg='white' , font=('monospace' , 12) , width = 3)
canvas1.create_window(250 ,250, window=ButtonCos)
#canvas1.create_window()
def tan_f():
    v1 = entry1.get()
    if v1 == '':
        messagebox.askretrycancel('Try Again?' , 'Please enter an input on the first entry box')
    else:
        label13 =  tk.Label(root, text= "                                              ")
        canvas1.create_window(210 ,300, window=label13)
        label13 = tk.Label(root , text=math.tan(float(v1)) , font=('monospace' , 12))
        canvas1.create_window(210, 300, window=label13)

ButtonTan = tk.Button(root , text='tan' , command=tan_f , bg='blue' , fg='white' , font=('monospace' , 12) , width = 3)
canvas1.create_window(200 , 250, window=ButtonTan)
# Clear Function
def clear_f():
	label7 = tk.Label(root, text= "                                              ")
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
    messagebox.showinfo('About' , 'PyCalcTK Nighty https://github.com/abhx-x11/pycalctk')
#Button Colors
def but_red():
    ButtonCos.configure(bg='red')
    ButtonTan.configure(bg='red')
    ButtonSin.configure(bg='red')
    buttonAdd.configure(bg='red')
    buttonSub.configure(bg='red')
    buttonMul.configure(bg='red')
    buttonDiv.configure(bg='red')
    buttonPwr.configure(bg='red')
    buttonSqrt.configure(bg='red')
    buttonCbrt.configure(bg='red')
    buttonClean.configure(bg='red')
def but_org():
    ButtonCos.configure(bg='orange')
    ButtonTan.configure(bg='orange')
    ButtonSin.configure(bg='orange')
    buttonAdd.configure(bg='orange')
    buttonSub.configure(bg='orange')
    buttonMul.configure(bg='orange')
    buttonDiv.configure(bg='orange')
    buttonPwr.configure(bg='orange')
    buttonSqrt.configure(bg='orange')
    buttonCbrt.configure(bg='orange')
    buttonClean.configure(bg='orange')
def but_yell():
    ButtonCos.configure(bg='yellow' , fg='black')
    ButtonTan.configure(bg='yellow' , fg='black')
    ButtonSin.configure(bg='yellow' , fg='black')
    buttonAdd.configure(bg='yellow' , fg='black')
    buttonSub.configure(bg='yellow' , fg='black')
    buttonMul.configure(bg='yellow' , fg='black')
    buttonDiv.configure(bg='yellow' , fg='black')
    buttonPwr.configure(bg='yellow' , fg='black')
    buttonSqrt.configure(bg='yellow' , fg='black')
    buttonCbrt.configure(bg='yellow' , fg='black')
    buttonClean.configure(bg='yellow' , fg='black')
def but_lgren():
    buttonPwr.configure(bg='light green' , fg='black')
    ButtonTan.configure(bg='light green' , fg='black')
    ButtonCos.configure(bg='light green' , fg='black')
    ButtonSin.configure(bg='light green' , fg='black')
    buttonAdd.configure(bg='light green' , fg='black')
    buttonSub.configure(bg='light green' , fg='black')
    buttonMul.configure(bg='light green' , fg='black')
    buttonDiv.configure(bg='light green' , fg='black')
    buttonSqrt.configure(bg='light green' , fg='black')
    buttonCbrt.configure(bg='light green' , fg='black')
    buttonClean.configure(bg='light green' , fg='black')
def but_lime():
    buttonAdd.configure(bg='lime' , fg='black')
    buttonSub.configure(bg='lime' , fg='black')
    buttonMul.configure(bg='lime' , fg='black')
    buttonDiv.configure(bg='lime' , fg='black')
    buttonPwr.configure(bg='lime' , fg='black')
    buttonCbrt.configure(bg='lime' , fg='black')
    buttonSqrt.configure(bg='lime' , fg='black')
    ButtonTan.configure(bg='lime' , fg='black')
    ButtonCos.configure(bg='lime' , fg='black')
    ButtonSin.configure(bg='lime' , fg='black')
    buttonClean.configure(bg='lime' , fg='black')
def but_dgreen():
    buttonAdd.configure(bg='green' , fg='white')
    buttonSub.configure(bg='green' , fg='white')
    buttonMul.configure(bg='green' , fg='white')
    buttonDiv.configure(bg='green' , fg='white')
    buttonPwr.configure(bg='green' , fg='white')
    buttonCbrt.configure(bg='green' , fg='white')
    buttonSqrt.configure(bg='green' , fg='white')
    ButtonTan.configure(bg='green' , fg='white')
    ButtonCos.configure(bg='green' , fg='white')
    ButtonSin.configure(bg='green' , fg='white')
    buttonClean.configure(bg='green' , fg='white')
def but_lblue():
    buttonAdd.configure(bg='light blue' , fg='black')
    buttonSub.configure(bg='light blue' , fg='black')
    buttonMul.configure(bg='light blue' , fg='black')
    buttonDiv.configure(bg='light blue' , fg='black')
    buttonPwr.configure(bg='light blue' , fg='black')
    buttonCbrt.configure(bg='light blue' , fg='black')
    buttonSqrt.configure(bg='light blue' , fg='black')
    ButtonCos.configure(bg='light blue' , fg='black')
    ButtonTan.configure(bg='light blue' , fg='black')
    ButtonSin.configure(bg='light blue' , fg='black')
    buttonClean.configure(bg='light blue' , fg='black')
def blue_f():
        buttonAdd.configure(bg='blue' , fg='white')
        buttonSub.configure(bg='blue' , fg='white')
        buttonMul.configure(bg='blue' , fg='white')
        buttonDiv.configure(bg='blue' , fg='white')
        buttonPwr.configure(bg='blue' , fg='white')
        buttonCbrt.configure(bg='blue' , fg='white')
        buttonSqrt.configure(bg='blue' , fg='white')
        ButtonCos.configure(bg='blue' , fg='white')
        ButtonTan.configure(bg='blue' , fg='white')
        ButtonSin.configure(bg='blue' , fg='white')
        buttonClean.configure(bg='blue' , fg='white')
def but_purp():
        buttonAdd.configure(bg='purple' , fg='white')
        buttonSub.configure(bg='purple' , fg='white')
        buttonMul.configure(bg='purple' , fg='white')
        buttonDiv.configure(bg='purple' , fg='white')
        buttonPwr.configure(bg='purple' , fg='white')
        buttonCbrt.configure(bg='purple' , fg='white')
        buttonSqrt.configure(bg='purple' , fg='white')
        ButtonCos.configure(bg='purple' , fg='white')
        ButtonTan.configure(bg='purple' , fg='white')
        ButtonSin.configure(bg='purple' , fg='white')
        buttonClean.configure(bg='purple' , fg='white')
def but_black():
        buttonAdd.configure(bg='black' , fg='white')
        buttonSub.configure(bg='black' , fg='white')
        buttonMul.configure(bg='black' , fg='white')
        buttonDiv.configure(bg='black' , fg='white')
        buttonPwr.configure(bg='black' , fg='white')
        buttonCbrt.configure(bg='black' , fg='white')
        buttonSqrt.configure(bg='black' , fg='white')
        ButtonCos.configure(bg='black' , fg='white')
        ButtonTan.configure(bg='black' , fg='white')
        ButtonSin.configure(bg='black' , fg='white')
        buttonClean.configure(bg='black' , fg='white')
#Asset Sizes
def ast_big():
    label0.configure(font=('monospace' , 14))
    label1.configure(font=('monospace' , 14))
    label2.configure(font=('monospace' , 14))
    label3.configure(font=('monospace' , 14))
    entry1.configure(font=('monospace' , 14))
    entry2.configure(font=('monospace' , 14))
    canvas1.create_window(250 , 100, window=entry1)
    canvas1.create_window(250 , 140, window=entry2)
def ast_nmal():
    label0.configure(font=('monospace' , 12))
    label1.configure(font=('monospace' , 12))
    label2.configure(font=('monospace' , 12))
    label3.configure(font=('monospace' , 12))
    entry1.configure(font=('monospace' , 12))
    entry2.configure(font=('monospace' , 12))
    canvas1.create_window(230 , 100, window=entry1)
    canvas1.create_window(230 , 140, window=entry2)
def ast_small():
        label0.configure(font=('monospace' , 10))
        label1.configure(font=('monospace' , 10))
        label2.configure(font=('monospace' , 10))
        label3.configure(font=('monospace' , 10))
        entry1.configure(font=('monospace' , 10))
        entry2.configure(font=('monospace' , 10))
        canvas1.create_window(200 , 100, window=entry1)
        canvas1.create_window(200 , 140, window=entry2)
#Menu Bar
menubar = Menu(root)
cbc = Menu(menubar, tearoff=0)
cbc.add_radiobutton(label='Red' , command=but_red)
cbc.add_radiobutton(label='Orange' , command=but_org)
cbc.add_radiobutton(label='Yellow' , command=but_yell)
cbc.add_radiobutton(label='Light Green' , command=but_lgren)
cbc.add_radiobutton(label='Lime' , command=but_lime)
cbc.add_radiobutton(label='Dark Green' , command=but_dgreen)
cbc.add_radiobutton(label='Light Blue' , command=but_lblue)
cbc.add_radiobutton(label='Blue' , command=blue_f)
cbc.add_radiobutton(label='Purple' , command=but_purp)
cbc.add_radiobutton(label='Black' , command=but_black)
cast = Menu(menubar, tearoff=0)
cast.add_radiobutton(label='Small Assets' , command=ast_small)
cast.add_radiobutton(label='Normal Assets' , command=ast_nmal)
cast.add_radiobutton(label='Big Assets' , command=ast_big)
prefm = Menu(menubar, tearoff=0)
prefm.add_cascade(label='Accent Color' , menu=cbc)
prefm.add_cascade(label='Asset Sizes' , menu=cast)
menubar.add_cascade(label='Settings' , menu=prefm)
helpmenu=Menu(root , tearoff=0)
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
