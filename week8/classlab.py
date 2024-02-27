#IN CLASS LAB - WEEK 8 DAY 1
# PEOPLE:
#    Joshua Mason
#    Ryan Thomas
#    Mohammed Malek
#
# Airplane seating map and seat selector program
#
#
# VARIABLE DICTIONARY:
#    seatMap = dictionary that holds the data for the seats in a 2D key, pair system similar to Battleship
#    rows = the number of rows on the plane (allows for customization and bigger seat maps in the future)
#    cols = the number of cols on the plane
#    alpha = the alphabet as a string. this is used in the program to validate user input for the letter of each column
#    selectedSeats = a list of all the selected seats at the end of the program


import os #For clearing the screen
import time #Allow for the sleep() method to avoid clearing the screen immediately after errors are shown
os.system('cls') #Clears the screen

rows = 7 #Number of rows on the plane
cols = 4 #Number of columns on the plane
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #The basic alphabet in order

seatMap = {} #Initialize a dictionary
#This for loop will contruct an empty dictionary based on the rows and columns set above
for i in range(0, rows):
    seatMap[str(i+1)] = {} #Intializes a 2D dictitonary
    for j in range(0, cols):
        letter = alpha[j] #Sets an alphabetical value based on the index j from the alpha list declared earlier
        seatMap[str(i+1)][letter] = letter #Setst the default value to the letter from the alphabet that corresponds with the given index

#Visualization function
def printMap():
    os.system('cls')

    print("=================================")
    print("|     ROW #   -  -        -  -  |")
    
    for i in range(0, rows): #This runs through the dictionary to print out the individual values in the 2d dictionary
        string = [] #Basic list for all the values in a given row
        for j in range(0, cols):
            letter = alpha[j]
            string.append(seatMap[str(i+1)][letter]) #Adds the value at the current index in the current dictionary to the 1D list
        print(f"|      {i+1}      {string[0]}  {string[1]}        {string[2]}  {string[3]}  |") #Print out the values
    print("=================================")


selectedSeats = [] #All selected seats list is initialized empty

selecting = "y"
while selecting != "n":
    os.system('cls')
    printMap() #Shows the screen

    row = input("Input a row number: ")
    try: #This try/ except loop checks tot make sure the input is a number, if not it sets it to a basic value of 0
        row = int(row)
    except:
        row = 0

    if row != 0: #If the above value is valid, this will run
        if row >= 1 and row <= rows: #Checks to make sure the inputed value is a valid row
            col = input("Input a col number: ").upper() #Makes the letter uppercase
            if col in alpha and (col in alpha[:-(26-cols)]): #Checks to make sure that the inputed value is in the alpha list but only up to the index set by the number of cols (the ':-(26-cols)' just removes all letters from the lists that are outside of the valid letters which in this case is only A B C D)
                if seatMap[str(row)][col] != "X": #Checks to make sure the seat thasn't already been taken
                    print(f"You are selecting seat: {row}{col}")
                    answer = input("Are you sure this is the seat you want? [y / n]")
                    if answer.lower() == "y":
                        seatMap[str(row)][col] = "X" #Sets the seat to taken and appends it to the seat selection list
                        selectedSeats.append(f"{row}{col}")
                else:
                    print("**ERROR, SEAT TAKEN**")
                    time.sleep(2) #Sleeps for 2 seconds before clearing the screen
            else:
                print("**ERROR, NOT A SEAT**")
                time.sleep(2)
        else:
            print("ERROR, NOT A ROW**")
            time.sleep(2)
    else:
        print("**ERROR, INCORRECT INPUT**")
        time.sleep(2)
    selecting = input("\nWould you like to reserve another seat? [y / n]")
    while selecting != "y" and selecting != "n":
        selecting = input("Incorrect input. Would you like to reserve another seat? [y / n]")
printMap()

print("\nHere are the seats you have reserved for:")
for i in range(0, len(selectedSeats)): #Prints all the values in the seatsSelected list
    print(f"\t#{i+1}   {selectedSeats[i]}")