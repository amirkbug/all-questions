class Person():
    def __init__(self,Fname,Lname):
        self.fname = Fname
        self.lanem = Lname

class Student(Person):
    def __init__(self,Fname,Lname,age,score):
        super().__init__(Fname,Lname)
        self.age = age
        self.score = score



o1 = Student("javad","javadi",18,19)

print(o1.fname)
print(o1.score)
           