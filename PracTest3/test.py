import matplotlib.pyplot as plt

# Create a figure and an axes
fig, ax = plt.subplots()

# Draw a square box using the `plot` function
# Square vertices (corners)
x = [1, 1, 4, 4, 1]  # x-coordinates
y = [1, 4, 4, 1, 1]  # y-coordinates

# Plot the square
ax.plot(x, y, color='blue', linewidth=2)

# Set axis limits to ensure square shape
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

# Set equal scaling for both axes
ax.set_aspect('equal')

# Add grid for clarity
ax.grid(True)

# Set title and labels
plt.title('Square Box')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.show()
