# Lab 2B - Joshua Mason
#
# Display a CSV file in a readable table in the console

#IMPORTS
import csv
import os

#I really need to clear the screen I swear, it's non-negotiable... I need it to be Mr. Clean
os.system('cls')

stack = [] #Holds the CSV file information
totalRecs = 0
totalOver = 0

#Grabbing the CSV file information
with open("week2/hw/Lab2b/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        stack.append(record) #Oh boy, here's that stack reference again (think of it as preserving the with open() loop outside of the loop itself)
        totalRecs += 1

#PRINT HEADER
print(f"{'Device':10s} {'Brand':8s} {'CPU':5s} {'RAM':5s} {'Disk 1':9s} {'Disks':5s} {'Disk 2':9s} {'OS':7s} {'Year'}")
print("------------------------------------------------------------------------\n")

#Here comes the fun part
for record in stack:
    if record[0] == "D": #This will take the shorthand letters and convert them to words for the print statement later
        commtype = "Desktop"
    else:
        commtype = "Laptop"

    if record[1] == "DL": #This will convert the shorthand abbreviations to manufacturer names
        manufacturer = "Dell"
    elif record[1] == "GW":
        manufacturer = "Gateway"
    else:
        manufacturer = record[1]

    #And here is where we deal with whoever decided to not include blank spaces in the CSV file itself... you know what you did whoever you are, this would make a programmers life hell in the job world
    if len(record) == 9:
        print(f"{commtype:10s} {manufacturer:8s} {record[2]:5s} {record[3]:5s} {record[4]:9s} {record[5]:5s} {record[6]:9s} {record[7]:7s} {record[8]}")
    else:
        print(f"{commtype:10s} {manufacturer:8s} {record[2]:5s} {record[3]:5s} {record[4]:9s} {record[5]:5s} {'':9s} {record[6]:7s} {record[7]}")

#FINAL PRINT STATEMENT
print(f"\nTotal computers: {totalRecs}")

#Peter Piper picked a peck of pickled peppers. If Peter Piper picked a peck of pickled peppers, how many pickled peppers did Peter Piper pick?
#At this poitn I'm just having fun with the documentation. Hopefully it's still informative to you but with some extra pizzazz
#And to answer my own question, he picked zero pickled peppers. They can't be pickled until after they are picked unless you grow them in a barrel of vinegar in which case: don't.