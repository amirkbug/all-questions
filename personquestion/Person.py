class Person():
    def __init__(self,Fname,Lname):
        self.Fname = Fname
        self.Lname = Lname
    


class Employee(Person):
    def __init__(self, Fname, Lname,hoursofwork,hourlywage,salary):
        super().__init__(Fname, Lname)
        self.hoursofwork = hoursofwork
        self.hourlywage = hourlywage
        self.salary = salary

    def Calmorework(self):
        if int(self.hoursofwork) > 40:
            morehour = self.hoursofwork - 40
            moremoney = self.hourlywage * 1.5 * morehour
            CalSalary = self.salary + moremoney
            return int(CalSalary)
        
    def CalTax(self):
        tax = self.hoursofwork * 0.1
        return tax
    
    def GetSalary(self):
        if self.hoursofwork > 40:
            return self.Calmorework() + self.salary
        return self.salary
        
    def __str__(self):
        return f'--{self.Fname} {self.Lname}--\n your tax is: {self.CalTax()}'
    


        
                
            
