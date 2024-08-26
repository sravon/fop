
rows = input("Enter number of rows in grid ")
rows = int(rows)
while(rows <= 0):
    print("Out of range, please re-enter... ")
    rows = input("Enter number of rows in grid... ")
    rows = int(rows)

cols = input("Enter number of cols in grid ")
cols = int(cols)
while(cols <= 0):
    print("Out of range, please re-enter... ")
    cols = input("Enter number of cols in grid... ")
    cols = int(cols)

totalNumberOfROws = rows*2+1

for row in range(totalNumberOfROws):
    if row%2 == 0:
        for col in range(cols):
            end= "+" if col == (cols-1) else ""
            print("+---", end=end)
        print("")
    else:
        for col in range(cols):
            end= "|" if col == (cols-1) else ""
            print("|   ", end=end)
        print("")


rowNumber = input("Enter a row number... ")
rowNumber = int(rowNumber)
while(rowNumber > rows):
    print("Out of range, please re-enter... ")
    rowNumber = int(input("Enter a row number... "))
    rowNumber = int(rowNumber)

colNumber = input("Enter a col number ... ")
colNumber = int(rowNumber)
while(colNumber > cols):
    print("Out of range, please re-enter... ")
    colNumber = input("Enter a col number... ")
    colNumber = int(colNumber)

for row in range(totalNumberOfROws):
    if row%2 == 0:
        for col in range(cols):
            end= "+" if col == (cols-1) else ""
            print("+---", end=end)
        print("")
    else:
        for col in range(cols):
            end= "|" if col == (cols-1) else ""
            if (row == rowNumber*2-1) and (col == colNumber-1):
                print("| X ", end=end)
            else:
                print("|   ", end=end)
        print("")