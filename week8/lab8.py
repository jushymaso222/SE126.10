#  Lab 8 - Joshua Mason
#
#  Seat selection and purchasing program for a large theater
# -----------------------------------------------------------
#  Variable Dictionary:
#     seatMap - the dictionary which contains all seat information (usually pulled from the seatMap.yaml file)
#     alpha - the acceptable values for seats; contains the full alphabet and 1-4 for column names
#     printMap() - prints the seat map to the console
#     load() - loads the data from the file and creates a file with default values if not found
#     save() - saves all data from the seatMap list to the file
#     calculateTotal() - runs through the dictionary and calculates the total of seats sold by type and overall price
#     calculateSeats() - runs through the dictionary and calculates the total number of seats available by row and overall seats
#     selectSeat() - selects seats to add to your cart for purchasing later
#     menu() - recursive loop to get users input and run through available program functions
# -----------------------------------------------------------

#Imports
import os
import time #For stopping time like a superhero
import yaml #For data storage in files

rows = 15 #Number of rows on the plane
cols = 29 #Number of columns on the plane
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234" #The basic alphabet in order

seatMap = {}

def printMap():
    os.system('cls')

    print(" Row\t\t\t\t    Seats")
    print("      A B C D E F G H   I J K L M N O P Q R S T U V   W X Y Z 1 2 3 4\n")
    
    for i in range(0, rows): #This runs through the dictionary to print out the individual values in the 2d dictionary
        string = [] #Basic list for all the values in a given row
        for j in range(0, cols):
            letter = alpha[j]
            string.append(seatMap[str(i+1)][letter]) #Adds the value at the current index in the current dictionary to the 1D list
        print(f" {i+1:2}   {string[0]} {string[1]} {string[2]} {string[3]} {string[4]} {string[5]} {string[6]} {string[7]}   {string[8]} {string[9]} {string[10]} {string[11]} {string[12]} {string[13]} {string[14]} {string[14]} {string[15]} {string[16]} {string[17]} {string[18]} {string[19]} {string[20]}   {string[21]} {string[22]} {string[23]} {string[24]} {string[25]} {string[26]} {string[27]} {string[28]}") #Print out the values

def load():
    try:
        f = open("week8/seatMap.yaml","r")
    except:
        seatMap = {} #Initialize a dictionary
        #This for loop will contruct an empty dictionary based on the rows and columns set above
        for i in range(0, rows):
            seatMap[str(i+1)] = {} #Intializes a 2D dictitonary
            for j in range(0, cols):
                letter = alpha[j] #Sets an alphabetical value based on the index j from the alpha list declared earlier
                seatMap[str(i+1)][letter] = "#" #Sets the default value to the letter from the alphabet that corresponds with the given index

        time.sleep(5)
        f = open("week8/seatMap.yaml","wt") #The 'wt' stands for write
        yaml.dump(seatMap, f)

        f = open("week8/seatMap.yaml","r")

    return yaml.full_load(f)

def save(list):
    f = open("week8/seatMap.yaml","wt") #Saves the list to the file
    yaml.dump(list, f)

def calculateTotal():
    total = 0 #Overall total cost of seats
    totals = [0, 0, 0] #Total cost of seats by class

    for row in seatMap:
        for col in seatMap[row]:
            if seatMap[row][col] == "*": #Checks each value in the list for an '*' and if found performs the following
                if int(row) < 6: #Rows 1-5 are $200
                    total += 200
                    totals[0] += 200
                elif int(row) < 11: #Rows 6-10 are $175
                    total += 175
                    totals[1] += 175
                else: #All others higher than 11 are $150
                    total += 150
                    totals[2] += 150
    
    return total, totals #Returns both totals variables

def calculateSeats(): #Calculates the available seats
    rowSeats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #List of all available seats by row
    totalSeats = 0 #Overall total seats
    sold = 0 #How many seats have been sold

    for row in seatMap:
        for col in seatMap[row]:
            if seatMap[row][col] == "#": #Checks all values in the dictionary for a '#' then runs the following
                rowSeats[int(row)-1] += 1 #Adds a count to the respective row in the list
                totalSeats += 1 #Adds a count to the overall total
            else:
                sold += 1

    return rowSeats, totalSeats, sold #Returns all three variables



selectedSeats = [] #Initializing a list for the selected seats

