
x = 7
y = "Hello"
z = 3.14
# arithmetic operator


print("addition:" , x + z)
print("substraction:" , x - z)
print("multiplication:" , x * z)
print("division:" , x / z)
print("modulus:" , x % z)
print("floor division" , x // z)
print("Expontiations:" , x ** x)

# assignment operator

opr1 = 6
opr2 = 9

opr1 += opr2 # opr1 = opr1 + opr2

print(opr1)

opr1 -= opr2

print(opr1)

opr1 *= opr2

print(opr1)

opr1 /= opr2

print(opr1)

opr1 %= opr2

print(opr1)

opr1 **= opr2

print(opr1)


# comparision operator

a = 9
b = 9

print("01. == Equal : " , a == b)
print("02. != Not Equal : " , a != b)
print("03. > Greater Than : " , a > b)
print("04. < Less Than : " , a < b)
print("05. <= Less/Equal : " , a <= b)
print("06. >= Greater/Wqual : " , a >= b)

#logical operator

a = True
b = False
c = False

print("01. and logical AND : " , a and b)
print("02. or logiocal OR : " , a or b)
print("03. not logical NOT : " , not b)



# bitwise operator

a = 7
b = 4

print("& Bitwise AND : " , a & b)
print("| Bitwise OR : " , a | b)
print("^ Bitwise XOR : " , a ^ b)
print("~ Bitwise NOT : " , ~b)
print(" << Left Shift :" , a << 1)
print(">> Right Shift : " , a >> 1)

# conditional / ternary operator

age = 14

result = 'ADULT' if age >= 18 else  'MINOR'

print(result)

# operator Precedence

result = 11 + 8 * 6

print(result)

# type conversion

#id()

a = 23
b = 22

print(id(a))
print(id(b))

# Identity operator

a = [5 , 6 , 7]
b = a
c = [5 , 6 , 7]


print(a is b)
print(a is c)
print(a is not c)

# membership operator



numbers = [1 ,  2 , 3 , 4 , 5]

print(20 in numbers)
print(2 in numbers)
print(20 not in numbers)







