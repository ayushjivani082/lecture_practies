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