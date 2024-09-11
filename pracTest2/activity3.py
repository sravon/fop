import matplotlib.pyplot as plt
import numpy as np
import random

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

colors = [random.random(), random.random(), random.random()]
rows = rows+1
cols = cols+1

# Horizontal line
for i in range(rows) :
    ypoints = np.full(
        shape=cols,
        fill_value=i,
        dtype=np.int8
    )
    xpoints = np.arange(cols)
    plt.plot(xpoints,ypoints, color="red")

#Vertical line
for i in range(cols) :
    col_color = [random.random(), random.random(), random.random()]
    xpoints = np.full(
        shape=rows,
        fill_value=i,
        dtype=np.int8
    )
    ypoints = np.arange(rows)
    plt.plot(xpoints,ypoints, color=col_color)
    for k in range(1, rows):
        if(i != cols-1) :
            plt.scatter(i + 0.5, k - 0.5, color=col_color)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Activity 3')
plt.grid(True)

plt.show()

