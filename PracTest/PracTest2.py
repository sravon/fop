import math

# def func(totalRows,cols, rowNum=0, colNum=0):
#     for row in range(totalRows):
#         if row%2 == 0:
#             for col in range(cols):
#                 end= "+" if col == (cols-1) else ""
#                 print("+---", end=end)
#             print("")
#         else:
#             for col in range(cols):
#                 end= "|" if col == (cols-1) else ""
#                 if (row == rowNum*2-1) and (col == colNum-1):
#                     print("| X ", end=end)
#                 else:
#                     print("|   ", end=end)
#             print("")

rows = int(input("Enter number of rows in grid... "))
while(rows <= 0 or rows > 21):
    print("Out of range, please re-enter... ")
    rows = int(input("Enter number of rows in grid... "))

cols = int(input("Enter number of cols in grid... "))
while(cols <= 0 or rows > 21):
    print("Out of range, please re-enter... ")
    cols = int(input("Enter number of cols in grid... "))
totalRows = rows*2+1

rowNum=0
colNum=0
for row in range(totalRows):
    if row%2 == 0:
        for col in range(cols):
            end= "+" if col == (cols-1) else ""
            print("+---", end=end)
        print("")
    else:
        for col in range(cols):
            end= "|" if col == (cols-1) else ""
            if (row == rowNum*2-1) and (col == colNum-1):
                print("| X ", end=end)
            else:
                print("|   ", end=end)
        print("")

# Part 2
rowNum = int(input("Enter a row number... "))
while(rowNum > rows):
    print("Out of range, please re-enter... ")
    rowNum = int(input("Enter a row number... "))

colNum = int(input("Enter a col number ... "))
while(colNum > cols):
    print("Out of range, please re-enter... ")
    colNum = int(input("Enter a col number... "))

for row in range(totalRows):
    if row%2 == 0:
        for col in range(cols):
            end= "+" if col == (cols-1) else ""
            print("+---", end=end)
        print("")
    else:
        for col in range(cols):
            end= "|" if col == (cols-1) else ""
            if (row == rowNum*2-1) and (col == colNum-1):
                print("| X ", end=end)
            else:
                print("|   ", end=end)
        print("")