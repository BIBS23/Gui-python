from tkinter import *

root = Tk()


mylabel0 = Label()
mylabel0.grid(row=0,column=0)
mylabel1 = Label(text='Enter you text')
mylabel1.grid(row=1,column=0)
mylabel0 = Label()
mylabel0.grid(row=2,column=0)
def mycommand():
 
    mylabel2 = Label(text='hi\t'+myentry.get())
    mylabel2.grid(row=7,column=0)


myentry = Entry(root,width='40',background='white')
myentry.grid(row=3,column=0)
mylabel0 = Label()
mylabel0.grid(row=4,column=0)
    
mybutton = Button(root,text="clickme",padx=30,pady=20,command=mycommand,foreground='blue',bg='red',)
mybutton.grid(row=5,column=0)
root.mainloop()
