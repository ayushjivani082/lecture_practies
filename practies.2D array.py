array_2D = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]
print(array_2D)

# Q.1 3 x 3 matrix

matrix = []
for i in range(3):
    row = list(map(int , input("Enter rows {i + 1}:").split()))


    matrix.append(row)

print(matrix)


for row in matrix:
    for value in row:
        print(value , end = "\t")

    print()

# Q.2 Transpose of 2x3 matrix

matrix = []

for i in range(2):

    row = list(map(int , input(f"Enter row element {i + 1}:").split()))

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



# q.3 sum of all element

rows = int(input("Enter number of rows:"))

matrix = []

for i in range(rows):
    row = list(map(int , input(f"Enter row{i + 1}:").split()))

    matrix.append(row)

total = 0

for row in matrix:
    for value in row:
        total += value

print(total)


student = [
    ("Rahul" , 90),
    ("Amit" , 67),
    ("man" , 45),
    ("ved" , 88)
]


result = sorted(student , key = lambda x : x[1] , reverse = True)

print(result)
