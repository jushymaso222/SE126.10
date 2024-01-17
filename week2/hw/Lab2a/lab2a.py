# Lab 2A - Joshua Mason
#
# This program will run calculations to determine whether a room is safe for a specified number of people according to the fire code of the room.

#IMPORTS
import csv
import os

#Clear the screen cause I'm a weirdo and like my terminal to be clean
os.system('cls')

stack = [] #This stores the values read from the csv file to an array
totalRecs = 0
totalOver = 0

#Open the file and save the data to the stack variable for later
with open("week2/hw/Lab2a/lab2a.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        stack.append(record)
        totalRecs += 1 #Counts the total number of records it goes over (this will also be the same as #stack)

#Calculation function takes a record as an argument
def analyzer(rec):
    ans = float(rec[1]) - float(rec[2]) #Calculates the capacity of the room minus the total number of people attending
    if ans > 0:
        check = True #This check will stay true if the room is within capacity
    else:
        check = False #It will be false if it is over capacity (this will make life easier later)
    return ans, check

#PRINT HEADER
print(f"{'ROOM':20s}  {'MAX':4s} {'MIN':4s} {'OVER':4s}")
print("--------------------------------------")

#Iterating through the stack to check all of the records we added from the file earlier
for record in stack:
    process = analyzer(record) #Function will take the record and return two variables, the amount over if applicable, and a boolean stating whether it is over or not
    if process[1] == False: #Check for only records that exceed the capacity
        print(f"{record[0]:20s} {record[1]:4s} {record[2]:4s}{abs(process[0]):4.0f}")
        totalOver += 1

#FINAL PRINT STATEMENT
print(f"\n{totalRecs} records have been analyzed.\n{totalOver} meetings were over the max capacity.")