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

colors = [ 'blue', 'green', 'cyan'] 
sizes = [20, 50, 80, 100] 
for i in range(rows-1):
    color = colors[i % len(colors)]
    size = sizes[i % len(sizes)] 
    for j in range(cols-1):
        plt.scatter(float(i)+ 0.5,float(j)+ 0.5, c=color, s=size)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Activity 4')
plt.grid(True)

plt.show()

