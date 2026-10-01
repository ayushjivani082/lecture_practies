# file = open("sample.txt", "x")

file = open("sample.py" , "w")

file.write("print('Hello World')")

file = open("sample.txt" , "r")

data = file.read()

# print(data)

file = open("sample.txt" , "w")

file.write("Learning File Handling in Python is Fun!!")

file = open("sample.txt" , "a")

file.write("\nPython is most popular language in the world....!")

file = open("sample.txt" , "r")

data = file.readline()

print(data)

file = open("notes.txt" , "w")

file.write("""
Line 1 :Python easy.
Line 2 :Python Hard.
Line 3 :Python Medium. 
"""
)

file.close()

