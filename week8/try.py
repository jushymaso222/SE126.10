def rowChoice():
    row_r = -1
    try:
        row_r = int(input("Input a value: "))
    except:
        print("ERROR")
        row_r = -1

    if row_r != -1:
        return row_r
    else:
        return rowChoice()
        

row = rowChoice()
print(f"Row: {row}")