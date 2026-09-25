# polymorphism

# 1. Method Overloading

# Using Default Parameter

class calculator:
    def add(self , a, b=0 , c=0):
        return a + b + c
c = calculator()

print(c.add(10 , 20))
print(c.add(10 , 20 , 30))
print(c.add(20))

# Using *args

class Calculator:
    def add(self , *num):
        return sum(sum)

c = calculator()

print(c.add(10))
print(c.add(10 , 30))
print(c.add(10 , 20 , 40))


# 2. Method Overriding

class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("BHow BHow")

class Cat(Animal):

    def sound(self):
        print("meow meow")

d = Dog()

d.sound()

c = Cat()

c.sound()

a = Animal()

a.sound()

class Employee:

    def work(self):
        print("employee is working")

class Developer:

    def work(self):
        print("Developer is wrtting coad")

class Designer:

    def work(self):
        print("designer is creating UI")

d = Developer()
e = Employee()
f = Designer()

d.work()
e.work()
f.work()

# with differnt classes

companys = [Developer() , Employee() , Designer()]
for company in companys:
    company.work()


# issubclass()

print(issubclass(Employee , Developer))

print(issubclass(Dog , Animal))

print(issubclass(Animal , Dog))


# super()

class Person:

    def __init__(self , name):
        self.name = name

class Student(Person):

    def __init__(self , name , marks):
        super().__init__(name)
        self.marks = marks

s = Student("Raj" , 68)

p = Person("Ayush")

print(s.name)
print(s.marks)
print(p.name)

class Employee:

    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Nmae : {self.name}")
        print(f"Salary : {self.salary}")

class Developer(Employee):

    def __init__(self ,name , salary , language):
        super().__init__(name , salary)
        self.language = language

    def display(self):
        super().display()
        print(f"Language : {self.language}")

d = Developer("Ayush" , 56000 , "English")

print(d.name)
print(d.salary)
print(d.language)


d.display()
    