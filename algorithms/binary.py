#Binary Search Algorithm:

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
        return mid
    else:
        return False

# search = input("Get search from user!")
# min = 0
# max = records - 1       #can also use len(listName) for 'records' value

# mid = int((min + max) / 2)

# #this is for INCREASING order
# while (min < max and search != listName[mid]):

#    if search < listName[mid]:
#        max = mid - 1
#    else:
#        min = mid + 1

#    guess = int((min + max) / 2)

# if search == listName[mid]:
#     print("Found")
#     #found them! use 'guess' for index of found search item
# else:
#     #boooo not found
#     print("Not found")