import matplotlib.pyplot as plt
import numpy as np

rows = int(input("Enter number of rows in grid "))
while(rows < 4 or rows > 21 ):
    print("Out of range, please re-enter... ")
    rows = input("Enter number of rows in grid... ")
    rows = int(rows)

cols = int(input("Enter number of cols in grid "))
while(cols < 4 or cols > 21 ):
    print("Out of range, please re-enter... ")
    cols = input("Enter number of cols in grid... ")
    cols = int(rows)

rows = rows+1
# Horizontal line
for i in range(rows) :
    ypoints = np.full(
        shape=rows,
        fill_value=i,
        dtype=np.int8
    )
    xpoints = np.arange(rows)
    plt.plot(xpoints,ypoints, color="red")

cols = cols+1
#Vertical line
for i in range(cols) :
    xpoints = np.full(
        shape=cols,
        fill_value=i,
        dtype=np.int8
    )
    ypoints = np.arange(cols)
    plt.plot(xpoints,ypoints, color="black")

newRows = np.array([])

for i in range(rows-1):
    newRows=np.append(newRows,[float(i)*10+0.5])

print(newRows)
        
plt.scatter(newRows,newRows, s=np.arange(1,rows))

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Activity 3')


plt.show()

