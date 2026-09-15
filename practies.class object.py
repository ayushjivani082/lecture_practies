# Class Defination

class Car:
  # Constructor
  def __init__(self , brand , model , color , price):
    self.brand = brand
    self.model = model
    self.color = color
    self.price = price
  
  # Method

  def start(self):
    print(f"{self.brand} {self.model} is Starting.......🚙")


  # Method

  def details(self):
    print(f"""
    Brand : {self.brand}
    Model : {self.model}
    Color : {self.color}
    Price : {self.price}
    """)

# Creating Objects

car1 = Car('Honda' , 'City' , 'White' , 1200000)
car2 = Car('Audi' , 'R8' , 'Red' , 120000000)

# Accessing Object Data

print(car1)
car1.details()
car1.start()

car2.details()
car2.start()

# Simple Class

class Student:
  pass

s1 = Student()

print(s1)
print(type(s1))

# Class With Attributes

class Student:

  name = "Vivek"
  age = 27
  course = "Python"

s1 = Student()

print("Name:" , s1.name)
print("Age:" , s1.age)
print("Course:" , s1.course)


# Update Object Value

class Student:
  def __init__(self , name , salary):
    self.name = name
    self.salary = salary

s1 = Student("Raj" , 120000)

print(s1.name)
print(s1.salary)

s1.salary = 130000

print(s1.salary)



# class variablr

class College:

  college_name = "Red and White Education"

  def __init__(self , student):
    self.student = student

s1 = College("Ayush")
s2 = College("Ved")

print(s1.student , "--" , s1.college_name)
print(s2.student , "--" , s2.college_name)

# User input Object


class student:
  def __init__(self , name , age , course , marks):
    self.name = name
    self.age = age
    self.course = course
    self.marks = marks

def display(self):
  print("name:" , selg.name)
  print("Age:" ,self.age)
  print("Course:" , self.course)
  print("Marks:" , self.marks)

s1 = Student("Priya",  20 , "Python" , 89)

# print(f"""
# Name : {s1.name}
# age : {s1.age}
# course: {s1.course}
# marks : {s1.marks}
# """
# )

# s1.display()

name = input("Enter Name:")
age = int(input("Enter Age:"))
course = input("Enter course:")
marks = int(input("Enter marks:"))

s1 = Student(name , age , course , marks)

s1.display()

# Object Reference

s2 = s1

s2.display()

# Delete Attributes (del)

class Demo:

  def __init__(self):
    self.name = 'Python'
    self.duration = "6 Month"

  def display(self):
    print("Name : " , self.name)
    print("Duration : " , self.duration)


d1 = Demo()

 print(d1.name)
 print(d1.duration)

 d1.display()

del d1.display

d1.display()



 del d1.name
 del d1.duration


 print(d1.duration)
 print(d1.name)