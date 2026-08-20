# python cntrol flow

print("=== if statement ====")

age = 17

if age >= 18:
    print("you are eligible to vote")


    print("==== if ...else statement======")


age = 18

if age <= 18:
    print("you are eligible to vote")
else :
    print("you are not eligible to vote")



print("======= if...elif...else statement ======")
marks = 50


if marks >= 90:
     print("Grade A")
elif marks >= 80:
     print("Grade B")
elif marks >= 70:
     print("Grade C")
elif marks >= 60:
     print("Grade D")
else:
    print("fail")


print("==== nested statement =====")


age = 17
_id = True

if age >= 18:
    print("Age is valid")

    if _id:
        print("ID is available.")
        print("Entry allowed.")
    else:
        print("ID is not availbale.")

else:
    print("Age is not vallid.")



# match- case statement

#syntx


num1 = 15
num2 = 10
operator ="**"
match operator:

    case "+":
        print("addition = " , num1 + num2)
    case "-":
        print("subtraction = " , num1 - num2)
    case "*":
        print("multiplication = " , num1 * num2)
    case "/":
        print("division = " , num1 / num2)
    case _:
        print("Invalid Operator")

       
    
# multiple values in one case


char = "ab"

match char:

    case "a" | "e" | "i" | "o" | "u" :
        print("vowal")

    case _:
        print("consonant")    
 


















