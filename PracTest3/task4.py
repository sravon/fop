'''
demo2.py - starter code for Pract Test 3 Tasks 3 & 4

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
    grid = np.zeros((mshape[0]*s, mshape[1]*s))
    print(grid)
    for block in b:
        (cx_start, ry_start) = block.get_topleft()  # x,y mapping to column,row
        print(block, cx_start, ry_start)
        grid[ry_start:ry_start+s, cx_start:cx_start+s] = block.generate_image()[:, :]
    return grid

def main():
    blocksize = 20       # each block is a 20x20 square
    map_shape = (2, 3)   # 2 rows of blocks, 3 columns
    blocks = []

    # Create and populate the top row blocks with a house and three trees each
    for i in range(3):
        block = Block(blocksize, (i*blocksize, 0))
        block.add_item(House((10, 10), 8, 5))  # Example house at center
        for _ in range(3):
            x, y = random.randint(0, blocksize-5), random.randint(0, blocksize-5)
            block.add_item(Tree((x, y), random.choice([1, 2, 3]), 3))
        blocks.append(block)

    # Create and populate the bottom row blocks with trees of varying green shades
    for i in range(3):
        block = Block(blocksize, (i*blocksize, blocksize))
        for _ in range(5):
            x, y = random.randint(0, blocksize-5), random.randint(0, blocksize-5)
            block.add_item(Tree((x, y), random.choice([4, 5, 6, 7]), 3))  # Different shades of green
        blocks.append(block)

    # Plot the generated image
    grid = generate_image(blocks, blocksize, map_shape)
    plt.imshow(grid, vmin=0, vmax=10)
    plt.colorbar()

    # Draw red lines around each block
    for i in range(map_shape[1]):  # columns
        for j in range(map_shape[0]):  # rows
            top_left_x = i * blocksize
            top_left_y = j * blocksize
            plt.plot([top_left_x, top_left_x + blocksize, top_left_x + blocksize, top_left_x, top_left_x],
                     [top_left_y, top_left_y, top_left_y + blocksize, top_left_y + blocksize, top_left_y],
                     color='red', linewidth=1)

    plt.show()

if __name__ == "__main__":
    main()
