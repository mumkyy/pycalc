from tkinter import *
from PIL import Image, ImageTk


expression = ""
last_clicked = ""
def add() :
    global expression
    global last_clicked
    if len(ex.get()) >= 52 :
        ex.set("Number/Equation Too Long Error")
    elif len(ex.get()) == 26 :
        bigify()
        expression += "+"
        ex.set(expression)
        last_clicked = "add"
    elif len(ex.get()) < 26 :
        minify()
        expression += "+"
        ex.set(expression)
        last_clicked = "add"
    else :
        expression += "+"
        ex.set(expression)
        last_clicked = "add"
def subtract() :
    global expression
    global last_clicked
    if len(ex.get()) >= 52 :
        ex.set("Number/Equation Too Long Error")
    elif len(ex.get()) == 26 :
        bigify()
        expression += "-"
        ex.set(expression)
        last_clicked = "subtract"
    elif len(ex.get()) < 26 :
        minify()
        expression += "-"
        ex.set(expression)
        last_clicked = "subtract"
    else :
        expression += "-"
        ex.set(expression)
        last_clicked = "subtract"
def multiply() :
    global expression
    global last_clicked
    if len(ex.get()) >= 52 :
        ex.set("Number/Equation Too Long Error")
    elif len(ex.get()) == 26 :
        bigify()
        expression += "*"
        ex.set(expression)
        last_clicked = "multiply"
    elif len(ex.get()) < 26 :
        minify()
        expression += "*"
        ex.set(expression)
        last_clicked = "multiply"
    else :
        expression += "*"
        ex.set(expression)
        last_clicked = "multiply"
def divide() :
    global expression
    global last_clicked
    if len(ex.get()) >= 52 :
        ex.set("Number/Equation Too Long Error")
    elif len(ex.get()) == 26 :
        bigify()
        expression += "/"
        ex.set(expression)
        last_clicked = "divide"
    elif len(ex.get()) < 26 :
        minify()
        expression += "/"
        ex.set(expression)
        last_clicked = "divide"
    else :
        expression += "/"
        ex.set(expression)
        last_clicked = "divide"
def reset() :
    global expression
    global last_clicked
    if len(ex.get()) >= 52 :
        ex.set("Number/Equation Too Long Error")
    elif len(ex.get()) == 26 :
        bigify()
        expression = ""
        ex.set(expression)
        last_clicked = "reset"
    elif len(ex.get()) < 26 :
        minify()
        expression = ""
        ex.set(expression)
        last_clicked = "reset"
    else :
        expression = ""
        ex.set(expression)
        last_clicked = "reset"
def evaluate() :
    global last_clicked
    global expression
    if len(ex.get()) >= 52 :
        ex.set("Number/Equation Too Long Error")
    elif len(ex.get()) == 26 :
        bigify()
        try:
            expression = str(eval(expression))
            ex.set(expression)
        except SyntaxError:
            ex.set("Syntax Error")
        except ZeroDivisionError:
            ex.set("Zero Division Error")
        last_clicked = "equals"
    elif len(ex.get()) < 26 :
        minify()
        try:
            expression = str(eval(expression))
            ex.set(expression)
        except SyntaxError:
            ex.set("Syntax Error")
        except ZeroDivisionError:
            ex.set("Zero Division Error")
        last_clicked = "equals"
    else :
        try:
            expression = str(eval(expression))
            ex.set(expression)
        except SyntaxError:
            ex.set("Syntax Error")
        except ZeroDivisionError:
            ex.set("Zero Division Error")
        last_clicked = "equals"
def addnum(button) :
    global last_clicked
    if last_clicked == "equals" :
        reset()
    if ex.get() == "Number/Equation Too Long Error" :
        reset()
    global expression
    if len(ex.get()) >= 52 :
        ex.set("Number/Equation Too Long Error")
    elif len(ex.get()) == 26 :
        bigify()
        expression += button.cget('text')
        ex.set(expression)
        last_clicked = "addnum"
    elif len(ex.get()) < 26 :
        minify()
        expression += button.cget('text')
        ex.set(expression)
        last_clicked = "addnum"
    else :
        expression += button.cget('text')
        ex.set(expression)
        last_clicked = "addnum"
