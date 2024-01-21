# here are several spatial indexing methods, each with its own strengths and weaknesses. Some common spatial indexing techniques include:
# Quadtree: Hierarchical tree structure dividing space into four quadrants recursively.
# Octree: Extends the concept of quadtrees to three dimensions, dividing space into octants.
# R-tree: Hierarchical tree structure for organizing spatial objects in multidimensional space.
# KD-tree (k-dimensional tree): Binary tree structure that partitions space into half-spaces along axes.
# Grid Index: Divides space into a grid and assigns each cell an index.
# Hashing: Maps spatial objects directly to locations in a hash table.
# Spatial Hashing: Uses a hash function to map objects to grid cells.
# Hilbert Curve Indexing: Maps multidimensional data to a one-dimensional curve, preserving spatial locality.

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import gridspec
from quadtree import Point, Rectangle, QuadTree

DPI = 72

# Define Total Area or Range for Testing 
width, height = 600, 400

# Generate random points
N = 1000
xs = np.random.rand(N) * width
ys = np.random.rand(N) * height
points = [Point(xs[i], ys[i]) for i in range(N)]

# Initialise size of Main Rectangle
domain = Rectangle(Point(width/2, height/2), width/2, height/2)
capacity = 4

# Initiallise quadtree
qtree = QuadTree(domain, capacity)

# Insert each of the point in quadtree
for point in points:
    qtree.insert(point)

# Print Total Points
print('Total Points', len(qtree))

# Draw Ractangle
fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
ax = plt.subplot()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
qtree.draw(ax)

# Draw the points
ax. scatter([p.x for p in points], [p.y for p in points], s=4)
ax.set_xticks([])
ax.set_yticks([])

ax.invert_yaxis()
plt.tight_layout()
plt.savefig('/workspaces/Practice-2024/Python Practice/Quadtree/7-1-24/img/quadtree.png')
plt.show()








