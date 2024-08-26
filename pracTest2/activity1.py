import matplotlib.pyplot as plt
import numpy as np

#start horizontal Line


# Vertical line
for i in range(9) :
    xpoints = np.array([i,i,i,i,i,i,i,i,i])
    ypoints = np.array([0,1,2,3,4,5,6,7,8])
    plt.plot(xpoints,ypoints, color="black")

# Horizontal line
for i in range(9) :
    xpoints = np.array([0,1,2,3,4,5,6,7,8])
    ypoints = np.array([i,i,i,i,i,i,i,i,i])
    plt.plot(xpoints,ypoints, color="red")

# Adding annotation
plt.annotate('(1, 1)', xy=(1,1), fontsize=10)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Activity 1')


plt.show()

