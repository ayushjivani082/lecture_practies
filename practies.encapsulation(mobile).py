# Mobail Behavior

class Mobile:

  #constructor
  def __init__(self , owner):
    self.owner = owner
    self.__password = "123456"
    self.__status = "Locked"

  # Unlock Mobile

  def unlock(self , password):

    if password == self.__password:
      self.__status = "Unlocked"
      print("\n ✅Mobile Unlocked Successfully.")

    else:
      print("\n Incorrect Password!")


  # Lock Mobile

  def lock(self):
    self.__status = "Locked"
    print("\n Mobile Locked.")

  # change password

  def change_pass(self , old_password , new_password):
    if old_password == self.__password:
      if len(new_password) >= 4:
        self.__password = new_password
        print("\n ✅ Password Changed Successfully.")
      else:
        print("Password must be at least 4 digit...")

    else:
      print("\n Old Password is incorrect.")

  # display 

  def display(self):

    print("======== Mobile Details =========")

    print("Owner : " , self.owner)
    print("Status : " , self.__status)

    print("=================================")


owner = input("Enter Mobile Owner Name : ")

mobile = Mobile(owner)

while True:

  print("\n====== Menu ========")
  print("1. Unlock Mobile")
  print("2. Lock Mobile")
  print("3. Change password")
  print("4. Mobile Status")
  print("5. Exit")


  choice = int(input("Enter Choice: "))

  if choice == 1:

    password = input("Enter Password:")

    mobile.unlock(password)

  elif choice == 2:

    mobile.lock()

  elif choice == 3:

    old_password = input("Enter Old Password:")
    new_password = input("Enter New Password:")

    mobile.change_pass(old_password , new_password)

  elif choice == 4:

    mobile.display()

  elif choice == 5:

    print('\n Thank you....')

    break

  else:
    
    print("Invalid choice")
