# Lab 3a - Joshua Mason SE111
#
# Using the csv file from last week, this program will calculate how many desktops and laptops need to be replaced and how expensive it would be to replace them

import csv 
import os

os.system('cls') #clear the console
stack = [] #this will store the decoded csv file into an array of lists
desktops = 0
laptops = 0

#Pulling information from the csv file
with open("week3/lab3a.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        stack.append(rec) #Appends it to the stack created earlier
#---------------------------------------

#Main calculations begin with sorting the records
for rec in stack:
    #First, we need to check if the record we are looking at is 9 in length or 8 since not all of the records line up the same
    if len(rec) == 9:
        year = int(rec[8]) #then set the value to the according record index
    else:
        year = int(rec[7])
    
    #Now we need to check if the computer is a 2016 or earlier
    if year <= 16:
        if rec[0] == "D": #If it is, we check what kind of computer it is and add 1 to its respective list
            desktops += 1
        else:
            laptops += 1

#All done, now we just add up the total from the numbers we gained (desktops are $2000 and laptops are $1500)
totalD = desktops * 2000
totalL = laptops * 1500

#Finally we print our results
print(f"Total desktops that need to be replaced: {desktops}\n\tTotal: ${totalD}")
print(f"Total desktops that need to be replaced: {laptops}\n\tTotal: ${totalL}")