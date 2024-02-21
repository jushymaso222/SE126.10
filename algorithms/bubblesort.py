#BUBBLE SORT----------------------------------------

def bubbleSort(table):
    for i in range(0, len(table) - 1):
        for k in range(0, len(table) - 1):
            if table[k] > table[k + 1]:
                temp = table[k]
                table[k] = table[k + 1]
                table[k + 1] = temp

#Added a function here for easy implementation to other projects

# for i in range(0, number_of_elements - 1):#outter loop
#     print("OUTER LOOP! i = ", i)

#     for index in range(0, number_of_elements - 1):#inner loop

#         print("\t INNER LOOP! k = ", index)
#         #below if statement determines the sort
#         #list used is the list being sorted
#         # > is for increasing order, < for decreasing

#         if(name[index] > name[index + 1]):
#             print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

#             #if above is true, swap places!
#             temp = name[index]
#             name[index] = name[index + 1]
#             name[index + 1] = temp

 
#             #swap all other values
#             # temp = age[index]
#             # age[index] = age[index + 1]
#             # age[index + 1] = temp
