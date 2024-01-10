import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from quadtree import Point, Rectangle, QuadTree

DPI = 72  # dots per inch

# Load crime data from csv file.
df = pd.read_csv('/workspaces/Practice-2024/Python Practice/Quadtree/data/DCR1.csv', encoding='latin-1')

# Extract Latitude and Longitude columns from the dataframe.
longitude = df['Longitude']
latitude = df['Latitude']

# Create points from the latitude and longitude.
points = [Point(longitude[i], latitude[i]) for i in range(len(df))]

print('Total number of points: ', len(points))
print('First point: ', points[0].x, points[0].y)

# Quadtree setup.
width, height = 120, 120  # width and height of the rectangle.
domain = Rectangle(Point(width/2, height/2), width/2, height/2)  # center of the rectangle, half width, half height.

# Adjust the capacity parameter based on your data.
qtree = QuadTree(domain, capacity=10)

# Insert points into the quadtree.
for point in points:
    qtree.insert(point)

print('Total points in the quadtree: ', len(qtree))

# Calculate an appropriate marker size based on the number of points.
s = min(10, 1000 / np.sqrt(len(points)))

# Draw rectangle and points.
fig = plt.figure(figsize=(1000/DPI, 800/DPI), dpi=DPI)
ax = plt.subplot()
ax.set_xlim(-90, 90)
ax.set_ylim(-180, 180)
qtree.draw(ax)

# Draw points with dynamically adjusted marker size.
ax.scatter([p.x for p in points], [p.y for p in points], s=s, c='black')
ax.set_xticks([])
ax.set_yticks([])

ax.invert_yaxis()  # invert y axis to match the image coordinate system.
plt.tight_layout()  # make the plot fit the figure.
plt.savefig('/workspaces/Practice-2024/Python Practice/Quadtree/5-1-24/img/quadtree4.png', dpi=DPI)  # save the plot as a png file.
plt.show()  # display the plot.
