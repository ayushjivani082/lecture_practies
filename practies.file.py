# Q1.

try:
    a = float(input("Enter first number:"))
    b = float(input("Enter secon number:"))

    result = a/b

    print("Result :" , result)
except ZeroDivisionError:

   print("Error : Cannot divied by zero.")

print("Hello Python")


#Q.2

try:
    number = [1 , 2 , 3 , 4 , 5]
    index = int(input("Enter list index:"))
    print("Element :", number[index])

except IndexError:
    print("Error : Index does not exist.")
except ValueError:
    print("Error : Enter a valid integer index.")

#Q.3
try:
    filename = input("Enter filename:")
    file = open(filename , "r")
    content = file.read()
except FileNotFoundError:
    print("Error : File not found.")

else:
    print("File Content:")
    print(content)
    file.close()

#Q.4

import math

try:
    number = float(input("Enter a number:"))
    if number < 0:
        raise ValueError("Negative number is not allowed.")
except ValueError as a:
    print("Error :" ,a)

else:
    print("Square Root:" , math.sqrt(number))

finally:
    print("Execution completed.")
