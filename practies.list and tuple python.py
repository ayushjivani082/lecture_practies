# collection Datatyaes

fruits = ["Apple" , "Banana" , "Mango" , "Graps" , "Orange"]

print("Original list : " , fruits)
print("Second Element of fruits : " , fruits[2])
print("Last Element of fruits : " , fruits[-3])
fruits[0] = "Watermelon"

# append

fruits.append("Kivi")
print("Original List : " , fruits)

# remove Element

fruits.pop(0)
print("Original List : " , fruits)

#Sorting
fruits.sort()
print("Original List : " , fruits)

#reverse the list
fruits.reverse()
print("Original List : " , fruits)


#Tuple

number = (10 , 20 , 30 , 40 , 50 , 60 , 70)

#Access

print(number[2])

#List and Tuple with same items

list_data = ["python" , "Java" , "c++"]
tuple_data = ["Python" , "Java" , "c++"]

print(list_data == tuple_data)

# List comprehension

square_num = []

for number in range(1,80):
    square_num.append(number ** 2)

print(square_num)

# syntax

square = [number ** 2 for number in range(2 , 890)]
print(square)

# Even number using list comprehension
number = list(range(1 , 70))

even_num = [number for number in number if number % 2 == 0]
print(even_num)
