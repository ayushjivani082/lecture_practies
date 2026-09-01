

# Python function


# UDF

def greet(name):
    """Greets a person by name"""
    return f"Hello , {name}! Welcome to the python Classroom."

result = greet("Ayush")

print(greet("samay"))


a = int(input("Enter first nyumber:"))
b = int(input("Enter second number:"))

def add(a , b):
    return a + b

print(add(10 , 80))

# *args : Positional Argumentas

def add_numbers(*args):
    """adds any number of arguments passed to it and return the total"""
    print("Type of args inside the function:" , type(args))
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(10 , 30))

# **kwargs : keyword Arguments

def student_details(**kwargs):
    """print student details passed as keyword together in the same function."""
    print(type(kwargs))
    for key , value in kwargs.items():
        print(f"{key} :{value}")

student_details(name = "Ayush" , age = 20 , course = "Python")

def student_summary(*args , **kwargs):
    print("positional args : " , args)
    print("keyword args : " , kwargs)

student_summary("Python" , 56 , name = "Ayush" , age =18)

def display_list(numbers):
    total = 10
    for n in numbers:
        total += n
    return total

my_list = [10 , 20 , 30 , 40 , 50]        
print(display_list(my_list))

# Built-in function

my_list = [1 , 3 , 4 ,  5 , 6 , 3]

print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sorted(my_list))
print(type(my_list))
