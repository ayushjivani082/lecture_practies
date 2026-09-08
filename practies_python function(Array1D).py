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

numbers = [10 , 20 , 30 , 40 , 50]

# Index start in array : 0
# Length calculate : 1


print(numbers[0])
print(numbers[2])
print(numbers[3])


for i in numbers:
    print(i)

# Ask the user how many element they want to enter.
# create an empty list
# use a for loop to take input
# Store each element using append().

# using for loop + append()

size = int(input("Enter size of Array:"))
numbers = [10 , 20 , 30 , 40 , 50]

for i in range(size):
    value = int(input(f"Enter Element{i + 1}:"))
    numbers.append(value)

print("\n Array Element:")

print(numbers)

for i in numbers:
    print(i)

# Using map() + split()


# Ask the user to enter all element in one line seperated by space.
# split() convert the input string into a list of string.
# map() convert each string into an integer.
# list() stores the result as a list.

numbers = list(map(int , input("Enter array Element:").split()))

for i in numbers:
    print(i)

print(numbers)


# Using List Comprehension

size = int(input("Enter size of Array:"))

numbers = [int(input(f"Enter Element{i + 1}"))for i in range(size)]

print(numbers)
    
