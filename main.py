import math_utils as math
import math as m
import string_utils as s
import helper

print("Addition  of 5 and 3 is:", math.add(5, 3))
print("Subtraction of 5 and 3 is:", math.subtract(5, 3))
print("Multiplication of 5 and 3 is:", math.multiply(5, 3))
print("Division of 5 and 3 is:", math.divide(5, 3))


print('49 square root is:', m.sqrt(49))

angle = m.radians(30)

print(angle)

print(m.sin(angle))

text = input("Enter a string :")

print("Number of Vowels:" , s.count_vowel(text))
import greet as g

g.greet("Ayush")

print("square:" , helper.square(5))
print("Cube:" , helper.cube(5))