def backspace() :
    global expression
    global last_clicked
    if len(ex.get()) >= 52 :
        ex.set("Number/Equation Too Long Error")
    elif len(ex.get()) == 26 :
        bigify()
        expression = expression[:-1]
        ex.set(expression)
        last_clicked = "back"
    elif len(ex.get()) < 26 :
        minify()
        expression = expression[:-1]
        ex.set(expression)
        last_clicked = "back"
    else :
        expression = expression[:-1]
        ex.set(expression)
        last_clicked = "back"
def bigify() :
    zero.config(image=zerib)
    one.config(image=oneib)
    two.config(image=twoib)
    three.config(image=thrib)
    four.config(image=forib)
    five.config(image=fivib)
    six.config(image=sixib)
    seven.config(image=sevib)
    eight.config(image=eigib)
    nine.config(image=ninib)
    decimal.config(image=decib)
    clear.config(image=clrib)
    backs.config(image=bacib)
    addi.config(image=addib)
    subi.config(image=subib)
    multi.config(image=mulib)
    divi.config(image=dvib)
    eqi.config(image=equib)
    startp.config(image=fpaib)
    endp.config(image=bpaib)
    label.config(image=labelimgb)
def minify() :
    zero.config(image=zeri)
    one.config(image=onei)
    two.config(image=twoi)
    three.config(image=thri)
    four.config(image=fori)
    five.config(image=fivi)
    six.config(image=sixi)
    seven.config(image=sevi)
    eight.config(image=eigi)
    nine.config(image=nini)
    decimal.config(image=deci)
    clear.config(image=clri)
    backs.config(image=baci)
    addi.config(image=addb)
    subi.config(image=subb)
    multi.config(image=muli)
    divi.config(image=dvi)
    eqi.config(image=equi)
    startp.config(image=fpai)
    endp.config(image=bpai)
    label.config(image=labelimg)

window = Tk()
zerib =ImageTk.PhotoImage(Image.open('assets\\0b.png'))
oneib = ImageTk.PhotoImage(Image.open('assets\\1b.png'))
twoib = ImageTk.PhotoImage(Image.open('assets\\2b.png'))
thrib = ImageTk.PhotoImage(Image.open('assets\\3b.png'))
forib = ImageTk.PhotoImage(Image.open('assets\\4b.png'))
fivib = ImageTk.PhotoImage(Image.open('assets\\5b.png'))
sixib = ImageTk.PhotoImage(Image.open('assets\\6b.png'))
sevib = ImageTk.PhotoImage(Image.open('assets\\7b.png'))
eigib = ImageTk.PhotoImage(Image.open('assets\\8b.png'))
ninib = ImageTk.PhotoImage(Image.open('assets\\9b.png'))
decib = ImageTk.PhotoImage(Image.open('assets\\.b.png'))
clrib = ImageTk.PhotoImage(Image.open('assets\\Cb.png'))
bacib = ImageTk.PhotoImage(Image.open('assets\\backsb.png'))
addib = ImageTk.PhotoImage(Image.open('assets\\+b.png'))
subib = ImageTk.PhotoImage(Image.open('assets\\-b.png'))
mulib = ImageTk.PhotoImage(Image.open('assets\\multb.png'))
dvib = ImageTk.PhotoImage(Image.open('assets\\divideb.png'))
equib = ImageTk.PhotoImage(Image.open('assets\\=b.png'))
fpaib = ImageTk.PhotoImage(Image.open('assets\\(b.png'))
bpaib = ImageTk.PhotoImage(Image.open('assets\\)b.png'))
labelimgb = ImageTk.PhotoImage(Image.open('assets\\labelb.png'))

icon = PhotoImage(file='assets\\calculator.png')
zeri = PhotoImage(file='assets\\0.png')
onei = PhotoImage(file='assets\\1.png')
twoi = PhotoImage(file='assets\\2.png')
thri = PhotoImage(file='assets\\3.png')
fori = PhotoImage(file='assets\\4.png')
fivi = PhotoImage(file='assets\\5.png')
sixi = PhotoImage(file='assets\\6.png')
sevi = PhotoImage(file='assets\\7.png')
eigi = PhotoImage(file='assets\\8.png')
nini = PhotoImage(file='assets\\9.png')
addb = PhotoImage(file='assets\\+.png')
subb = PhotoImage(file='assets\\-.png')
muli = PhotoImage(file='assets\\mult.png')
dvi = PhotoImage(file='assets\\divide.png')
baci = PhotoImage(file='assets\\backs.png')
clri = PhotoImage(file='assets\\C.png')
deci = PhotoImage(file='assets\\..png')
fpai = PhotoImage(file='assets\\(.png')
bpai = PhotoImage(file='assets\\).png')
equi = PhotoImage(file='assets\\=.png')
labelimg = PhotoImage(file='assets\\label.png')

