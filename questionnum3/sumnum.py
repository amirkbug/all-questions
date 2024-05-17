def sumnum():
        input_num = input("enter num with space:")
        numlist = input_num.split()
        totla = 0
        for i in numlist:
            totla += int(i)
        print(totla)
        
sumnum()
                
