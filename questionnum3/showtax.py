from tkinter import *


main = Tk()



def showtax():

    top = Toplevel() 
    tax = int(salary_e.get()) * 0.15
    label_tax = Label(top,text=f"tax is : {int(tax)}")
    label_tax.pack()
    top.geometry("200x200")
    top.mainloop()


# label
Fname_lb = Label(main,text='Fname')
Fname_lb.place(x=5,y=5)

Lname_lb = Label(main,text='Lname')
Lname_lb.place(x=5,y=40)

code_lb = Label(main,text='code')
code_lb.place(x=400,y=5)

salary_lb = Label(main,text='salary')
salary_lb.place(x=400,y=40)

show_tax_lbl = Label(main,text="show tax",font="arial 10")
show_tax_lbl.place(x=250,y=200)

# entry
Fname_e = Entry(main,width=14)
Fname_e.place(x=50,y=5)



lname_e = Entry(main,width=14)
lname_e.place(x=50,y=40)

code_e = Entry(main,width=14)
code_e.place(x=480,y=5)


salary_e = Entry(main,width=14)
salary_e.place(x=480,y=40)


# btn
show_tax_btn = Button(main,text="show tax",width=15,height=2,command=showtax)
show_tax_btn.place(x=230,y=120)

# main
main.geometry('600x250')

# ob






main.resizable(0,0)
main.mainloop()