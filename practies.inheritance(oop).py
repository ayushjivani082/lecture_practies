# single inheritance

# Bank Account -> SavingsAccount

class BankAccount:

    def __init__(self , account_holder , account_number , balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Account Balance : {self.balance}")

class SavingsAccount(BankAccount):

    def __init__(self , account_holder , account_number , balance , intrest_rate):
        super().__init__(account_holder , account_number , balance)
        self.intrest_rate = intrest_rate

    def add_intrest(self):
        intrest = self.balance * self.intrest_rate / 100
        self.balance += intrest
        print(f"Intrest added: ${intrest:.2f} at {self.intrest_rate}% rate")

class CurrentAccount(BankAccount):

    def __init__(self , account_holder , account_number , balance , intrest_rate):
        super().__init__(account_holder , account_number , balance)
        self.intrest_rate = intrest_rate

    def add_intrest(self):
        intrest = self.balance * self.intrest_rate / 100
        self.balance += intrest
        print(f"Intrest added: ${intrest:.2f} at {self.intrest_rate}% rate")

acc_s = SavingsAccount("Kushal Vora" , "SBI178726r78" , 10000 , 4)
acc_c = CurrentAccount("Ayush Jivani" , "SBI56564667" , 12000 , 6)

acc_s.display()

acc_s.add_intrest()

acc_s.display()

acc_c.display()
acc_c.add_intrest()
acc_c.display()


# Multiple Inheritance

# Teacher + Administrator + Headmaster

class Teacher:
    def __init__(self , subject):
      self.subject = subject

    def teach(self):
      print(f"Teaching {self.subject} to students.")

class Administrator:

    def __init__(self , department):
        self.department = department

    def manage(self):
        print(f"Managing the {self.department} department")

class Headmaster(Teacher , Administrator):

    def __init__(self , subject , department , school_name):
        Teacher.__init__(self , subject)
        Administrator.__init__(self , department)
        self.school_name = school_name

    def guide(self):
        print(f"Guiding staff and student at {self.school_name}")


head = Headmaster("Maths" , "Academic" , "litter flower school")

head.teach()
head.manage()
head.guide()
   

