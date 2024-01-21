import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('point Construction Initialisation __init__(self, x, y).')

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
        print('Rectangle Construction Initialisation __init__(self, center, width, height).')
    
    def contains_points(self, point): # Specifing that points is lies inside the current four of subrectangle, therefor checking it's location withrespect to x-axis and y-axis bondries.
        print('Step 2: contains_points(self, point): # Point lies in one of the current four rectangle')
        return (self.west <= point.x < self.east and 
                self.north <= point.y < self.south)

    def draw(self, ax, c='k', lw=1, **kwargs):
        print('Step 7: Draw function called.')
        x1, y1 = self.west, self.north
        x2, y2 = self.east, self.south
        ax.plot([x1,x2,x2,x1,x1], [y1,y1,y2,y2,y1], c=c, lw=lw , **kwargs)

class QuadTree: # It is ractangle pluse capacity

    rectangle_counter = 1  # Class-level counter for rectangle_id

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
        print('QuadTree Construction Initialisation __init__(self, boundary, capacity = 4)')

    def insert(self, point):
        print('Step 1: def insert(self, point): # Insert function is called.')
        # Check If the given point is outside the boundaries of the currrent rectangle?
        if not self.boundary.contains_points(point):
            print('Step A: In subtrangle Point in not lies in current subdivided rectangle but it will lies one of the four subdivided current rectanlge.')
            return False
        
        # If the quadtree has space to contain the points then let it store.
        if len(self.points) <self.capacity: 
            print('Step 3: len(self.points) <self.capacity:), # Checked the points capacity is grater than capacity or not?')
            self.points.append(point)            
            return True
        
        # Check if quadtree is not devided then call divide function.
        if not self.divided:
            print('Step 4: if not self.divided: # Condition is not satisfied and point is above the capacity now need to create subtree or subrectangle.')
            self.divide() # Rectangle need to divide therefore divide() function is calling to subdivide the rectanlge.
            print('Subrectangle is created.')
            
        # Insert points inside Recursive quadtree function
        if self.nw.insert(point):
            print('Step B: self.nw.insert(point): Point added to NorthWest subdivided rectangle')
            return True
        elif self.ne.insert(point):
            print('Step C: self.ne.insert(point): Point added to NorthEast subdivided rectangle')
            return True
        elif self.sw.insert(point):
            print('Step D: self.sw.insert(point): Point added to SouthWest subdivided rectangle')
            return True
        elif self.se.insert(point):
            print('Step E: self.se.insert(point): Point added to SouthEast subdivided rectangle')
            return True
        
        return False
    
    # Create Recursive quadthree function
    def divide(self):
        print('Step 5: def divide(self): # Dividing current rectangle into subrectangle.')
        center_x = self.boundary.center.x # X axix of subdivided rectangle
        center_y = self.boundary.center.y # Y axix of subdivided rectangle
        new_width = self.boundary.width / 2 # Half width of subdivided rectangle
        new_height = self.boundary.height / 2 # Half height of subdivided rectangle

        # Initialise SubRectangle 
        # nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height, rectangle_id=self.rectangle_id) # North West Side
        # self.nw = QuadTree(nw, self.capacity, rectangle_id=self.rectangle_id)

        # ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height, rectangle_id=self.rectangle_id) # North East Side
        # self.ne  = QuadTree(ne, self.capacity, rectangle_id=self.rectangle_id)

        # sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height, rectangle_id=self.rectangle_id) # South West Side
        # self.sw = QuadTree(sw, self.capacity, rectangle_id=self.rectangle_id)

        # se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height, rectangle_id=self.rectangle_id) # South East Side
        # self.se = QuadTree(se, self.capacity, rectangle_id=self.rectangle_id)

        # Use the parent's rectangle_id as a prefix for child node identifiers
        
        # Use the parent's rectangle_id as a prefix for child node identifiers
        self.nw = QuadTree(Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height, rectangle_id=self.rectangle_id), self.capacity)
        self.nw.rectangle_id = f"{self.rectangle_id}_nw"
        self.children_ids.append(self.nw.rectangle_id)

        self.ne = QuadTree(Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height, rectangle_id=self.rectangle_id), self.capacity)
        self.ne.rectangle_id = f"{self.rectangle_id}_ne"
        self.children_ids.append(self.ne.rectangle_id)

        self.sw = QuadTree(Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height, rectangle_id=self.rectangle_id), self.capacity)
        self.sw.rectangle_id = f"{self.rectangle_id}_sw"
        self.children_ids.append(self.sw.rectangle_id)

        self.se = QuadTree(Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height, rectangle_id=self.rectangle_id), self.capacity)
        self.se.rectangle_id = f"{self.rectangle_id}_se"
        self.children_ids.append(self.se.rectangle_id)

        self.divided = True

        # Increment the rectangle_counter for each child rectangle created during subdivision
        self.nw.rectangle_id = QuadTree.rectangle_counter
        #QuadTree.rectangle_counter += 1

        self.ne.rectangle_id = QuadTree.rectangle_counter
        #QuadTree.rectangle_counter += 1

        self.sw.rectangle_id = QuadTree.rectangle_counter
        #QuadTree.rectangle_counter += 1

        self.se.rectangle_id = QuadTree.rectangle_counter
        #QuadTree.rectangle_counter += 1

    # Calculate how many points are in quadtree including subtree
    def __len__(self):
        print('Step 6: def __len__(self): # Calculating  Total Numbers of Points in Quadtree.')
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
        print('def draw(self, ax):')



