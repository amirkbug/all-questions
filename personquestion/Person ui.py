from tkinter import *
import Person

main = Tk()



def showsalary():
    e1 = Person.Employee(Fname_e.get(), lname_e.get(), float(hoursofwork_e.get()), float(hourlywage_e.get()), 12000)
    show_salary_lbl.config(text=f"Your salary is: {e1.GetSalary()}")
    


# label
Fname_lb = Label(main,text='Fname')
Fname_lb.place(x=5,y=5)

Lname_lb = Label(main,text='Lname')
Lname_lb.place(x=5,y=40)

hoursofwork_lb = Label(main,text='hoursofwork')
hoursofwork_lb.place(x=400,y=5)

hourlywage_lb = Label(main,text='hourlywage')
hourlywage_lb.place(x=400,y=40)

show_salary_lbl = Label(main,text="show salary",font="arial 10")
show_salary_lbl.place(x=250,y=200)

# entry
Fname_e = Entry(main,width=14)
Fname_e.place(x=50,y=5)



lname_e = Entry(main,width=14)
lname_e.place(x=50,y=40)

hoursofwork_e = Entry(main,width=14)
hoursofwork_e.place(x=480,y=5)


hourlywage_e = Entry(main,width=14)
hourlywage_e.place(x=480,y=40)


# btn
show_salary_btn = Button(main,text="show salary",width=15,height=2,command=showsalary)
show_salary_btn.place(x=230,y=120)

# main
main.geometry('600x250')

# ob






main.resizable(0,0)
main.mainloop()