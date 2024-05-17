def Numberentered():
    numlist = []
    while True:
        input_num = int(input("enter some number -1 to exit : "))
        if input_num == -1:
            break
        numlist.append(input_num)
        sumnumlist = sum(numlist)
    print(numlist,sumnumlist)
       
Numberentered()