def selectSeat(): #Select seats to add to cart
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
                if col in alpha: #Checks to make sure that the inputed value is in the alpha list but only up to the index set by the number of cols (the ':-(26-cols)' just removes all letters from the lists that are outside of the valid letters which in this case is only A B C D)
                    if seatMap[str(row)][col] != "X": #Checks to make sure the seat thasn't already been taken
                        print(f"You are selecting seat: {row}{col}")
                        answer = input("Are you sure this is the seat you want? [y / n]")
                        if answer.lower() == "y":
                            seatMap[str(row)][col] = "*" #Sets the seat to taken and appends it to the seat selection list
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
        while selecting != "y" and selecting != "n": #Trap loop for users giving incorrect responses
            selecting = input("Incorrect input. Would you like to reserve another seat? [y / n]")



def menu(): #Menu function 
    os.system('cls')

    printMap()

    print("\nPPAC Reservation System\n")
    print("\t1. Purchase Seat(s)")
    print("\t2. View Total Ticket Sales")
    print("\t3. View Sales Information")
    print("\t4. Checkout")
    print("\t5. Quit")

    answer = -1
    try:
        answer = int(input("Please select an option from the menu above [1 - 5]: "))
    except:
        print("**ERROR, NOT A VALID SELECTION!**")
        time.sleep(1)

    if answer != -1:
        return answer
    else:
        return menu() #Recursive trap loop :)
    

seatMap = load() #Loads the file (if the file does not exist, it will create a new one following gthe default values)

selection = -1    
while selection != 5:
    selection = menu() #Grab the users menu selection

    if selection == 1:
        selectSeat() #Add seats to cart
    elif selection == 2:
        os.system('cls')
        total, totals = calculateTotal() #Gets the totals for all sales
        print(f"Sales:\n\tPremium Seats: ${totals[0]:.2f}\n\tRegular Seats: ${totals[1]:.2f}\n\tEconomy Seats: ${totals[2]:.2f}\n\nTotal: ${total:.2f}")
        input("\nPress enter to continue...")
    elif selection == 3:
        os.system('cls')
        rows1, total, sold = calculateSeats() #Gets the total available seats from each row
        print("Available Seats:")
        print(f"\tRow 1: {rows1[0]}\n\tRow 2: {rows1[1]}\n\tRow 3: {rows1[2]}\n\tRow 4: {rows1[3]}\n\tRow 5: {rows1[4]}\n\tRow 6: {rows1[5]}\n\tRow 7: {rows1[6]}\n\tRow 8: {rows1[7]}\n\tRow 9: {rows1[8]}\n\tRow 10: {rows1[9]}\n\tRow 11: {rows1[10]}\n\tRow 12: {rows1[11]}\n\tRow 13: {rows1[12]}\n\tRow 14: {rows1[13]}\n\tRow 15: {rows1[14]}")
        print(f"\nTotal Seats Available: {total}")
        print(f"\nTotal Seats Sold: {sold}")
        input("\nPress enter to continue...")
    elif selection == 4:
        os.system('cls')
        print("\nHere are the seats you have reserved for:")
        totalPrice = 0 #Total price of all seats in the selectedSeats list
        for i in range(0, len(selectedSeats)): #Prints all the values in the seatsSelected list
            rowNum = int(selectedSeats[i][:-1]) #Removes the letter from the seat number to get just the row number and checks it against a few values
            if rowNum < 6: #This is the same total generator as above just for the selectedSeats list
                price = 200
                totalPrice += 200
            elif rowNum < 11:
                price = 175
                totalPrice += 175
            else:
                price = 150
                totalPrice += 150

            print(f"\t#{i+1}   {selectedSeats[i]}  Price: ${price:.2f}")
        print(f"\nTotal: ${totalPrice:.2f}")

        answer = "x"
        while answer != "y" and answer != "n": #Basic user trap loop for purchase selection
            answer = input("Would you like to purchase these tickets? [y / n]")
            if answer != "y" and answer != "n":
                print("Invalid response!")

        if answer == "y": #If seats are purchased, all selected seats are saved to the file
            save(seatMap)
            print("Purchased successfully!")
            selectedSeats = [] #Resets the purchased seats list so you can't purchase the same seats again
        else:
            answer1 = "x"
            while answer1 != "y" and answer1 != "n":
                answer1 = input("Would you like to clear your selections? [y / n]")
                if answer1 != "y" and answer1 != "n":
                    print("Invalid response!")

            if answer1 == "y":
                seatMap = load() #Reloads the file to restore the values from before selection began
                selectedSeats = [] #Clears the selected seats list
                print("Seat selection cleared!")

        time.sleep(3)
    
    elif selection != 5:
        print("**ERROR, NOT A VALID SELECTION!**")
        time.sleep(1)
    
print("Thank you for your time!") #End of program