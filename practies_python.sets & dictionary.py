

print("=" * 50)

print("01. set")

numbers = {1 , 2 , 3 , 4 , 5 }

print(numbers)
numbers.add(6)

print(numbers)

numbers.remove(3)

print(numbers)

print(3 in numbers)
print(2 in numbers)

# Dictionary

print("=" * 50)
print("02. Dictionary")

student = {
    "name":"ayush",
    "age":18,
    "grade":"A"
}

print(student["name"])

for key in student.keys():
    print(f"{key} : {student[key]}")
for value in student.values():
    print(value)

student["city"] = "Surat"

student["age"] = 25

print(student)

# dictionary from list

print("=" * 50)

key = ["id" ,  "name" , "email"]
value = [101 , "rakesh" , "rakesh@gmail.com"]

print(len(key))

print(key , value)

employee = {}

for i in range(len(key)):
    employee[key[i]] = value[i]

print(employee)

# Type conversion

print("=" * 40)

num = "123"
print(type(num))
print(type(int(num)))

list1 = [1 , 2 , 3 , 4 , 5 , 6 ]
tuple1 = tuple(list1)

print(list1)
print(tuple1)

pairs = [(1 , "Apple") , (2 , "Mango")]

dict1 = dict(pairs)

print(dict1)


# Delete item using del keyword

numbers = [10 , 20 , 30 , 40 , 50]

print(numbers)

del numbers[0]
print(numbers)
