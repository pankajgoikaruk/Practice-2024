import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from quadtree import Point, Rectangle, QuadTree

DPI = 72    # dots per inch

# Load crime data from csv file.
df = pd.read_csv('/workspaces/Practice-2024/Python Practice/Quadtree/5-1-24/data/DCR1.csv', encoding='latin-1')

df = df.head(10)

print(df.head())    # print the first 5 rows of the dataframe.
print(df.shape)     # print the shape of the dataframe.
print(df.columns)   # print the columns of the dataframe.

# Extract Latitude and Longitude columns from the dataframe.
longitude = df['Longitude']
latitude = df['Latitude']

# Find the min and max of the longitude and latitude.
min_longitude, max_longitude = longitude.min(), longitude.max()
min_latitude, max_latitude = latitude.min(), latitude.max()

# Plot the points directly on the map
plt.scatter(longitude, latitude, s=1)  # Adjust the size based on your preference
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Data Map')
plt.xlim(min_longitude, max_longitude)
plt.ylim(min_latitude, max_latitude)
plt.savefig('/workspaces/Practice-2024/Python Practice/Quadtree/5-1-24/img/crime_data_map.png', dpi=DPI)
plt.show()

print(df[['Longitude', 'Latitude']].head())    # print the first 5 rows of the dataframe with only the Longitude and Latitude columns.

# Create points from the latitude and longitude.
points = [Point(longitude[i], latitude[i]) for i in range(len(df))]

print('Total number of points: ', len(points))
print('First point: ', points[0].x, points[0].y)

# Quadtree setup.
width, height = 180, 90    # width and height of the rectangle.
domain = Rectangle(Point(width/2, height/2), width/2, height/2)   # center of the rectangle, half width, half height.

# Adjusting the capacity parameter based on my data.
qtree = QuadTree(domain, 10)    # create or initialise a quadtree with the rectangle and capacity of 4.

# Insert points into the quadtree.
for i, point in enumerate(points):
    qtree.insert(point)
    print(f'Point {i} is out of boundary: {point.x}, {point.y}')

print('Total points in the quadtree: ', len(qtree))

# Calculate an appropriate marker size based on the number of points.
s = min(10, 1000 / np.sqrt(len(points)))

# Draw rectangle and points.
fig = plt.figure(figsize=(1000/DPI, 800/DPI), dpi=DPI)
ax = plt.subplot()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
qtree.draw(ax)

# Draw points.
ax.scatter([p.x for p in points], [p.y for p in points], s=s, c='black')
ax.set_xticks([])
ax.set_yticks([])

ax.invert_yaxis()   # invert y axis to match the image coordinate system.
plt.tight_layout()  # make the plot fit the figure.
plt.savefig('/workspaces/Practice-2024/Python Practice/Quadtree/5-1-24/img/quadtree1.png', dpi=DPI)  # save the plot as a png file.
plt.show() # display the plot.