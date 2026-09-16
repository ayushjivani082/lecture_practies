# real world : Online shopping costomers
'''
class Customer:

  def __init__(self , name):
    self.name = name
  
  def shopping(self):
    print(f"{self.name} is shopping.")

  def __del__(self):
    print(f"{self.name} logged out.")

c1 = Customer("Rahul")

del c1

c1.shopping()


'''

# Employee Attendence

class Employee:
    def __init__(self):
        self.name = "Ayush"
        self.department = "IT"

    def display(self):
        print("Employee :" , self.name)
        print("Department :" , self.department)

    def __del__(self):
        print(self.name , "Left office. Goodbye.")

e1 = Employee()

e1.display()

# Bank Account

class BankAccount:

    def __init__(self , account_holder , account_number , balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposite(self , amount):

        if amount > 0:
            self.balance += amount
            print(f"{amount} Successfully deposite.")
        else:
            print("Invalid Deposite amount.")

    def withdraw(self , amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balnce.")
        else:
            self.balance -= amount
            print("f{amount} Withdraw Successfully.")

    def check_balance(self):

        print(f"Current Balance : {self.balance}")

    def display(self):
        print("Account Holder:" , self.account_holder)
        print("Account Number:" , self.account_number)
        print("Current Blanvce:" , self.balance)

name = input("Enter your name:")
account_num = int(input("Enter account number:"))
balance = float(input("Enter Opening Balance:"))

account = BankAccount(name , account_num  , balance)

while True:

    print("========bank menu=======")
    print("1. Deposite")
    print("2. Withdraw")
    print("3. Check Blance")
    print("4. Display Account")
    print("5. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:

        amount = float(input("Enter Deoposite amount:"))

        account.deposite(amount)

    elif choice == 2:

        amount = float(input("Enter Withdraw amount:"))

        account.withdraw(amount)

    elif choice == 3:

        account.check_balance()

    elif choice == 4:

        account.display()

    elif choice == 5:

        print("Thank you for choosing Bank of Baroda.")

    else:

        print("Invalid Choice")



    