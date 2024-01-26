# Lab 3b - Joshua Mason SE111
# 
# This program will go through a list of voters and determine who is eligible, who is registered, and who voted for a final total of each

import csv
import os

os.system('cls') #This clears the screen
stack = [] #This hold the file information for later

#Initialize the variables for each respective total
inelligible = 0
ageNoReg = 0
eligNoVote = 0
voted = 0
records = 0

#Grabbing the file information
with open("week3/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        stack.append(rec) #Appending it to the stack variable from earlier

#Time to calculate the totals
for rec in stack:
    if int(rec[1]) < 18: #First successful check someone needs to pass, is whether they are old enough. This determines whether they are elligible to vote or not. If they are under 18, add to the inelligible list
        inelligible += 1
    else:
        if rec[2] == "N": #Next check we will run is whether they are registered to vote. If they aren't, add one to the ageNoReg list
            ageNoReg += 1
        else:
            if rec[3] == "N": #Finally we check to see if they voted. If they didn't, add one to the eligNoVote list and if they did, add one to the voted list
                eligNoVote += 1
            else:
                voted += 1
    records += 1 #Update the number of records processed as they go through

#Finally, print out all the values to the console!
print(f"Inelligible voters: {inelligible}")
print(f"Elligible but not registered voters: {ageNoReg}")
print(f"Elligible but didn't vote: {eligNoVote}")
print(f"Number of people who voted: {voted}")
print(f"Records processed: {records}")