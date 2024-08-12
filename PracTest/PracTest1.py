rows = int(input("Enter number of rows in grid... "))
while(rows <= 0):
    print("Out of range, please re-enter... ")
    rows = int(input("Enter number of rows in grid... "))

cols = int(input("Enter number of cols in grid... "))
while(cols <= 0):
    print("Out of range, please re-enter... ")
    cols = int(input("Enter number of cols in grid... "))

for row in range(rows*2+1):
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