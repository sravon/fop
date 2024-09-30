'''
task4.py - (2,3) grid of block with houses and trees

Student Name: 
Student ID  : 

Version History:
    - 11/9/24 - original version released
'''
import random
import numpy as np
import matplotlib.pyplot as plt

from canopy import *

def generate_image(b, s, mshape):
    # Initialize the grid with the correct shape based on map_shape and blocksize
    grid = np.zeros((mshape[0] * s, mshape[1] * s))
    
    for block in b:
        (cx_start, ry_start) = block.get_topleft()  # x,y mapping to column,row
        
        # Generate the image for the current block
        block_image = block.generate_image()
        
        # Check if block_image is not empty
        if block_image.size == 0:
            print("Warning: Block image is empty, skipping this block.")
            continue
        
        # Ensure the block image has the correct shape before assignment
        if block_image.shape[0] == s and block_image.shape[1] == s:
            grid[ry_start:ry_start+s, cx_start:cx_start+s] = block_image
        else:
            print(f"Warning: Block image shape {block_image.shape} does not match expected shape {(s, s)}")
    return grid

def main():
    # Setup for the assignment
    blocksize = 20       # each block is a 20x20 square
    map_shape = (2, 3)   # 2 rows of blocks, 3 columns
    blocks = []

    finalblock = blocksize * 2
    blocks.append(Block(blocksize, (0, 0)))
    blocks.append(Block(blocksize, (blocksize, 0)))
    blocks.append(Block(blocksize, (finalblock, 0)))

    blocks.append(Block(blocksize, (0, blocksize)))
    blocks.append(Block(blocksize, (blocksize, blocksize)))
    blocks.append(Block(blocksize, (finalblock, blocksize)))

    hcolor = 7
    # Top row
    for i in range(3): 
        hcolor += i
        blocks[i].add_item(Tree((5, 15), 3, 3))
        blocks[i].add_item(Tree((3, 3), 3, 3))
        blocks[i].add_item(Tree((12, 6), 5, 4))
        # Adjusted line to match the expected number of arguments in House constructor
        blocks[i].add_item(House((13, 13), hcolor, 10))  # Adjusted line

    # Second row
    for i in range(3, 6):
        numtree = random.choice(range(1, 7))
        for j in range(numtree):
            colortree = random.choice(range(2, 7))
            treesize = random.choice(range(1, 5))
            treex = random.choice(range(0, 18))
            treey = random.choice(range(0, 18))
            blocks[i].add_item(Tree((treex, treey), colortree, treesize))

    # Generate the final image and show it
    image = generate_image(blocks, blocksize, map_shape)
    plt.imshow(image, vmin=0, vmax=10)
    plt.colorbar()

    # Print red vertical and horizontal lines
    plt.plot((20, 20), (0, 39), "r")
    plt.plot((40, 40), (0, 39), "r")
    plt.plot((0, 0), (39, 0), "r")
    plt.plot((0, 59), (0, 0), "r")
    plt.plot((0, 59), (20, 20), "r")

    plt.title("Task 4 : (2,3) grid of Block with Houses and Trees")
    plt.show()

if __name__ == "__main__":
    main()

