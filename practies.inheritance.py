# 3. Multileval Inheritance

class Vehical:

    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def start (self):
        print(f"{self.brand} {self.model} has started.....")


class car(Vehical):

    def __init__(self , brand , model , fule_type):
        super().__init__(brand , model)
        self.fule_type = fule_type
    def fule_info(self):
        print(f"Fule_type : {self.fule_type}")

class motarcycle(car):

    def __init__(self , brand , model , average):
        super().__init__(brand , model , fule_type="Average")
        self.average = average


    def average_info(self):
        print(f"Average : {self.average}")

mv = motarcycle("TATA" , "Safari" , 60)

mv.start()

mv.average_info()

mv.fule_info()


# Hierarchical Inheritance

# Staffmember -> devloper , Tester

class StaffMember:

    def __init__(self , name , employee_id):
        self.name = name
        self.employee_id = employee_id

    def check_in(self):
        print(f"{self.name} (ID : {self.employee_id}) checked in for successfully>>>>>>>")

class Developer(StaffMember):

    def code(self):
        print(f"{self.name} is writing code>>>>>>>")

class Tester(StaffMember):

    def test(self):
        print(f"{self.name} is testing the application code>>>>>")


d = Developer("Ayush" , "E678")

d.check_in()

d.code()

print()

t = Tester("Man" , "E579")

t.check_in()

t.test()

# 5. Hybrid Inheritance

# Person -> Student & Employee -> TeachingAssistant

class Person:

    def __init__(self , name):
        self.name = name
    def profile(self):
        print(f"Name : {self.name}")

class Student(Person):

    def __init__(self , name , roll_num):
        Person.__init__(self , name)
        self.roll_num = roll_num

    def profile(self):
        print(f"Roll Number : {self.roll_num}")

class Employee(Person):

    def __init__(self , name , salary):
        Person.__init__(self , name)
        self.salary = salary
    def profile(self):
        print(f"Salary : {self.salary}")

class TeachingAssistant(Student , Employee):

    def __init__(self , name , roll_num , salary , subject):
     Student.__init__(self , name , roll_num)
     Employee.__init__(self , name , salary)
     self.subject = subject

    def profile(self):
     Person.profile(self)
     Student.profile(self)
     print(f"Salary : {self.salary}/month")
     print(f"Subject Assisting : {self.subject}")

ta = TeachingAssistant("Maan" , "N8990" , 7000 , "Python")

ta.profile
