from tkinter import *

# main
main = Tk()
main.geometry("700x500")

# function
def CalculateAge():
    day2_entry_get = int(day2_entry.get())
    day_entry_get = int(day_entry.get())
    calculate_day = day2_entry_get + day_entry_get
    mounth2_entry_get = int(mounth_entry.get())
    mounth_entry_get = int(mounth_entry.get())
    calculate_mounth = mounth_entry_get + mounth2_entry_get
    year2_entry_get = int(year2_entry.get())
    year_entry_get = int(year_entry.get())
    calculate_year = year_entry_get - year2_entry_get
    while calculate_day >= 30:
            calculate_mounth += 1
            calculate_day -= 30

        
    age_label.config(text=f"day : {calculate_day} mounth: {calculate_mounth} year : {calculate_year*-1}")
    
    
    
    




# label
born_date = Label(main,text="تاریخ تولد",borderwidth=2,relief="solid",width=15,height=2)
born_date.place(x=500,y=2)

day = Label(main,text=":روز")
day.place(x=630,y=70)

mounth = Label(main,text=":ماه")
mounth.place(x=630,y=140)

year = Label(main,text=":سال")
year.place(x=628,y=200)

day_date = Label(main,text="تاریخ روز",borderwidth=2,relief="solid",width=15,height=2)
day_date.place(x=100,y=2)

day2 = Label(main,text=":روز")
day2.place(x=230,y=70)

mounth2 = Label(main,text=":ماه")
mounth2.place(x=230,y=140)

year2 = Label(main,text=":سال")
year2.place(x=230,y=200)

your_age = Label(main,text=": سن شما ",borderwidth=2,relief="solid",width=15,height=2)
your_age.place(x=315,y=350)



age_label = Label(main,text=" سال و _______ ماه و ______ روز  _______ ",font="arial 15")
age_label.place(x=180,y=450)
# entrys
day_entry = Entry(main,width=13)
day_entry.place(x=500,y=73)


mounth_entry = Entry(main,width=13)
mounth_entry.place(x=500,y=143)


year_entry = Entry(main,width=13)
year_entry.place(x=500,y=203)



day2_entry = Entry(main,width=13)
day2_entry.place(x=100,y=73)

mounth2_entry = Entry(main,width=13)
mounth2_entry.place(x=100,y=143)

year2_entry = Entry(main,width=13)
year2_entry.place(x=100,y=203)

# button
calculate_age = Button(main,text="محاسبه سن",width=15,height=2,command=CalculateAge)
calculate_age.place(x=315,y=140)

main.mainloop()