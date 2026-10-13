# HDF function

numbers = [12 , 34 , 45 , 54 ,56]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Original List:", numbers)
print("Ascending Order:", ascending)
print("Descending Order:", descending)

# sort strings by length

words = ["apple", "banana", "cherry", "grepas", "elderberry"]

sotred_by_length = sorted(words, key=len)

print("Words sorted by Length: ", sotred_by_length)

# sort Strings by last letter using lambda function

sorted_by_last_letter = sorted(words, key=lambda x: x[-1])

print("Words sorted by Last Letter: ", sorted_by_last_letter)

# sort list of dictionaries by age

students = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 30}
]

sorted_students = sorted(students, key=lambda x: x["age"])
print("Students sorted by Age: ", sorted_students)

# map() - Square Every Number

import math

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda X: X ** 2, numbers))
print(squares)

# map() - Apply 18% tax to priace 

prices = [100, 200, 300, 400, 500]

final_prices = list(map(lambda price:int(price + (price * 18 / 100)), prices))

print(final_prices)

# filter() - Filter Even Numbers

numbders = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda X : X % 2 == 0, numbders))
print(even_numbers)

#filter() - string with length greater than 5

words = ["apple", "banana", "cherry", "grapes", "elderberry"]

long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)