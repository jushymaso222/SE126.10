import csv
import os


os.system('cls')

lname = []
fname = []
test1 = []
test2 = []
test3 = []

num_avg = []
let_avg = []

def menu():
    print("~CLASS ACCOUNT MENU~")
    print("1. Show All Students")
    print("2. Show Roster Only")
    print("3. Search for a Student")
    print("4. Exit")
    choice = int(input("Enter your choice [1 - 4]: "))

    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("*INVALID ENTRY* DIGITS 1 - 4 ONLY")
        choice = int(input("Enter your choice [1 - 4]: "))

    return choice

def seq_search(search_term):

    found_index = ""

    for i in range(0, len(lname)):
        if lname[i] == search_term:
            found_index = i
        elif fname[i] == search_term:
            found_index = i

    return found_index

with open("week5/week5_listReview/listPractice1.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        lname.append(rec[0])
        fname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))


for i in range(0, len(lname)):
    avg = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(avg)

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = 'D'
    elif avg < 60:
        letter = "F"
    else:
        letter = "ERROR @ I:" + str(i)

    let_avg.append(letter)





menu_choice = menu()

while menu_choice != 4:

    if menu_choice == 1:
        print(f"{'Last Name':12} \t {'First Name':12} \t {'Test 1':6} \t {'Test 2':6} \t {'Test 3':6} \t {'Avg':6} \t {'Letter':6}")
        print("-------------------------------------------------------------------------------------------------------")

        for i in range(0, len(lname)):
            print(f"{lname[i]:12} \t {fname[i]:12} \t {test1[i]:6} \t {test2[i]:6} \t {test3[i]:6} \t {num_avg[i]:6.1f} \t {let_avg[i]:6}")
    elif menu_choice == 2:
        print(f"{'Last Name':12} \t {'First Name':12} ")
        print("---------------------------")

        for i in range(0, len(lname)):
            print(f"{lname[i]:12} \t {fname[i]:12} ")
    else:
        print("Search for Student")
        search = input("Enter the LAST name you are looking for: ")

        found = seq_search(search)
        if found != "":
            print(f"{'Last Name':12} \t {'First Name':12} \t {'Test 1':6} \t {'Test 2':6} \t {'Test 3':6} \t {'Avg':6} \t {'Letter':6}")
            print("-------------------------------------------------------------------------------------------------------")
            print(f"{lname[found]:12} \t {fname[found]:12} \t {test1[found]:6} \t {test2[found]:6} \t {test3[found]:6} \t {num_avg[found]:6.1f} \t {let_avg[found]:6}")
        else:
            print("Record not found!")

    menu_choice = menu()

print("\n\nKeep the change ya filthy animal")