import numpy as np
import pandas as pd

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #### -------- Debugging ------------#### print('point Construction Initialisation __init__(self, x, y).')




class Rectangle:
    def __init__(self, center, width, height, rectangle_id=None):
        self.center = center # It contain x and y value of point
        self.width = width
        self.height = height
        self.rectangle_id = rectangle_id
        # We need four side of rectangle with respect to orignal x and y axis. 
        self.east = center.x + width
        self.west = center.x - width
        self.north = center.y - height
        self.south = center.y + height
        #### -------- Debugging ------------#### print('Rectangle Construction Initialisation __init__(self, center, width, height).')
    
    def contains_points(self, point): # Specifing that points is lies inside the current four of subrectangle, therefor checking it's location withrespect to x-axis and y-axis bondries.
        #### -------- Debugging ------------#### print('Step 2: contains_points(self, point): # Point lies in one of the current four rectangle')
        return (self.west <= point.x < self.east and 
                self.north <= point.y < self.south)

    def draw(self, ax, c='k', lw=1, **kwargs):
        #### -------- Debugging ------------#### print('Step 7: Draw function called.')
        x1, y1 = self.west, self.north
        x2, y2 = self.east, self.south
        ax.plot([x1,x2,x2,x1,x1], [y1,y1,y2,y2,y1], c=c, lw=lw , **kwargs)





