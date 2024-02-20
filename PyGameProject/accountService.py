import yaml

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