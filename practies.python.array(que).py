# Q.1 Find Length of array without buit - in function

n = int(input("Enter array size:"))

arr = []

for i in range(n):
    element = int(input(f"a[{i}] = "))
    arr.append(element)

count = 0

for element in arr:
    count = count + 1


print("Array Length :" , count)


# Q.2 Find average without built - in function

n = int(input("Enter array size:"))

arr  = []

for i in range(n):
    element = int(input(f"a[{i}] = "))
    arr.append(element)

total = 0

for element in arr:
    total = total + element

average = total / n

print("Average of an array : " , average)


# Q.3 sum of two 1d arrays

n = int(input("Enter array size:"))

a = []
b = []
c = []

for i in range(n):
    element = int(input(f"a[{i}]="))
    a.append(element)


for i in range(n):
    element = int(input(f"b[{i}]="))
    b.append(element)

for i in range(n):
    c.append(a[i] + b[i])

print("Array an C :" , c)


# Q.4 creat an array from 1 to 10 and multiply each lement by 2

arr = []

for i in range(1 , 11):
    arr.append(i)

print(arr)

arr_2 = []

for i in range(0 , 10):
    arr_2.append(arr[i]*2)

print(arr_2)

for element in arr:
    print(element * 2)


# Q.5 Check weather a number exists in an array

arr = [10 , 20 , 30 , 40 , 50]

print(arr)

n = int(input("Enter the element:"))

found = False

for i in range(len(arr)):
    if arr[i] == n:
        print(i)
        found = True
        break

if found == False:
    print("Not found")



# Q.6 Print all odd and even numbers from a user - define array


n = int(input("Enter array size:"))

arr = []
odd = []
even = []

for i in range(n):
    element = int(input(f"arr[{i}]="))
    arr.append(element)

print(arr)


for element in arr:
    if element % 2 == 0:
        even.append(element)

for element in arr:
    if element % 2 != 0:
        odd.append(element)

print(even)
print(odd)

# Q.7 find the every alternate element from array

arr = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80]

# first five element

print("First five element:", arr[:5])

# Every alternate element
print("Every alternate element:",arr[::2])

# Q.8  print the first , middle and last element in array

arr = [10 , 20 , 30 , 40 , 50]

print("First element:",arr[0])
print("Last element:",arr[-1])
print("middle element:",arr[len(arr)//2])
