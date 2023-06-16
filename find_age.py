from tkinter import *
import datetime

root = Tk()
mylabel1 = Label()
mylabel1.grid(row=0,column=0)
mylabel1 = Label(text='Enter your Birth Date')
mylabel1.grid(row=1,column=0)
mylabel0 = Label()
mylabel0.grid(row=2,column=0)
def mycommand():
    year1 = myentry.get()
    birthyear = year1.split('/')[-1]
    current_year = datetime.date.today().year
    age = int(current_year)-int(birthyear)
    
    mylabel2 = Label(text=str(age))
    mylabel2.grid(row=8,column=0)


myentry = Entry(root,width='30',background='white',)
myentry.grid(row=3,column=0)
myentry.insert(0,'22/01/2002')
mylabel0 = Label()
mylabel0.grid(row=4,column=0)
    
mybutton = Button(root,text="clickme",padx=20,pady=5,command=mycommand,foreground='blue',bg='yellow')
mybutton.grid(row=5,column=0)
root.mainloop()
