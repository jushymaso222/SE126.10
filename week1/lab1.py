# Lab 1 - Room Capacity Calculator
# Joshua Mason
#
# This program is to calculate whether a certain request of people can fit into a specified room size without breaking the fire code of the room.
import os

#Calculates the difference between max people and requested people
def difference(people, max_people):
    dif = max_people - people
    return dif
    
#Trap loop for filtering responses from the user
def userLoop(response):
    while response != "y" and response != "n":
        os.system('cls')
        print("That is an invalid response, please try again.")
        print("Would you like to calculate another room? [y / n]")
        response = input()
    return response


#MAIN LOOP

os.system('cls') #This just clears the screen on Windows systems (doesn't work on Mac but will work in VSCode)
print("Welcome to the fire code calculator!\n")

active = True #Simple 'game' loop
while active:
    name = input("Please enter a name for the event: ")
    #Max room capacity
    roomcap = int(
        input("What is the max capacity of the room? ") #These get converted to integers for calculations later
    )
    #The requested number of people
    people = int(
        input("How many people will be attending? ")
    )

    answer = difference(people, roomcap) #Calling our previously made function
    os.system('cls')
    if answer >= 0:
        print("The room meets the fire code!\n")
        if answer > 0:
            print(f"You can still invite {answer} more people to the event!")
        else:
            print("You are at max capacity for the room!")
    else:
        print("The room does not meet the fire code!\n")
        absvalue = abs(answer) #Absolute value of the answer for later use in a print statement
        print(f"You are over capacity by {absvalue} people!")
        print("Try finding some people who are not required to attend or choose a different venue!")

    response = input("\nWould you like to calculate another room? [y / n]")
    finalresponse = userLoop(response) #Callback loop

    if finalresponse == "n":
        active = False
        os.system('cls')
        print("Goodbye!")
    else:
        os.system('cls')
    