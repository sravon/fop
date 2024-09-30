'''
demo1.py - demonstration code to start Prac Test 3, Tasks 1 & 2

Student Name: 
Student ID  :

Version History:
 - 9/9/24 - original version
 - 11/9/24 - updated as follows: (use ":set number" to show line numbers) 
       line 30 - sets a value in the grid to 10 - stretching the colours
       line 31 - "b" for colour in Tree creation (not numeric on scatter)
       line 33 - swapped xlim/ylim
       line 37 - moved plt.colorbar() to immediately after plt.imshow()
'''
import random
import numpy as np
import matplotlib.pyplot as plt
from canopy import Tree

# def overlay(g, item):
#     coords = item.get_topleft()
#     size = item.get_size()
#     print(coords, size)
#     print(f"g[{coords[0]}:{coords[0]}+{size},{coords[1]}:{coords[1]}+{size}] = ({size},{size})")
#     g[coords[0]:coords[0]+size,coords[1]:coords[1]+size] = item.get_image()[:,:]


def main():
    xlim = 60
    ylim = 80
    grid = np.zeros((ylim,xlim))
    
    grid[0,0] = 10      

    listsX = []
    listsY = []
    
    for i in range(20):
        listsX.append(random.randint(20, xlim-20))
        listsY.append(random.randint(20, xlim-20))
    sumX = sum([num for num in listsX])/len(listsX)
    sumY = sum([num for num in listsY])/len(listsY)
    print(sumX)
    t = Tree((listsX,listsY), "r", 10)
    fig, ax = plt.subplots()
    # Xcenter - (size/2)
    x = [ sumX - (10*2), sumX - (10*2), sumX + (10*2),sumX + (10*2),sumX - (10*2) ]
    y = [sumY - (10*2), sumY + (10*2), sumY + (10*2), sumY - (10*2), sumY - (10*2)]
    ax.plot(x, y, color='green', linewidth=2)
    ax.set_xlim(0, xlim)
    ax.set_ylim(0, ylim)
    ax.set_aspect('equal')
    
    plt.imshow(grid)
    plt.colorbar()                # updated 11/9
    plt.scatter(t.get_coord()[0], t.get_coord()[1], c=t.get_colour(), s=t.get_size())
    
    fig = plt.gcf()  # Get the current figure
    fig.savefig("task2.png")
    plt.show()

if __name__ == "__main__":
    main()
