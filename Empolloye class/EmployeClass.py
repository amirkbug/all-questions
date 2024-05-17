class Employe():
    def __init__(self,code,name,familyname,salary):
        self.code = code
        self.name = name
        self.familyname = familyname
        self.salary = salary
    def Fullname(self):
        return f"{self.name} {self.familyname}"
    def Calltax(self):
        if self.salary <= 150000:
            return 0
        return int(self.salary * 0.1)
    def __str__(self):
        pay = self.salary - self.Calltax()
        return f"--{self.Fullname()}--\n****{pay}****"

        

