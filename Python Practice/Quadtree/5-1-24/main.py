import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import gridspec
from quadtree import Point, Rectangle, QuadTree

DPI = 72

width, height = 600, 400

N = 500
xs = np.random.rand(N) * width
ys = np.random.rand(N) * height
points = [Point(xs[i], ys[i]) for i in range(N)]

domain = Rectangle(Point(width/2, height/2), width/2, height/2)
qtree = QuadTree(domain, 4)

for point in points:
    qtree.insert(point)

print('Total points in the quadtree: ', len(qtree))

# Draw rectangle.
fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
ax = plt.subplot()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
qtree.draw(ax)

# Draw points.
ax.scatter([p.x for p in points], [p.y for p in points], s=4, c='black')
ax.set_xticks([])
ax.set_yticks([])

ax.invert_yaxis()
plt.tight_layout()
plt.savefig('/workspaces/Practice-2024/Python Practice/Quadtree/5-1-24/img/quadtree.png', dpi=DPI)
plt.show()