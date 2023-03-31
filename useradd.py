import os
def new_user():
  confirm="N"
  while confirm != "Y":
      username = input("enter the name to user to add: ")
      print("use the user name'"+ username + "'?(Y/N)")
      confirm = input().upper()
       
  os.system("sudo useradd "+ username)
new_user()