from tkinter import *
from main import Main

top = Tk()

top.geometry('800x800')
top.config(bg='#00ccff')
top.title("Online classes Automation")
top.iconbitmap('icon.ico')

Label(top, text="ONLINE CLASSES AUTOMATION",
      font=('Lato', '28', 'bold')).grid(row=0, column=0, sticky=W, pady=40, padx=35)

Label(top, text="Welcome, Press 'START' button to activate the bot!",
      font=('Lato', '18', 'bold')).grid(row=1, column=0, sticky=W, pady=20, padx=45)


def check_res():
    Main(var1.get())


var1 = IntVar()
Button(top, text="START", command=check_res,
       height=3, width=15, relief=RIDGE, background='#b3f0ff', activebackground='#33cc33', bd=4, font=('Lato', '20', 'bold')).grid(pady=20)
Button(top, text='QUIT', command=top.quit,
       height=3, width=15, relief=RIDGE, background='#b3f0ff', activebackground='#ff3300', bd=4, font=('Lato', '20', 'bold')).grid(pady=20)

chbtn1 = Checkbutton(top, text='Notify me on WhatsApp',
                     variable=var1, font=('Lato', '15'), width=20).grid(pady=25)

top.mainloop()
