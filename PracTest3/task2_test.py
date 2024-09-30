import random
import numpy as np
import matplotlib.pyplot as plt
from canopy import Tree

def add_green_frame(grid, frame_width=2):
    """ Add a green frame to the grid. """
    grid[:frame_width, :] = 20  # top frame
    grid[-frame_width:, :] = 20  # bottom frame
    grid[:, :frame_width] = 20  # left frame
    grid[:, -frame_width:] = 20  # right frame
    return grid

def main():
    xlim = 60
    ylim = 80
    grid = np.zeros((ylim, xlim))
    
    # Add green frame to the grid
    grid = add_green_frame(grid)
    grid[0, 0] = 10  # For color stretch (as per instructions)
    
    listsX = [random.randint(20, xlim-20) for _ in range(20)]
    listsY = [random.randint(20, ylim-20) for _ in range(20)]
    
    sumX = sum(listsX) / len(listsX)
    sumY = sum(listsY) / len(listsY)

    t_red = Tree((listsX, listsY), "r", 10)  # Red trees for first subplot

    # Create second tree object for green trees, twice the size of the original
    t_green = Tree((listsX, listsY), "g", 20)  # Green trees for second subplot

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # Two subplots side by side

    # Plot for first subplot
    im1 = ax1.imshow(grid)  # Save the image handle for colorbar
    plt.colorbar(im1, ax=ax1)  # Associate the colorbar with the first subplot
    ax1.scatter(t_red.get_coord()[0], t_red.get_coord()[1], c=t_red.get_colour(), s=t_red.get_size())
    ax1.set_xlim(0, xlim)
    ax1.set_ylim(0, ylim)
    ax1.set_aspect('equal')
    ax1.set_title("Red Trees with Green Frame")  # Title for the first subplot

    # Plot for second subplot with green trees
    im2 = ax2.imshow(grid, cmap="hot")  # Hot colormap for second subplot
    plt.colorbar(im2, ax=ax2)  # Associate the colorbar with the second subplot
    ax2.scatter(t_green.get_coord()[0], t_green.get_coord()[1], c=t_green.get_colour(), s=t_green.get_size())
    ax2.set_xlim(0, xlim)
    ax2.set_ylim(0, ylim)
    ax2.set_aspect('equal')
    ax2.set_title("Green Trees (Twice Size) with Hot Colormap")  # Title for the second subplot

    # Add a higher level title
    fig.suptitle("Comparison of Red and Green Trees with Modified Grid and Colormap", fontsize=16)

    # Save the figure
    fig.savefig("task2.png")
    plt.show()

if __name__ == "__main__":
    main()
