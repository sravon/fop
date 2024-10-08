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
    xpoints = np.full(
        shape=rows,
        fill_value=i,
        dtype=np.int8
    )
    ypoints = np.arange(rows)
    plt.plot(xpoints,ypoints, color="black")

# # Adding annotation
for i in range(rows+1):
    for j in range(cols):
        val = "("+ str(j)+","+str(i)+")"
        plt.annotate(val, xy=(i,j), fontsize=10)
plt.gca().invert_yaxis()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Activity 2')
plt.grid(True)

plt.show()

