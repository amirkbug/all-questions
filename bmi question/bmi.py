from tkinter import *


# main
main = Tk()
main.geometry("400x400")
# functions
def CalculateBmi():
    label_weight_entry_get = label_weight_entry.get()
    label_height_entry_get = label_height_entry.get()
    bmi = float(label_weight_entry_get) / float(label_height_entry_get)
    label_calculated.config(text=f"your bmi is : {float(bmi)}")
    print(bmi)
    
    
    



# labels
label_weight = Label(main,font="arial 17",text="وزن :")
label_weight.place(x=1,y=5)

label_height = Label(main,font="arial 20",text="قد :")
label_height.place(x=1,y=90)


label_calculated = Label(main,text=f"your bmi :",font="arial 15")
label_calculated.place(x=4,y=300)

# entrys
label_weight_entry = Entry(main,width=30)
label_weight_entry.place(x=70,y=13)


label_height_entry = Entry(main,width=30)
label_height_entry.place(x=70,y=95)


# buttons
calculate_button = Button(main,text="محاسبه",width=10,command=CalculateBmi)
calculate_button.place(x=160,y=180)
main.mainloop()