import time
import yaml
import getpass as g

defaultListFile = "PyGameProject/profiles/default.yaml"

def createProfile(user, pass1):
  match = False
  while match == False:
    try:
      stream = open("PyGameProject/profiles/"+user+".yaml", 'r')
      return "exists"
    except:
        f = open("PyGameProject/profiles/"+user+".yaml","wt")
        info = {"User": user, "Pass": pass1}
        yaml.dump(info, f)
        return

def login(user, pass1):
    try:
      f = open("PyGameProject/profiles/"+user+".yaml","r")
      list = yaml.full_load(f)
      passTemp = list['Pass']
      if pass1 == passTemp:
        return list
      else:
        print("Incorrect password!")
        return "incpass"
    except:
      print("Username doesn't exist!")
      return "404"

def accountMenu():
  done = False
  while done == False:
    print("\033c",end='')
    print("Please select an option:")
    print("{1} Create Account")
    print("{2} Login")
    reading = input()
    try:
      reading = int(reading)
      if reading == 1:
        key = "createProfile"
        done = True
        return key
      elif reading == 2:
        key = "login"
        done = True
        return key
      else:
        print("Not a listed option.")
        time.sleep(3)
    except:
      print("Not a number.")
      time.sleep(3)
