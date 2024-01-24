import csv

comp_type_list = []
manu_list = []
processor_list = []
ram_list = []
hdd_1_list = []
num_hdd_list = []
hdd_2_list = []
os_list = []
year_list = []

text_file_list = []

with open("week2/hw/Lab2b/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        text_file_list.append(rec)

        # comp_type_list.append(rec[0])
        # manu_list.append(rec[1])
        # processor_list.append(rec[2])
        # ram_list.append(rec[3])
        # hdd_1_list.append(rec[4])
        # num_hdd_list.append(rec[5])

        # if rec[5] == "1":
        #     hdd_2_list.append("---")
        #     os_list.append(rec[6])
        #     year_list.append(rec[7])
        # else:
        #     hdd_2_list.append(rec[6])
        #     os_list.append(rec[7])
        #     year_list.append(rec[8])
#--------------------------------------

for rec in text_file_list:
    if rec[5] == "2":
        print(f"{rec[0]} {rec[5]} {rec[8]}")
    else:
        print(f"{rec[0]} {rec[5]} {rec[7]}")

        