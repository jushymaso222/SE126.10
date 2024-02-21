import csv

type = []
name = []
meaning = []
origin = []

with open("week7/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        origin.append(rec[3])

def bubbleSort(table, table2, table3, table4): #The first list is the list that it is sorting through, all others just get swapped with it
    for i in range(0, len(table) - 1):
        for k in range(0, len(table) - 1):
            if table[k] > table[k + 1]:
                temp = table[k]
                table[k] = table[k + 1]
                table[k + 1] = temp

                temp = table2[k]
                table2[k] = table2[k + 1]
                table2[k + 1] = temp

                temp = table3[k]
                table3[k] = table3[k + 1]
                table3[k + 1] = temp

                temp = table4[k]
                table4[k] = table4[k + 1]
                table4[k + 1] = temp

def binSearch(searchTerm, table):
    min = 0
    max = len(table) - 1
    mid = int((min + max) / 2)

    while (min < max and searchTerm.lower() != table[mid].lower()):
        if searchTerm < table[mid]:
            max = mid - 1
        else:
            min = mid + 1

        mid = int((min + max) / 2)
    if searchTerm.lower() == table[mid].lower():
        return mid
    else:
        return False
    
#Print original file:
print("+========================Original File========================+")
print(f"{'TYPE':10} \t {'NAME':15} \t {'MEANING':25} \t {'ORIGIN':10}")
for i in range(0, len(name)):
    print(f"{type[i]:10} \t {name[i]:15} \t {meaning[i]:25} \t {origin[i]:10}")
print("+=============================================================+\n\n")

bubbleSort(name, type, meaning, origin)

#Print sorted file:
print("+=========================Sorted File=========================+")
print(f"{'TYPE':10} \t {'NAME':15} \t {'MEANING':25} \t {'ORIGIN':10}")
for i in range(0, len(name)):
    print(f"{type[i]:10} \t {name[i]:15} \t {meaning[i]:25} \t {origin[i]:10}")
print("+=============================================================+\n\n")

print("+========================Search========================+")

answer = "y"
while answer != "n":
    search = input("\nEnter the name of the dragon/elf you are searching for: ")
    result = binSearch(search, name)

    if result != False:
        print("----------------------------------------")
        print(f"Your dragon/elf was found at index: {result}\nHere is their data:")
        print(f"\t{type[result]} \t {name[result]} \t {meaning[result]} \t {origin[result]}")
    else:
        print("The dragon/elf you are searching for couldn't be found.")

    answer = input("Would you like to search again? [y / n] ").lower()

print("\n\nGoodbye!")