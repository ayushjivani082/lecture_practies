
# pattern

rows = int(input("Enter number of rows:"))
for i in range(1 , rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(rows-1,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()


'''

data = []

def add_data():
    global data
    print("\n=== Input Data ===")
    raw_input = input("Enter numbers separated by spaces: ")
    
    
    string_numbers = raw_input.split()
    
    data = []
    for num in string_numbers:
        data.append(int(num))
        
    print("Data has been saved successfully!")

def data_summary():
    if len(data) == 0:
        print("\nNo data found! Please input data first.")
        return
        
    print("\n=== Data Summary ===")
    print("Total elements :", len(data))
    print("Minimum value  :", min(data))
    print("Maximum value  :", max(data))
    print("Sum of values  :", sum(data))
    
    
    avg = sum(data) / len(data)
    print("Average value  :", round(avg, 2))

def factorial(n):
    
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

def run_factorial():
    print("\n=== Calculate Factorial ===")
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")

def filter_data():
    if len(data) == 0:
        print("\nNo data found! Please input data first.")
        return
        
    print("\n=== Filter Data ===")
    threshold = int(input("Enter threshold value: "))
    
    
    my_filter = lambda x: x >= threshold
    filtered_result = list(filter(my_filter, data))
    
    print(f"Values greater than or equal to {threshold}: {filtered_result}")

def sort_data():
    if len(data) == 0:
        print("\nNo data found! Please input data first.")
        return
        
    print("\n=== Sort Data ===")
    print("1. Ascending Order")
    print("2. Descending Order")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        data.sort()
        print("Sorted Data:", data)
    elif choice == "2":
        data.sort(reverse=True)  
        print("Sorted Data:", data)
    else:
        print("Invalid sorting choice.")

def display_statistics():
    if len(data) == 0:
        print("\nNo data found! Please input data first.")
        return
        
    print("\n=== Dataset Statistics ===")
   
    minimum = min(data)
    maximum = max(data)
    total_sum = sum(data)
    average = sum(data) / len(data)
    
    
    print(f"Min: {minimum} | Max: {maximum} | Sum: {total_sum} | Avg: {round(average, 2)}")


# MAIN MENU 
while True:
    print("\n=== Welcome to Data Analyzer Program ===")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    
    choice = input("Please enter your choice (1-7): ")
    
    if choice == "1":
        add_data()
    elif choice == "2":
        data_summary()
    elif choice == "3":
        run_factorial()
    elif choice == "4":
        filter_data()
    elif choice == "5":
        sort_data()
    elif choice == "6":
        display_statistics()
    elif choice == "7":
        print("\nThank you for using the program. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please try again.")
