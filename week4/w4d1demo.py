import csv
import os

os.system('cls')

fname = []
lname = []
test1 = []
test2 = []
test3 = []
avgList = []

with open("week4/listPractice1-1.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

    print(f"{'FNAME':12} \t {'LNAME':12} \t {'TEST1':5} \t {'TEST2':5} \t {'TEST3':5} \t {'AVG':10}")
    print("--------------------------------------------------------------")
for i in range(0, len(fname)):
    avg = (test1[i] + test2[i] + test3[i]) / 3
    avgList.append(avg)
    print(f"{fname[i]:12} \t {lname[i]:12} \t {test1[i]:5} \t {test2[i]:5} \t {test3[i]:5} \t {avg:5.1f}")

low_name = ""
low_avg = 100

for i in range(0, len(fname)):
    if avgList[i] < low_avg:
        low_avg = avgList[i]
        low_name = fname[i]

print(f"Number of students: {len(fname)}")
print(f"Lowest average: {low_name} \t {low_avg:.1f}")

all_students = []

for i in range(0, len(fname)):

    tempList = [fname[i], lname[i], test1[i], test2[i], test3[i], avgList[i]]
    all_students.append(tempList)

# for i in range(0, len(all_students)):
#     print(f"{all_students[i]}")

for i in range(0, len(all_students)):
    for j in range(0, len(all_students[i])):
        print(f"{all_students[i][j]}", end=" ")
    print("")