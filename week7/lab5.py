# Lab 5 - Joshua Mason
#
# Searching through a student record table and returning records based upon search criteria
# menu() - The main menu loop of the program is run through here
#   returns the response
# seqSearch() - Sequential search algorithm developed into a function. Can take 1 to 3 lists if needed
#   returns a list of found indices
# binSearch() - Binary search algorithm developed into a function. Can take 1 to 6 lists if needed
#   returns a single index


#----IMPORTS----
import csv
import os

#MENU FUNCTION START
def menu():
    print("Please select an option from the menu below:\n\t1. See All Student Reports\n\t2. Search for a Student by ID\n\t3. Search for a Student by LAST NAME\n\t4. View a Class Roster by CLASS ID\n\t5. Exit\n") 
    response = input("[1 - 5]: ")
    while response != '1' and response != '2' and response != '3' and response != '4' and response != '5': #User trap loop
        print("--INVALID INPUT--")
        response = input("Please enter a valid menu option [1 - 5]: ")
    return response #returns the response 1-5

#----1D Lists----
sID = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

#----Gathering data----
with open("week7/lab5_students.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        sID.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

#----Sequential search function----
def seqSearch(searchTerm, table, table2 = None, table3 = None): #tables 2 and 3 are given default values making them optional (not necessary but adds versatility)
    foundValues = [] #Initialize the found indices list
    if table2 == None: #if only 1 table is given
        for i in range(0, len(table)):
            if table[i] == searchTerm:
                foundValues.append(i)
    elif table3 == None: #if 2 tables are given
        for i in range(0, len(table)):
            if table[i] == searchTerm or table2[i] == searchTerm:
                foundValues.append(i)
    else: #if all three tables are given
        for i in range(0, len(table)):
            if table[i] == searchTerm or table2[i] == searchTerm or table3[i] == searchTerm:
                foundValues.append(i)
    return foundValues #returns all found indices or an empty list if none were found

#----Binary search function----
def binSearch(searchTerm, table):
    min = 0
    max = len(table) - 1
    mid = int((min + max) / 2)

    while (min < max and searchTerm != table[mid]):
        if searchTerm < table[mid]:
            max = mid - 1
        else:
            min = mid + 1

        mid = int((min + max) / 2)
        
    if searchTerm == table[mid]:
        return mid #returns the index if found
    else:
        return False #returns false if nothing found

#----Bubblesort function----
def bubbleSort(table, table1 = None, table2 = None, table3 = None, table4 = None, table5 = None): #Again, only 1 list is required, all the rest are optional for versatility
    #This function will always sort based on the required first list. All optional lists are just moved along with it
    for i in range(0, len(table) - 1):
        for k in range(0, len(table) - 1):
            if table[k] > table[k + 1]:
                temp = table[k]
                table[k] = table[k + 1]
                table[k + 1] = temp

                if table1 != None: #this will only run if there are 2 or more lists
                    temp = table1[k]
                    table1[k] = table1[k + 1]
                    table1[k + 1] = temp

                if table2 != None: #this will only run if there are 3 or more lists
                    temp = table2[k]
                    table2[k] = table2[k + 1]
                    table2[k + 1] = temp

                if table3 != None: #this will only run if there are 4 or more lists
                    temp = table3[k]
                    table3[k] = table3[k + 1]
                    table3[k + 1] = temp

                if table4 != None: #this will only run if there are 5 or more lists
                    temp = table4[k]
                    table4[k] = table4[k + 1]
                    table4[k + 1] = temp

                if table5 != None: #this will only run if there are all 6 lists
                    temp = table5[k]
                    table5[k] = table5[k + 1]
                    table5[k + 1] = temp

#----MAIN PROGRAM----
program = 0 #initialize while loop variable
while program != 5:
    os.system('cls') #I love clearing the screen...
    print("--+Student Records Program+--\n")
    program = int(menu()) #Call that menu function from before to givethe user options

    if program == 1: #Print all records
        os.system('cls')
        bubbleSort(sID, lname, fname, class1, class2, class3) #Sorts the lists to the first table [sID] 
        print("===============================================================================")
        print(f"{'ID':5} \t {'LNAME':10} \t {'FNAME':10} \t {'CLASS1':8} \t {'CLASS2':8} \t {'CLASS3':8}")
        print("===============================================================================")
        for i in range(0, len(lname)):
            print(f"{sID[i]:5} \t {lname[i]:10} \t {fname[i]:10} \t {class1[i]:8} \t {class2[i]:8} \t {class3[i]:8}")
        input("\nPress enter to continue...")
    elif program == 2: #Search by student ID
        os.system('cls')
        bubbleSort(sID, lname, fname, class1, class2, class3) #Sorts the lists to the first table [sID]

        search = input("Please enter the STUDENT ID of the student you are looking for: ")
        student = binSearch(search, sID) #Runs a binary search with the search term 'search' from the sID list
        if student != False:
            print(f"We found your student at index: {student}")
            print("Here is their info:")
            print("\n===============================================================================")
            print(f"{'ID':5} \t {'LNAME':10} \t {'FNAME':10} \t {'CLASS1':8} \t {'CLASS2':8} \t {'CLASS3':8}")
            print("===============================================================================")
            print(f"{sID[student]:5} \t {lname[student]:10} \t {fname[student]:10} \t {class1[student]:8} \t {class2[student]:8} \t {class3[student]:8}")
            input("\nPress enter to continue...")
        else: #the binSearch function returned False meaning there were no matches found
            print("Student not found in records!")
            input("\nPress enter to continue...")
    elif program == 3: #Search by Last Name
        os.system('cls')
        bubbleSort(lname, sID, fname, class1, class2, class3) #Sorts the lists to the second table [lname]

        search = input("Please enter the LAST NAME of the student you are looking for: ")
        student = binSearch(search, lname) #Runs a binary search with the search term 'search' from the lname list (after sorted accorrdingly)
        if student != False:
            print(f"We found your student at index: {student}")
            print("Here is their info:")
            print("\n===============================================================================")
            print(f"{'ID':5} \t {'LNAME':10} \t {'FNAME':10} \t {'CLASS1':8} \t {'CLASS2':8} \t {'CLASS3':8}")
            print("===============================================================================")
            print(f"{sID[student]:5} \t {lname[student]:10} \t {fname[student]:10} \t {class1[student]:8} \t {class2[student]:8} \t {class3[student]:8}")
            input("\nPress enter to continue...")
        else: #The binSearch function returned False meaning there were no matches
            print("Student not found in records!")
            input("\nPress enter to continue...")
    elif program == 4: #Print class roster
        os.system('cls')

        search = input("Please enter the CLASS ID of the roster you want to view: ")
        roster = seqSearch(search, class1, class2, class3) #Runs the sequential search function for all three class lists
        if roster != []:
            print(f"Class Roster for {search}:")
            print("\n===============================================================================")
            print(f"{'ID':5} \t {'LNAME':10} \t {'FNAME':10} \t {'CLASS1':8} \t {'CLASS2':8} \t {'CLASS3':8}")
            print("===============================================================================")
            for index in roster:
                print(f"{sID[index]:5} \t {lname[index]:10} \t {fname[index]:10} \t {class1[index]:8} \t {class2[index]:8} \t {class3[index]:8}")
            input("\nPress enter to continue...")
        else: #The sequential search function returned an empty list therefore, no matches were found
            print("Class not found in records!")
            input("\nPress enter to continue...")

#Exit the main loop
os.system('cls')
print("Thank you, goodbye!")