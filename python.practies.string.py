# pythobn string manipulation

s1 = "Hello"
s2 = 'World'
s3 = '''miltiline string'''
s4 = r"Raw \n string"


print(s1)
print(s2)
print(s3)
print(s4)

# cpmmon string Methods

s = "   Hello ,   World!   Hello  "


print(s.upper())
print(s.lower())
print(s)
print(s.lstrip())
print(s.rstrip())
print(s.replace("World" , "Python"))
print(s.split())
print(s.find("Hello"))
print(s.find("World"))
print(s.count("Hello"))
print(s.startswith("    Hello"))
print(s.endswith(" "))

#String Formatting

name = "Ayush"

age = 30

#f-string
print(f"Name : {name} , Age : {age}")

#.format()

print("Name: {} , Age:{}".format(name , age))


# % formtting

print("Name: %s , Age: %d"%(name , age))

# Padding and Aligment

print(f"{name:<10}")
print(f"{name:>10}")
print(F"{name:^10}")
print(f"{3.14156:.3f}")

# Slicing

s = "Hello , World!"

print(s[8])
print(s[-2])
print(s[0:6])
print(s[6])
print(s[:6])
print(s[::3])
print(s[::-2])


# joining and splitting

words = ["Python" , "is" , "Easy."]

print(" ".join(words))
print("_".join(words))

print("x , y , z".split(","))
print("Hello".split())

# Checking String Content

print("Hello123".isalpha())
print("123".isdigit())
print("hello123".isalnum())
print(" ".isspace())
print("HELLO".isupper())
print("hello".islower())