ex = StringVar()
ex.set(expression)
window.title("Calculator")
window.iconphoto(True,icon)
window.config(background="#c0d1eb")
zero = Button(window,image=zeri,text='0',bg='#c0d1eb',activebackground='#c0d1eb',font=('Arial',10,'bold'),bd=0)
zero.config(command = lambda : addnum(zero))
zero.grid(row = 5, column=0,sticky="NSEW")

one = Button(window,image=onei,text='1',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
one.config(command = lambda : addnum(one))
one.grid(row = 4, column=0,sticky="NSEW")

two = Button(window,image=twoi,text='2',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
two.config(command = lambda : addnum(two))
two.grid(row = 4, column=1,sticky="NSEW")

three = Button(window,image=thri,text='3',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
three.config(command = lambda : addnum(three))
three.grid(row = 4, column=2,sticky="NSEW")

four = Button(window,image=fori,text='4',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
four.config(command = lambda : addnum(four))
four.grid(row = 3, column=0,sticky="NSEW")


five = Button(window,image=fivi,text='5',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
five.config(command = lambda : addnum(five))
five.grid(row = 3, column=1,sticky="NSEW")

six = Button(window,image=sixi,text='6',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
six.config(command = lambda : addnum(six))
six.grid(row = 3, column=2,sticky="NSEW")

seven = Button(window,image=sevi,text='7',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
seven.config(command = lambda : addnum(seven))
seven.grid(row = 2, column=0,sticky="NSEW")

eight = Button(window,image=eigi,text='8',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
eight.config(command = lambda : addnum(eight))
eight.grid(row = 2, column=1,sticky="NSEW")

nine = Button(window,image=nini,text='9',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
nine.config(command = lambda : addnum(nine))
nine.grid(row = 2, column=2,sticky="NSEW")

decimal = Button(window,image=deci,text='.',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
decimal.config(command = lambda : addnum(decimal))
decimal.grid(row = 5, column=1,sticky="NSEW")

clear = Button(window,image=clri,command= reset,font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
clear.grid(row = 1, column=3,sticky="NSEW")

backs = Button(window,image=baci,font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb',command=backspace)
backs.grid(row = 1, column=2,sticky="NSEW")

addi = Button(window,image=addb,bd = 0,bg='#c0d1eb',activebackground='#c0d1eb',command= add,font=('Arial',10,'bold'))
addi.grid(row = 5, column=3,sticky="NSEW")

subi = Button(window,image=subb,bd = 0,bg='#c0d1eb',activebackground='#c0d1eb',command= subtract,font=('Arial',10,'bold'))
subi.grid(row = 4, column=3,sticky="NSEW")

multi = Button(window,image=muli,bd = 0,bg='#c0d1eb',activebackground='#c0d1eb',command= multiply,font=('Arial',10,'bold'))
multi.grid(row = 3, column=3,sticky="NSEW")

divi = Button(window,image=dvi,bd = 0,bg='#c0d1eb',activebackground='#c0d1eb',command= divide,font=('Arial',10,'bold'))
divi.grid(row = 2, column=3,sticky="NSEW")

eqi = Button(window,image=equi,bd = 0,bg='#c0d1eb',activebackground='#c0d1eb',command= evaluate,font=('Arial',10,'bold'))
eqi.grid(row = 5, column=2,sticky="NSEW")

startp = Button(window,image=fpai,text='(',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
startp.config(command = lambda : addnum(startp))
startp.grid(row = 1, column=0,sticky="NSEW")

endp = Button(window,image=bpai,text=')',font=('Arial',10,'bold'),bd = 0,bg='#c0d1eb',activebackground='#c0d1eb')
endp.config(command = lambda : addnum(endp))
endp.grid(row = 1, column=1,sticky="NSEW")

label = Label(window,
    textvariable= ex,
    image=labelimg,
    font=('Arial',20,'bold'), 
    fg = 'black',
    bg='#c0d1eb',
    relief=RAISED,compound=CENTER,bd=0)
label.grid(row = 0 , columnspan=4,sticky="NSEW")
window.resizable(False,False)
window.mainloop()

