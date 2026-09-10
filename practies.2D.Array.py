array_2D = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]

print(array_2D)

#Q.1 3x3 matrix

matrix = []

for i in range(3):
    row = list(map(int , input(f"Enter row {i + 1}:").split()))

    matrix.append(row)

print(matrix)

for row in matrix:
    for value in row:
        print(value , end="\t")

    print()

    
#Q.2 Transpose 2x3 matrix



matrix = []

for i in range(2):

    row = list(map(int , input(f"Enter row element {i + 1} :").split()))

    matrix.append(row)

print(matrix)

for row in matrix:
    print(row)

transpose = []

for j in range(3):

    temp = []

    for i in range(2):

        temp.append(matrix[i][j])

    transpose.append(temp)

for row in transpose:
    print(row)


num = [1 , 2 , 3 , 4 , 5]

total = 0

for i in num:
    total = total + i

print(total)


#Q.3 sum of all element


rows = int(input("Enter number of rows:"))

matrix = []

for i in range(rows):
    row = list(map(int , input(f"Enter row {i + 1} :").split()))

    matrix.append(row)

total = 0

for row in matrix:
    for value in row:
        total += value
        
print(total)


#Q.6 sorted function

students = [
        ("Rahul" , 80),
        ("Amit" , 45),
        ("Priya" , 65),
        ("Neha" , 70)
]

result = sorted(students , key = lambda x : x[1] , reverse=True)

print(result)

#Q.4 max and min value in 2D array

arr = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]

maximum = arr[0][0]
minimum = arr[0][0]


for row in arr:
    for value in row:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value


print("maximum value:", maximum)
print("Minimum value:", minimum)


#Q.5 sort a list in ascending order

number = [40 , 30 , 50 , 10 , 20]

number.sort()

print("Sorted list:" , number
      )

#Q.7 sorted list of dictionary by specific key

student = [
    
    {"name":"Ayush","mark":90},
    {"name":"raj","mark":89},
    {"name":"lalit","mark":67},
    {"name":"Amit","mark":78}
]
sorted_student = sorted(student , key = lambda x:x["mark"])
for student in sorted_student:
    print(student)



#Q.8 diffrence between sort() and sorted()

numbers = [10 , 20 , 40 , 60 , 70 , 90]

# sort() changes thr original list

print("After sort():",numbers)

# sorted() creates a new list
numbers = [10 , 20 , 30 , 40 , 50]
new_list = sorted(numbers)

print("Original list:", numbers)
print("New sorted list:", new_list)
