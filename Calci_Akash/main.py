from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_helper import PlayAudio
import threading
font=('Verdana',20,'bold')
ob=PlayAudio()
def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)


def all_clear():
    textField.delete(0,END)
def click_btn_function(event):
    print("btn Clicked")
    b=event.widget
    text=b['text']
    print(text)
    t=threading.Thread(target=ob.speak,args=(text,))
    t.start()

    if text=='x':
        textField.insert(END,"*")
        return

    if text=='=':
        try:
            ex=textField.get()
            anser=eval(ex)
            textField.delete(0,END)
            textField.insert(0,anser)
        except Exception as e:
            print("Error......",e)
            showerror("Error",e)
        return
    textField.insert(END,text)
window=Tk()
window.title('Akash_Calculator')
window.geometry('510x550')
pic=PhotoImage(file='cal2.png')
headingLabel=Label(window,image=pic)
headingLabel.pack(side=TOP,pady=10)

heading=Label(window,text='My Calculator',font=font, underline=0)
heading.pack(side=TOP)

textField=Entry(window,font=font,justify=CENTER)
textField.pack(side=TOP,pady=10, fill=Y,padx=10)

buttonFrame=Frame(window)
buttonFrame.pack(side=TOP,padx=10)
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
        btn.grid(row=i,column=j,padx=3,pady=3)
        temp=temp+1
        btn.bind('<Button-1>',click_btn_function)

zeroBtn=Button(buttonFrame,text='0',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
zeroBtn.grid(row=3,column=0,padx=3,pady=3)


dotBtn=Button(buttonFrame,text='.',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
dotBtn.grid(row=3,column=1,padx=3,pady=3)

equalBtn=Button(buttonFrame,text='=',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
equalBtn.grid(row=3,column=2,padx=3,pady=3)



plusBtn=Button(buttonFrame,text='+',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
plusBtn.grid(row=0,column=3,padx=3,pady=3)


minusBtn=Button(buttonFrame,text='-',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
minusBtn.grid(row=1,column=3,padx=3,pady=3)


multBtn=Button(buttonFrame,text='x',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
multBtn.grid(row=2,column=3,padx=3,pady=3)


divideBtn=Button(buttonFrame,text='/',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
divideBtn.grid(row=3,column=3,padx=3,pady=3)


clearBtn=Button(buttonFrame,text='<---',font=font,width=11,relief='ridge',activebackground='orange',activeforeground='white',command=clear)
clearBtn.grid(row=4,column=0,columnspan=2,padx=3,pady=3)

allClearBtn=Button(buttonFrame,text='AC',font=font,width=11,relief='ridge',activebackground='orange',activeforeground='white',command=all_clear)
allClearBtn.grid(row=4,column=2,columnspan=2,padx=3,pady=3)
plusBtn.bind('<Button-1>',click_btn_function)
minusBtn.bind('<Button-1>',click_btn_function)
multBtn.bind('<Button-1>',click_btn_function)
divideBtn.bind('<Button-1>',click_btn_function)
zeroBtn.bind('<Button-1>',click_btn_function)
dotBtn.bind('<Button-1>',click_btn_function)
equalBtn.bind('<Button-1>',click_btn_function)
def enterClick(event):
    print('hi')
    e=Event()
    e.widget=equalBtn
    click_btn_function(e)

textField.bind('<Return>',enterClick)


# ***********************************************************

scFrame=Frame(window)
sqrtBtn=Button(scFrame,text='???',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
sqrtBtn.grid(row=0,column=0,padx=3,pady=3)

powBtn=Button(scFrame,text='^',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
powBtn.grid(row=0,column=1,padx=3,pady=3)


factBtn=Button(scFrame,text='x!',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
factBtn.grid(row=0,column=2,padx=3,pady=3)


radBtn=Button(scFrame,text='torad',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
radBtn.grid(row=0,column=3,padx=3,pady=3)

degBtn=Button(scFrame,text='todeg',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
degBtn.grid(row=1,column=0,padx=3,pady=3)

sinBtn=Button(scFrame,text='sin??',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
sinBtn.grid(row=1,column=1,padx=3,pady=3)

cosBtn=Button(scFrame,text='cos??',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
cosBtn.grid(row=1,column=2,padx=3,pady=3)

tanBtn=Button(scFrame,text='tan??',font=font,width=5,relief='ridge',activebackground='orange',activeforeground='white')
tanBtn.grid(row=1,column=3,padx=3,pady=3)


normalcalc=True

def calculate_sc(event):
    print('Button clicked')
    btn=event.widget
    text=btn['text']
    print(text)
    ex=textField.get()
    answer=''
    if text=='todeg':
        print("cal degree")
        answer=m.degrees(float(ex))


    elif text=='torad':
        print("radian")
        answer=str(m.radians(float(ex)))
    elif text=='x!':
        print("cal factorial")
        answer=str(m.factorial(int(ex)))
    elif text=='sin??':
        print("cal sin")
        answer=str(m.sin(m.radians(int(ex))))
    elif text=='cos??':
        print("cal cos")
        answer = str(m.cos(m.radians(int(ex))))
    elif text=='tan??':
        print("cal tan")
        answer = str(m.tan(m.radians(int(ex))))
    elif text=='???':
        print("sqrt")
        answer=m.sqrt(int(ex))
    elif text=='^':
        print("pow")
        base,pow=ex.split(',')
        answer=m.pow(int(base),int(pow))

    textField.delete(0, END)
    textField.insert(0, answer)
def sc_click():
    global normalcalc
    if normalcalc:

        buttonFrame.pack_forget()
        scFrame.pack(side=TOP)
        buttonFrame.pack(side=TOP,pady=20)
        window.geometry('500x700')
        print("show scientific")
        normalcalc=False
    else:
        print("Show Normal")
        scFrame.pack_forget()
        window.geometry('510x550')
        normalcalc=True
sqrtBtn.bind("<Button-1>",calculate_sc)
powBtn.bind("<Button-1>",calculate_sc)
factBtn.bind("<Button-1>",calculate_sc)
radBtn.bind("<Button-1>",calculate_sc)
degBtn.bind("<Button-1>",calculate_sc)
sinBtn.bind("<Button-1>",calculate_sc)
cosBtn.bind("<Button-1>",calculate_sc)
tanBtn.bind("<Button-1>",calculate_sc)

fontMenu=('',15)
menubar=Menu(window,font=fontMenu)

mode=Menu(menubar,font=fontMenu,tearoff=0)
mode.add_checkbutton(label="Scientific Calculator",command=sc_click)
menubar.add_cascade(label="Mode",menu=mode)



window.config(menu=menubar)

window.mainloop()