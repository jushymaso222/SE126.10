import csv

id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open("week7/w7_demoFile.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        id_stud.append(rec[0])
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])

for i in range(0, len(lname)):
    print(f"{id_stud[i]}\t{lname[i]}\t{fname[i]}")


search_name = input("Enter the nums you are looking for: ")

found = []
seq_count = 0
for i in range(0, len(lname)):
    seq_count += 1
    if search_name.lower() == lname[i].lower():
        found.append(i)

print(f"\n\nSearching complete. Search loop ran {seq_count} iterations.")
if found != -1:
    print(f"\nWe found {search_name} at index position(s): {found}")
    print("\tHere is their info: ")
    for i in found:
        print(f"\t\t{fname[i]}\t{lname[i]}\t{id_stud[i]}\t{class1[i]}\t{class2[i]}\t{class3[i]}")
else:
    print(f"\nWe could not find {search_name}")
    print("\tPlease try again.")


#BINARY SEARCH

search_name = input("Enter the last nums you are looking for: ")
bin_count = 0

min = 0
max = len(lname) - 1
mid = int((min + max) / 2)

while (min < max and search_name != lname[mid]):
    bin_count += 1
    if search_name < lname[mid]:
        max = mid - 1
    else:
        min = mid + 1

    mid = int((min + max) / 2)

if search_name == lname[mid]:
    print(f"\n\nSearching complete. Search loop ran {bin_count} iterations.")
    print(f"\nWe found {search_name} at index position: {mid}")
    print("\tHere is their info: ")
    print(f"\t\t{fname[mid]}\t{lname[mid]}\t{id_stud[mid]}\t{class1[mid]}\t{class2[mid]}\t{class3[mid]}")
else:
    print(f"\nWe could not find {search_name}")
    print("\tPlease try again.")


#BUBBLE SORT

nums = [100, 75, 32, 250, 47, 9, 2, 3, 99, 200]

print(f"Current List: {nums}")

for i in range(0, len(nums) - 1):#outter loop

    #print("OUTER LOOP! i = ", i)

    for index in range(0, len(nums) - 1):#inner loop

        #print("\t INNER LOOP! k = ", index)
        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(nums[index] > nums[index + 1]):

            print("\t\t SWAP! ", nums[index], "<-->", nums[index + 1])
            #if above is true, swap places!
            temp = nums[index]
            nums[index] = nums[index + 1]
            nums[index + 1] = temp

print(f"Sorted List: {nums}")
