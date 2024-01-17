import csv
import os
os.system('cls')

stack = []
totalRecs = 0

fnames = []
lnames = []
favenums = []
faveanimals = []

with open('week2/w2d2demo/w2d2_demoTextFile.txt') as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        stack.append(record)

        fnames.append(record[0])
        lnames.append(record[1])
        favenums.append(int(record[2]))
        if len(record) == 4:
            faveanimals.append(record[3])
        else:
            faveanimals.append("N/A")

        totalRecs += 1

for index in range(0, totalRecs):
    print(f"{fnames[index]:10s} {lnames[index]:1s}   {favenums[index]:3.0f}   {faveanimals[index]}")
