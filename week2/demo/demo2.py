import csv
import os

os.system('cls')
print(f"{'NAME':10s}\t{'AGE':2s}\t{'SALARY':10s}")
print("-------------------------------")

totalRecords = 0
totalSalaries = 0

stack = []

with open('week2/demo/example.csv') as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        stack.append(record)
        totalRecords += 1

for record in stack:
    print(f"{record[0]:10s}\t{record[1]:2s}\t{record[2]:10s}")
    totalSalaries += float(record[2])

print(f"\nTOTAL RECORDS: {totalRecords} | TOTAL SALARIES: ${totalSalaries:.2f}\n")

# for record in stack:
#     print(f"{record[0]} is {record[1]} years old!")
totalAge = 0
for record in stack:
    totalAge += int(record[1])
avgAge = totalAge / totalRecords

print(f"The total age of the set is: {totalAge}\nThe average age of the set is: {avgAge}")