class QuadTree: # It is ractangle pluse capacity

    rectangle_counter = 1  # Class-level counter for rectangle_id
    children_counter = 1  # Class-level counter for child nodes

    def __init__(self, boundary, capacity = 4, rectangle_id=None): # Set default capacity is 4. Must need to change withrespect to datasets.
        self.boundary = boundary # initialising the boundaries of Quadtree.
        self.capacity = capacity # initialising the limite of the points in each ractangle. if it will cross thresold we will create new quadtree.
        self.points = [] # Creating a list to store a points.
        self.divided = False # Boolean variable to tell us is quadtree is divided or not?
        self.children_ids = []  # List to store rectangle_id values of child nodes
        if rectangle_id is None:
            self.rectangle_id = QuadTree.rectangle_counter
            QuadTree.rectangle_counter += 1
        else:
            self.rectangle_id = rectangle_id
        # self.rectangle_id = rectangle_id  # Assign a unique identifier to the rectangle
        #### -------- Debugging ------------#### print('QuadTree Construction Initialisation __init__(self, boundary, capacity = 4)')

    def insert(self, point):
        #### -------- Debugging ------------#### print('Step 1: def insert(self, point): # Insert function is called.')
        # Check If the given point is outside the boundaries of the currrent rectangle?
        if not self.boundary.contains_points(point):
            #### -------- Debugging ------------#### print('Step A: In subtrangle Point in not lies in current subdivided rectangle but it will lies one of the four subdivided current rectanlge.')
            return False
        
        # If the quadtree has space to contain the points then let it store.
        if len(self.points) <self.capacity: 
            #### -------- Debugging ------------#### print('Step 3: len(self.points) <self.capacity:), # Checked the points capacity is grater than capacity or not?')
            self.points.append(point)
            return True
        
        # Check if quadtree is not devided then call divide function.
        if not self.divided:
            #### -------- Debugging ------------#### print('Step 4: if not self.divided: # Condition is not satisfied and point is above the capacity now need to create subtree or subrectangle.')
            self.divide() # Rectangle need to divide therefore divide() function is calling to subdivide the rectanlge.
            #### -------- Debugging ------------#### print('Subrectangle is created.')
            
        # Insert points inside Recursive quadtree function
        if self.nw.insert(point):
            #### -------- Debugging ------------#### print('Step B: self.nw.insert(point): Point added to NorthWest subdivided rectangle')
            return True
        elif self.ne.insert(point):
            #### -------- Debugging ------------#### print('Step C: self.ne.insert(point): Point added to NorthEast subdivided rectangle')
            return True
        elif self.sw.insert(point):
            #### -------- Debugging ------------#### print('Step D: self.sw.insert(point): Point added to SouthWest subdivided rectangle')
            return True
        elif self.se.insert(point):
            #### -------- Debugging ------------#### print('Step E: self.se.insert(point): Point added to SouthEast subdivided rectangle')
            return True
        
        return False
    
    # Create Recursive quadthree function
    def divide(self):
        #### -------- Debugging ------------#### print('Step 5: def divide(self): # Dividing current rectangle into subrectangle.')
        center_x = self.boundary.center.x # X axix of subdivided rectangle
        center_y = self.boundary.center.y # Y axix of subdivided rectangle
        new_width = self.boundary.width / 2 # Half width of subdivided rectangle
        new_height = self.boundary.height / 2 # Half height of subdivided rectangle

        # Initialise SubRectangle 
        self.nw = QuadTree(Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height, rectangle_id=self.rectangle_id), self.capacity)
        self.nw.rectangle_id = f"{self.rectangle_id}_nw_{QuadTree.children_counter}"
        self.children_ids.append(self.nw.rectangle_id)
        QuadTree.children_counter += 1

        self.ne = QuadTree(Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height, rectangle_id=self.rectangle_id), self.capacity)
        self.ne.rectangle_id = f"{self.rectangle_id}_ne_{QuadTree.children_counter}"
        self.children_ids.append(self.ne.rectangle_id)
        QuadTree.children_counter += 1

        self.sw = QuadTree(Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height, rectangle_id=self.rectangle_id), self.capacity)
        self.sw.rectangle_id = f"{self.rectangle_id}_sw_{QuadTree.children_counter}"
        self.children_ids.append(self.sw.rectangle_id)
        QuadTree.children_counter += 1

        self.se = QuadTree(Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height, rectangle_id=self.rectangle_id), self.capacity)
        self.se.rectangle_id = f"{self.rectangle_id}_se_{QuadTree.children_counter}"
        self.children_ids.append(self.se.rectangle_id)
        QuadTree.children_counter += 1

        # # IMPORTANT TO DEBUG AND EVALUATE THE QUADTREE STRUCTURE. SHOULD KEEP IT.
        # # Here we are printing that current node is dividing.
        # print(f"Dividing node {self.rectangle_id} into:")
        # # Print the width and height of current node before it is divided. Means providing the size of the orignal rectangle that is being subdivided.
        # print(f"Width and Height: {round(self.boundary.width, 2)}, {round(self.boundary.height, 2)} | ID: {self.rectangle_id}")
        # # Printing the center coordinates of each of the four child nodes. 
        # print(f"NW: {round(self.nw.boundary.center.x, 2)}, {round(self.nw.boundary.center.y, 2)} | SUBDIVIDE PARENT ID: {self.nw.rectangle_id}")
        # print(f"NE: {round(self.ne.boundary.center.x, 2)}, {round(self.ne.boundary.center.y, 2)} | SUBDIVIDE PARENT ID: {self.ne.rectangle_id}")
        # print(f"SW: {round(self.sw.boundary.center.x, 2)}, {round(self.sw.boundary.center.y, 2)} | SUBDIVIDE PARENT ID: {self.sw.rectangle_id}")
        # print(f"SE: {round(self.se.boundary.center.x, 2)}, {round(self.se.boundary.center.y, 2)} | SUBDIVIDE PARENT ID: {self.se.rectangle_id}")        
        # print("------------------ Each Subdivision is End ------------------")

        self.divided = True


    # Calculate how many points are in quadtree including subtree
    def __len__(self):
        #### -------- Debugging ------------#### print('Step 6: def __len__(self): # Calculating  Total Numbers of Points in Quadtree.')
        count = len(self.points)
        if self.divided:
            count += len(self.nw) + len(self.ne) + len(self.sw) + len(self.se)
        return count
            
    # To draw recursively draw quadtree we have created draw function.
    def draw(self, ax):
        self.boundary.draw(ax)

        if self.divided:
            self.nw.draw(ax)
            self.ne.draw(ax)
            self.sw.draw(ax)
            self.se.draw(ax)
        #### -------- Debugging ------------#### print('def draw(self, ax):')
    #     print(f"Node {self.rectangle_id}:")
    #     print(f"Center: {round(self.boundary.center.x, 2)}, {round(self.boundary.center.y, 2)} | Width and Height: {round(self.boundary.width, 2)}, {round(self.boundary.height, 2)}")
    #     print(f"Child IDs: {self.children_ids}")
    #     print("-----")

    # def recursive_print(self):
    #     print(f"Node {self.rectangle_id}:")
    #     print(f"Center: {round(self.boundary.center.x, 2)}, {round(self.boundary.center.y, 2)} | Width and Height: {round(self.boundary.width, 2)}, {round(self.boundary.height, 2)}")
    #     print(f"Child IDs: {self.children_ids}")
    #     print("-----")

    #     if self.divided:
    #         self.nw.recursive_print()
    #         self.ne.recursive_print()
    #         self.sw.recursive_print()
    #         self.se.recursive_print()
    
    def recursive_collect_tree_datastruc(self, data=None):
        if data is None:
            data = []

        node_info = {
            "Node ID": self.rectangle_id,
            "Center X": round(self.boundary.center.x, 2),
            "Center Y": round(self.boundary.center.y, 2),
            "Width": round(self.boundary.width, 2),
            "Height": round(self.boundary.height, 2),
            "Child IDs": self.children_ids
        }
        data.append(node_info)

        if self.divided:
            self.nw.recursive_collect_tree_datastruc(data)
            self.ne.recursive_collect_tree_datastruc(data)
            self.sw.recursive_collect_tree_datastruc(data)
            self.se.recursive_collect_tree_datastruc(data)

        return data

    def save_to_csv(self, filename):
        data = self.recursive_collect_tree_datastruc()
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

