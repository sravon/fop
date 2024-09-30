'''
task2.py - two tree plot

Student Name: Abdur Rahman Kazi
Student ID  : 22402293

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
from canopy import *

def overlay(g, item):
    coords = item.get_topleft()
    size = item.get_size()
    print(coords, size)
    print(f"g[{coords[0]}:{coords[0]}+{size},{coords[1]}:{coords[1]}+{size}] = ({size},{size})")
    g[coords[0]:coords[0]+size,coords[1]:coords[1]+size] = item.get_image()[:,:]


def main():
    xlim = 60
    ylim = 80
    grid = np.zeros((ylim,xlim))
    
    # to draw the border - Vertical
    grid[0,0] = 10                # updated 30/9
    for i in range(10,ylim-9):
        grid[i,10] = 8
        tmp = xlim-10
        grid[i,tmp] = 8

    # to draw the border - Horizontal
    for i in range(10,xlim-9):
        grid[10,i] = 8
        tmp = ylim-10
        grid[tmp,i] = 8

    #t = Tree((20, 30), "r", 100)  # updated 11/9
    treeplot1 = []
    treeplot2 = []

    for i in range(20):
        xval = random.randint(20,xlim-20)
        yval = random.randint(20,ylim-20)
        t = Tree((xval,yval), "r", 50)
        treeplot1.append(t)  
        t = Tree((xval,yval), "g", 100)
        treeplot2.append(t)  
        print(t)
    
    plt.figure(1)
    plt.subplot(121)
    plt.imshow(grid)
    # To adjust colorbar height
    plt.colorbar(shrink=0.65)                # updated 11/9

    for t in treeplot1:
        plt.scatter(t.get_coord()[0], t.get_coord()[1], c=t.get_colour(), s=t.get_size())
    plt.title("Task 1: Random Red Trees")
    plt.subplot(122)
    plt.imshow(grid,cmap="hot")
    plt.colorbar(shrink=0.65)                # updated 11/9
    
    for t in treeplot2:
        plt.scatter(t.get_coord()[0], t.get_coord()[1], c=t.get_colour(), s=t.get_size())
    plt.title("Task 2: Random Green Trees")
    plt.suptitle("TWO TREE PLOTS")
    
    # save the plot as an image
    plt.savefig("task2.png")

    plt.show()

if __name__ == "__main__":
    main()
