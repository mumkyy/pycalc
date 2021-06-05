from tkinter import *

expression = ""
def add() :
    global expression
    expression += "+"
    text.set(expression)
def subtract() :
    global expression
    expression += "-"
    text.set(expression)
def multiply() :
    global expression
    expression += "*"
    text.set(expression)
def divide() :
    global expression
    expression += "/"
    text.set(expression)
def reset() :
    global expression
    expression = ""
    text.set(expression)
def change_sign() :
    global expression
    if expression[0] != "-" :
        expression = "-" + expression
    else :
        expression[0] = "" 
    text.set(expression)
def evaluate() :
    global expression
    expression = str(eval(expression))
    text.set(expression)
def addnum(button) :
    global expression
    expression += button.cget('text')
    text.set(expression)
def backspace() :
    global expression
    expression = expression[:-1]
    text.set(expression)



window = Tk()
icon = PhotoImage(file='calculator.png')
text = StringVar()
text.set(expression)
window.title("Calculator")
window.iconphoto(True,icon)
window.config(background="#c0d1eb")
zero = Button(window,text="0",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
zero.config(command = lambda : addnum(zero))
zero.grid(row = 4, column=0,sticky="NSEW")

one = Button(window,text="1",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
one.config(command = lambda : addnum(one))
one.grid(row = 3, column=0,sticky="NSEW")

two = Button(window,text="2",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
two.config(command = lambda : addnum(two))
two.grid(row = 3, column=1,sticky="NSEW")

three = Button(window,text="3",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
three.config(command = lambda : addnum(three))
three.grid(row = 3, column=2,sticky="NSEW")

four = Button(window,text="4",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
four.config(command = lambda : addnum(four))
four.grid(row = 2, column=0,sticky="NSEW")


five = Button(window,text="5",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
five.config(command = lambda : addnum(five))
five.grid(row = 2, column=1,sticky="NSEW")

six = Button(window,text="6",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
six.config(command = lambda : addnum(six))
six.grid(row = 2, column=2,sticky="NSEW")

seven = Button(window,text="7",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
seven.config(command = lambda : addnum(seven))
seven.grid(row = 1, column=0,sticky="NSEW")

eight = Button(window,text="8",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
eight.config(command = lambda : addnum(eight))
eight.grid(row = 1, column=1,sticky="NSEW")

nine = Button(window,text="9",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
nine.config(command = lambda : addnum(nine))
nine.grid(row = 1, column=2,sticky="NSEW")

decimal = Button(window,text=".",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
decimal.config(command = lambda : addnum(decimal))
decimal.grid(row = 4, column=1,sticky="NSEW")

clear = Button(window,text="Clear",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',command= reset,height= 5, width= 10)
clear.grid(row = 0, column=3,sticky="NSEW")

backs = Button(window,text="<--",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',command= backspace,height= 5, width= 10)
backs.grid(row = 0, column=2,sticky="NSEW")

addi = Button(window,text="+",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',command= add,height= 5, width= 10)
addi.grid(row = 4, column=3,sticky="NSEW")

subi = Button(window,text="-",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',command= subtract,height= 5, width= 10)
subi.grid(row = 3, column=3,sticky="NSEW")

multi = Button(window,text="*",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',command= multiply,height= 5, width= 10)
multi.grid(row = 2, column=3,sticky="NSEW")

divi = Button(window,text="/",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',command= divide,height= 5, width= 10)
divi.grid(row = 1, column=3,sticky="NSEW")

eqi = Button(window,text="=",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',command= evaluate,height= 5, width= 10)
eqi.grid(row = 4, column=2,sticky="NSEW")

startp = Button(window,text="(",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
startp.config(command = lambda : addnum(startp))
startp.grid(row = 0, column=0,sticky="NSEW")

endp = Button(window,text=")",fg = 'black', bg = 'gray',activebackground= 'gray',activeforeground='black',height= 5, width= 10)
endp.config(command = lambda : addnum(endp))
endp.grid(row = 0, column=1,sticky="NSEW")

label = Label(window,
    textvariable= text,
    font=('Arial',20,'bold'), 
    fg = 'black',
    bg='#c0d1eb',
    relief=RAISED)
label.grid(row = 5, columnspan=4)
window.resizable(False,False)
window.mainloop()