###### ------------------------- ########## New changes to store points into new dataframes.
    
    def organize_data_points(self):
        # Calling the recursive helper function to organize data points
        root_df = self._recursive_organize_data_points(self)
        root_df.to_csv('/workspaces/Practice-2024/Python Practice/Quadtree/19-1-24/data/quadtree_new_data.csv', index=False)
    
    def _recursive_organize_data_points(self, quadtree_node=None, current_df=None):
        if quadtree_node is None:
            quadtree_node = self  # Set the default value for quadtree_node

        # If quadtree is not divided not even single time (root).
        if not quadtree_node.divided:
            # Leaf node, store data points in the current data frame
            if current_df is None:
                current_df = pd.DataFrame(quadtree_node.points, columns=['Latitude', 'Longitude'])
                current_df['rectangle_id'] = quadtree_node.rectangle_id
            else:
                points_df = pd.DataFrame([(point.x, point.y, quadtree_node.rectangle_id) for point in quadtree_node.points], columns=['Latitude', 'Longitude', 'rectangle_id'])
                points_df['rectangle_id'] = quadtree_node.rectangle_id
                if current_df is None:
                    current_df = points_df.copy()
                else:
                    current_df = current_df._append(points_df, ignore_index=True, sort=False)
        # If quadtree is dividedd
        elif quadtree_node.divided:
            # Subdivide and organize data points for each sub-rectangle
            for sub_rectangle in [quadtree_node.nw, quadtree_node.ne, quadtree_node.sw, quadtree_node.se]:
                sub_df_name = f'df{QuadTree.children_counter}_rect{quadtree_node.rectangle_id}'
                sub_df = pd.DataFrame(columns=['Latitude', 'Longitude', 'rectangle_id'])
                sub_df = self._recursive_organize_data_points(sub_rectangle, sub_df)
                if current_df is None:
                    current_df = sub_df.copy()
                else:
                    current_df = current_df._append(sub_df, ignore_index=True, sort=False)
                QuadTree.children_counter += 1
        return current_df





