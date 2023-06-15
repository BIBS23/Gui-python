from tkinter import *

root = Tk()

def mycommand():
    mylabel2 = Label(text='hi'+myentry.get())
    mylabel2.pack()




myentry = Entry(root,width='80')
myentry.pack()


    
mybutton = Button(root,text="clickme",padx=50,pady=20,command=mycommand,foreground='blue',bg='red')
mybutton.pack()
root.mainloop()
