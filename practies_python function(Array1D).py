# Global Variable

total = 0

def add_number(num):
    global total
    total += num


n = int(input("How many number do you want to enter?"))

for i in range(n):
    num = int(input("Enter number:"))
    add_number(num)

print("Total sum :" , total)


username = "Guest"

def change_username(new_name):
    global username
    username = new_name

print(username)

new_username = input("Enter new number:")

change_username(new_username)

print(username)


value = 100

def show_value():
    value = 50
    print(value)

show_value()

print(value)



# Function task list and returns:

def list_operation(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total , maximum , minimum

numbers = [10 , 20 , 30, 40 , 50 , 50]

total , maximum , minimum = list_operation(numbers)


print(total)
print(maximum)
print(minimum)




# 1D array

#1. Homogeneous Array

number = [10 , 20 , 30 , 40 , 50]

fruits = ['apple' , 'banana' , 'orange' , 'mango']

#2. Heterogeneous Array

student = ["Ayush" , 18 , 90.90 , True]
print(student)






