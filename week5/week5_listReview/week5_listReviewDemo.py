#Week 5 LIST REVIEW

#

#----------------------------------------------------------------
import csv


#FUNCTION--------------------------------------------------------

def menu():

    print("1. SHOW NUMERIC AVERAGE")
    print("2. SHOW LETTER AVERAGE")
    print("3. PRINT STARTING FILE")
    print("4. EXIT")

    choice = int(input("Please enter your selecton: "))

    while choice < 0 or choice > 4:

        print("**ERROR**ERROR**")
        choice = int(input("Please enter your selecton: "))

    return choice


#list creation -- create empty lists, one per field of data in the file we are storing from

firstname = []
lastname = []
test1 = []
test2 = []
test3 = []
teacher = []

records = 0

#connect to the file, read the data, and store data into lists
with open("week5/week5_listReview/listPractice1.txt") as unicorn:

    file = csv.reader(unicorn)

    for rec in file:

        #print(rec)     #test a print of records to make sure file is connected and can be read

        firstname.append(rec[0])
        lastname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
        teacher.append("KT")

        records += 1 #records = records + 1

        

#below is no longer connected to file / LIST PROCESSING ONLY!

#process the lists to print to the console
#PROCESS THE LIST --> FOR LOOP! 

#for index in range(0, records):

    #print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3}".format(firstname[index], lastname[index], test1[index], test2[index], test3[index], teacher[index]))


num_avg = []

#process the test scores for each student and find their average (numeric) then, store into a new list
for index in range(0, records):

    grade_sum = test1[index] + test2[index] + test3[index]

    grade_avg = grade_sum / 3 

    num_avg.append(grade_avg)


#for index in range(0, records):

#    print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3} \t {6:4.2f}".format(firstname[index], lastname[index], test1[index], test2[index], test3[index], teacher[index], num_avg[index]))


letter_avg = []

for index in range(0, records):

    if num_avg[index] >= 90:

        letter = "A"

    else: 
        letter = "Not A"

    letter_avg.append(letter)



#for index in range(0, records):

#   print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3} \t {6:4.2f} \t {7:2}".format(firstname[index], lastname[index], test1[index], test2[index], test3[index], teacher[index], num_avg[index], letter_avg[index]))






menu_choice = menu()

while menu_choice != 4: #while menu_choice is not the exit option 

    if menu_choice == 1: #printing numeric averages

        print("\n\t NUMERIC AVERAGES\n")
        
        for index in range(0, records):

            print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3} \t {6:4.2f}".format(firstname[index], lastname[index], test1[index], test2[index], test3[index], teacher[index], num_avg[index]))


    elif menu_choice == 2: #printing letter averages

        print("\n\t LETTER AVERAGES\n")

        for index in range(0, records):

            print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3} \t {6:4.2f} \t {7:2}".format(firstname[index], lastname[index], test1[index], test2[index], test3[index], teacher[index], num_avg[index], letter_avg[index]))

    elif menu_choice == 3: #printing starting file 

        print("\n\t STARTING FILE\n")

        for index in range(0, records):

            print("{0:15} \t {1:15} \t {2:3} \t {3:3} \t {4:3} \t {5:3}".format(firstname[index], lastname[index], test1[index], test2[index], test3[index], teacher[index]))

    else: #exit -- wont be in the loop at all 

        print("\n\tERROR\n")


    menu_choice = menu()

print("\n\n\nthank you & goodbye!")