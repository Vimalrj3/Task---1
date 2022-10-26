import re

def user_login():

  flag=1

  global Email
  while flag==1:
    regex = re.compile(r'([A-Za-z]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    Email = input('Enter Email id: ')
    #Email_Database=[]
    if re.fullmatch(regex, Email):
      pass
      f=open("database.txt","r")
      data=f.read()
      if Email in data:
        f.seek(0)
        while True:
          data = f.readline()
          if data!="":
            dt=data.split()
            if dt[0] == Email:
              print("Email Exist!!")
              flag=0
              break
      else:
        login1(Email)
    break


def login1(Email):
  flag = 0
  l, u, p, d = 0, 0, 0, 0
  password = input('Enter Password: ')
  capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  smallalphabets = "abcdefghijklmnopqrstuvwxyz"
  specialchar = ".$@_"
  digits = "0123456789"
  l_p = len(password)
  if l_p >= 8 and l_p <= 16:
    for i in password:
      if (i in smallalphabets):
        l += 1
      if (i in capitalalphabets):
        u += 1
      if (i in digits):
        d += 1
      if (i in specialchar):
        p += 1
    if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == l_p):
      f = open("database.txt", "a")
      f.writelines([Email, "\t", password])
      f.write("\n")
      print("Registered Successfully")

    else:
      print("Invalid Password, Try again")
  else:
      print("invalid Password, Try again")
  return

def pswd(Email):

  flag = 0
  l, u, p, d = 0, 0, 0, 0
  password = input('Enter Password12: ')
  capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  smallalphabets = "abcdefghijklmnopqrstuvwxyz"
  specialchar = ".$@_"
  digits = "0123456789"
  l_p = len(password)
  if l_p >= 8 and l_p <= 16:
    for i in password:
      if (i in smallalphabets):
        l += 1
      if (i in capitalalphabets):
        u += 1
      if (i in digits):
        d += 1
      if (i in specialchar):
        p += 1
    if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == l_p):

      f = open("database.txt", "a")
      f.writelines([Email, "\t", password])
      f.write("\n")
      print("Registered Successfully")

      f.close()

    else:
      print("Invalid Password, Try again")
  else:
    print("Invalid Password, Try again")

def update(Email):
  l, u, p, d = 0, 0, 0, 0
  password = input('Update Enter Password: ')
  capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  smallalphabets = "abcdefghijklmnopqrstuvwxyz"
  specialchar = ".$@_"
  digits = "0123456789"
  l_p = len(password)
  if l_p >= 8 and l_p <= 16:
    for i in password:
      if (i in smallalphabets):
        l += 1
      if (i in capitalalphabets):
        u += 1
      if (i in digits):
        d += 1
      if (i in specialchar):
        p += 1
    if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == l_p):

      f = open("database.txt", "r+")

      while True:
        data=f.readline()
        dt=data.split()

        if dt[0]==Email:
          dt[1]= password
          break

      print("Updated Password Successfully")
      f.close()

    else:
      print("Invalid Password, Try again")
  else:
    print("Invalid Password, Try again")


def login():
  Email=input("Enter Email id :")
  f=open("database.txt","r")
  dt=f.read()

  if dt != "":
    dt = dt.split()
    if dt[0] == Email:
      while True:
        password=input("Enter password :")
        if dt[1]==password:
          print("Login Successfully!!")
          break
        else:

          ch=input("Forgot Password Yes/No :")
          if ch=="Yes" or ch=="yes":
            update(Email)

while True:
  print("1.Create User :")
  print("2.Login :")
  ch=input("Enter your option 1/2:")
  if ch=="1":
    user_login()
    break
  elif ch=="2":
    login()
  else:
    break
