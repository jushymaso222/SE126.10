import csv
import os
import time
import yaml

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
        f = open("week8/seatMap.yaml","wt")
        yaml.dump(seatMap, f)

        f = open("week8/seatMap.yaml","r")

    return yaml.full_load(f)

def save(list):
    f = open("week8/seatMap.yaml","wt")
    yaml.dump(list, f)

def calculateTotal():
    total = 0
    totals = [0, 0, 0]

    for row in seatMap:
        for col in seatMap[row]:
            if seatMap[row][col] == "*":
                if int(row) < 6:
                    total += 200
                    totals[0] += 200
                elif int(row) < 11:
                    total += 175
                    totals[1] += 175
                else:
                    total += 150
                    totals[2] += 150
    
    return total, totals

def calculateSeats():
    rowSeats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    totalSeats = 0
    sold = 0

    for row in seatMap:
        for col in seatMap[row]:
            if seatMap[row][col] == "#":
                rowSeats[int(row)-1] += 1
                totalSeats += 1
            else:
                sold += 1

    return rowSeats, totalSeats, sold



selectedSeats = []

def selectSeat():
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
        while selecting != "y" and selecting != "n":
            selecting = input("Incorrect input. Would you like to reserve another seat? [y / n]")



def menu():
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
        return menu()
    

seatMap = load()

selection = -1    
while selection != 5:
    selection = menu()

    if selection == 1:
        selectSeat()
    elif selection == 2:
        os.system('cls')
        total, totals = calculateTotal()
        print(f"Sales:\n\tPremium Seats: ${totals[0]:.2f}\n\tRegular Seats: ${totals[1]:.2f}\n\tEconomy Seats: ${totals[2]:.2f}\n\nTotal: ${total:.2f}")
        input("\nPress enter to continue...")
    elif selection == 3:
        os.system('cls')
        rows, total, sold = calculateSeats()
        print("Available Seats:")
        print(f"\tRow 1: {rows[0]}\n\tRow 2: {rows[1]}\n\tRow 3: {rows[2]}\n\tRow 4: {rows[3]}\n\tRow 5: {rows[4]}\n\tRow 6: {rows[5]}\n\tRow 7: {rows[6]}\n\tRow 8: {rows[7]}\n\tRow 9: {rows[8]}\n\tRow 10: {rows[9]}\n\tRow 11: {rows[10]}\n\tRow 12: {rows[11]}\n\tRow 13: {rows[12]}\n\tRow 14: {rows[13]}\n\tRow 15: {rows[14]}")
        print(f"\nTotal Seats Available: {total}")
        print(f"\nTotal Seats Sold: {sold}")
        input("\nPress enter to continue...")
    elif selection == 4:
        print("\nHere are the seats you have reserved for:")
        totalPrice = 0
        for i in range(0, len(selectedSeats)): #Prints all the values in the seatsSelected list
            rowNum = int(selectedSeats[i][:-1])
            if rowNum < 6:
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
        while answer != "y" and answer != "n":
            answer = input("Would you like to purchase these tickets? [y / n]")
            if answer != "y" and answer != "n":
                print("Invalid response!")

        if answer == "y":
            save(seatMap)
            print("Purchased successfully!")
        else:
            answer1 = "x"
            while answer1 != "y" and answer1 != "n":
                answer1 = input("Would you like to clear your selections? [y / n]")
                if answer1 != "y" and answer1 != "n":
                    print("Invalid response!")

            if answer1 == "y":
                seatMap = load()
                print("Seat selection cleared!")

        time.sleep(3)
    
    elif selection != 5:
        print("**ERROR, NOT A VALID SELECTION!**")
        time.sleep(1)
    
print("Thank you for your time!")