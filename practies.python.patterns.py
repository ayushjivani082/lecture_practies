# python patterns

n = 5

for i in range(1, n + 1):
    print(" " * (2 * (n - i)) + "  ".join("*" * i))

for i in range(n - 1, 0, -1):
    print(" " * (2 * (n - i)) + "  ".join("*" * i))


# star Triangle
    
print("\n STAR TRIANGLE")

rows = int(input("Enter number of rows:"))


for i in range(1 ,rows + 1):
    for j in range(i):
        print("*" , end=" ")
    print()


# inverted star triangle

print("\n Inverted star trinagle")

rows = int(input("Enter number of rows:"))

for i in range(rows ,  0 , -1):
    for j in range(i):
        print(i , end=" ")
    print()


# number triangle
rows = int(input("Enter number of rows:"))

for i in range(1 , rows + 1):
    for j in range(i):
        print(i , end= " ")
    print()


rows = int(input("Enter number of rows:"))

for i in range(rows , 0 , -1):
    for j in range(i):
        print(i , end=" ")
        
    print()


# Continuoes Number Triangle


rows = int(input("Enter number of rows:"))
number = 1

for i in range(1  , rows + 1):
    for j in range(i):
        print(number , end=" ")
        number += 1
    print()



# right-angle triangle

rows = int(input("Enter number of rows:"))

for i in range(1 , rows + 1):
    for j in range(rows - i):
        print("  "  ,end=" ")
    for j in range(i):
        print("*" , end=" ")
    print()


rows = int(input("Enter number of rows:"))

for i in range(1 , rows + 1):
    for j in range(rows - i):
        print("  " , end=" ")
    for j in range(2 * i - 1):
        print("*" , end=" ")
    print()    
    
