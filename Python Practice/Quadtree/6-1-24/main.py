import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from quadtree import Point, Rectangle, QuadTree

# Step 1: Load crime data from csv file.
df = pd.read_csv('/workspaces/Practice-2024/Python Practice/Quadtree/data/DCR1.csv', encoding='latin-1')

# Step 2: Extract Latitude and Longitude columns from the dataframe.
latitude = df['Latitude']
longitude = df['Longitude']

# Step 3: Convert latitude and longitude to Cartesian coordinates
# I have used StandardScaler to normalize the coordinates.
scaler = StandardScaler()
df[['X', 'Y']] = scaler.fit_transform(df[['Latitude', 'Longitude']])

print(df.head())

# Step 4: Create quadtree and insert points into the quadtree.
# We will select appropriate width and height based on the data.
width, height = 2, 2    # width and height of the rectangle.
domain = Rectangle(Point(width/2, height/2), width/2, height/2)   # center of the rectangle, half width, half height.
qtree = QuadTree(domain, 10)    # create or initialise a quadtree with the rectangle and capacity of 4.

# Insert points into the quadtree.
points = [Point(row['X'], row['Y']) for _, row in df.iterrows()]
for point in points:
    qtree.insert(point)

# Step 5: Visuaalize the quadtree and crime data
# Draw rectangle.
fig, ax = plt.subplots(figsize=(10,8))
ax.set_xlim(-3, 2.5)
ax.set_ylim(-3, 2.5)

# Draw quadtree.
qtree.draw(ax)

# Draw  crime data points.
ax.scatter(df['X'], df['Y'], s=1, c='black', label= 'Crime Data')

ax.set_xticks([])
ax.set_yticks([])

ax.invert_yaxis()
plt.legend()
plt.savefig('/workspaces/Practice-2024/Python Practice/Quadtree/6-1-24/img/quadtree3.png')  # save the plot as a png file.
plt.show()



