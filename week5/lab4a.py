#Lab 4 - Joshua Mason
#
#Displaying a list based on 1D lists from a CSV file

#Imports
import csv
import os


os.system('cls') #It's an addiction... I need it to be cleared

#Initializing 1D lists... and no I don't mean One Direction, they aren't a thing anymore
fname= []
lname = []
age = []
nname = []
house = []

#Opening the file for it's juicy information for me to steal I mean borrow
with open("week5/lab4A.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: #Appending all the fields to the respective lists
        fname.append(rec[0])
        lname.append(rec[1])
        age.append(int(rec[2])) #Don't forget to turn this guy to a number, he's been a very good string and deserves a raise
        nname.append(rec[3])
        house.append(rec[4])

#file closed------

print("\n\n") #SPACE, OH GOD I NEED SPACE

#STEP ONE - PRINT OUT THE LIST
print(f"{'First Name':12} \t {'Last Name':12} \t {'Age':4} \t {'Nickname':18} \t {'House Allegiance':20}") #Some headers and stuff
print("-------------------------------------------------------------------------------------")

for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {age[i]:4} \t {nname[i]:18} \t {house[i]:20}") 

#END OF STEP ONE

print("\n\n") #MORE SPACE, ITS NOT ENOUGH SPACE

#STEP TWO - ADD HOUSE MOTTOS
motto = [] #New list for the respective mottos
houseTallies = [0,0,0,0,0,0] #tallies of all the house allegiances instead of making 6 more 1D lists, I combined them into one 1D list with each index corresponding to the order below

for i in range(0, len(fname)): #Add mottos and tally houses for later secret shenanigans
    if house[i] == "House Stark":
        motto.append("Winter is Coming") #Can it not? I've had enough of the cold already...
        houseTallies[0] += 1
    elif house[i] == "House Baratheon":
        motto.append("Ours is the fury.")
        houseTallies[1] += 1
    elif house[i] == "House Tully":
        motto.append("Family. Duty. Honor.")
        houseTallies[2] += 1
    elif house[i] == "Night's Watch":
        motto.append("And now my watch begins.") #He finally got a new battery for his watch and can tell the time again
        houseTallies[3] += 1
    elif house[i] == "House Lannister":
        motto.append("Hear me roar!") #Rawr
        houseTallies[4] += 1
    elif house[i] == "House Targaryen":
        motto.append("Fire & Blood")
        houseTallies[5] += 1
    else:
        motto.append("N/A") #Just in case, added a little error catch for this 

#REPRINT
print(f"{'First Name':12} \t {'Last Name':12} \t {'Age':4} \t {'Nickname':18} \t {'House Allegiance':20} \t {'House Motto':20}") #MMMMMMMmmmmm more print statements
print("-------------------------------------------------------------------------------------------------------------------")

for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {lname[i]:12} \t {age[i]:4} \t {nname[i]:18} \t {house[i]:20} \t {motto[i]:20}")

#END OF STEP TWO

print("\n\n") #THE SPACE, I NEED IT

#STEP THREE - AVERAGE AGE

#Initializing values for the total and average age
sumAge = 0
avgAge = 0

for i in range(0, len(fname)):
    sumAge += age[i] #Adding up all the ages instead of using the much more helpful and quicker sum() function... its a for loop instead

avgAge = sumAge / len(fname) #Average = Sum / Num of Items

#SO MANY PRINT STATEMENTS
print(f"Total Records: {len(fname)}") 
print(f"Average Age Amoungst Records: {avgAge:.0f}")
print("House Tallies:")

#And here, we do a classic thing known as pulling those previous values from our other for loop back out for our print statements... I really didnt want to write another for loop and that one already went through house mottos sooooooo
print(f"\tHouse Stark: {houseTallies[0]}")
print(f"\tHouse Baratheon: {houseTallies[1]}")
print(f"\tHouse Tully: {houseTallies[2]}")
print(f"\tNight's Watch: {houseTallies[3]}")
print(f"\tHouse Lannister: {houseTallies[4]}")
print(f"\tHouse Targaryen: {houseTallies[5]}")

#And now we have finished! With three, count em' three, print statements (not literally there are so many)
#Sorry for the comments, but they were fun and absolutely necessary for my code to function properly

