
'''
Last Code Update Date: 20/01/2024
Code Updated By: Pankaj Dilip Goikar
Updated Topics:

1. Added a function print_statistics() to display the points in each reactangle.
2. 

Last Code Update Date: 19/01/2024
Code Updated By: Pankaj Dilip Goikar
Updated Topics: 

1. Removed data points' lables.
2. Replace file name test.py to main.py.
3. Specified local variable for path to store data and quadtree images.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import gridspec
from sklearn.preprocessing import StandardScaler
from quadtree import Point, Rectangle, QuadTree

# Local Variables
img_path = '/workspaces/Practice-2024/Python Practice/Quadtree/20-1-24/img/'
quadree_sturcture_csv = '/workspaces/Practice-2024/Python Practice/Quadtree/20-1-24/data/'

# Step 1: Load crime data from csv file.
data = pd.read_csv('/workspaces/Practice-2024/Python Practice/Quadtree/data/DCR1.csv', encoding='latin-1')

df = data[['CMPLNT_FR_DT','CMPLNT_FR_TM','Latitude','Longitude']].head(40)
# print(df.info())
# print('Null vlaues is',df.isnull().sum())

DPI = 100
capacity = 5

# Step 2: Extract Latitude and Longitude columns from the dataframe.
longitude = df['Longitude']
latitude = df['Latitude']

# Step 3: Convert latitude and longitude to Cartesian coordinates
# I have used StandardScaler to normalize the coordinates.
scaler = StandardScaler()
df[['X', 'Y']] = scaler.fit_transform(df[['Latitude', 'Longitude']])

# Step 4: Create quadtree and insert points into the quadtree.
# We will select appropriate width and height based on the data.
width, height = 5, 5   # width and height of the main rectangle.
domain = Rectangle(Point(0, 0), width/1.5, height/1.5, rectangle_id=1)   # center of the rectangle, half width, half height. domain = Rectangle(Point(-0.5, -0.5), width/1.7, height/1.8)
#capacity = 10
qtree = QuadTree(domain, capacity, rectangle_id=1)    # create or initialise a quadtree with the rectangle and capacity of 4.

# Insert points into the quadtree.
points = [Point(row['X'], row['Y']) for _, row in df.iterrows()]
rectangle_association = {}  # Dictionary to store the association between points and rectangles

for point in points:
    if qtree.insert(point):
        rectangle_association[point] = qtree.rectangle_id

        
# # Create separate data frames for leaf rectangles
# leaf_rectangles_data_frames = qtree.create_data_frames_for_leaf_rectangles()

# # Display the leaf rectangles' data frames
# for df_name, df in leaf_rectangles_data_frames.items():
#     print(f"\nData Frame: {df_name}")
#     print(df)




# # Call recursive print
# qtree.save_to_csv(quadree_sturcture_csv + 'quadtree_info.csv')


# Print the total number of rectangles created
print('Total Number of Rectangles:------>', QuadTree.rectangle_counter)

# Print Total Points
print('Total Points Quadtree Contains:------>', len(qtree))

# Draw Ractangle
fig = plt.figure(figsize=(800/DPI, 600/DPI), dpi=DPI)
ax = plt.subplot()
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
qtree.draw(ax)

# Draw the points with labels
# Draw the points
ax. scatter([p.x for p in points], [p.y for p in points], s=4)
ax.set_xticks([])
ax.set_yticks([])

ax.invert_yaxis()
plt.tight_layout()
plt.savefig(img_path + 'quadtree.png')
plt.show()








