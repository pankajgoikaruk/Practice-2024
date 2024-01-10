import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, center, width, height):
        self.center = center # It contain x and y value of point
        self.width = width
        self.height = height
        # We need four side of rectangle with respect to orignal x and y axis. 
        self.east = center.x + width
        self.west = center.x - width
        self.north = center.y - height
        self.south = center.y + height
    
    def contains_points(self, point):
        return (self.west <= point.x < self.east and 
                self.north <= point.y < self.south)

    def draw(self, ax, c='k', lw=1, **kwargs):
        x1, y1 = self.west, self.north
        x2, y2 = self.east, self.south
        ax.plot([x1,x2,x2,x1,x1], [y1,y1,y2,y2,y1], c=c, lw=lw , **kwargs)


class QuadTree: # It is ractangle pluse capacity
    def __init__(self, boundary, capacity = 50): 
        self.boundary = boundary # initialising the boundaries of Quadtree.
        self.capacity = capacity # initialising the limite of the points in each ractangle. if it will cross thresold we will create new quadtree.

        self.points = [] # Creating a list to store a points.
        self.divided = False # Boolean variable to tell us is quadtree is divided or not?

    def insert(self, point):
        # Check If the point is in the range of current quadtree?
        if not self.boundary.contains_points(point):
            return False
        
        # It means if the quadtree has space to contain the points then let it store.
        if len(self.points) <self.capacity: 
            self.points.append(point)
            return True
        
        # Check if quadtree is not devided then call divide function.
        if not self.divided:
            self.divide()
            
        
        # Insert points inside Recursive quadtree function
        if self.nw.insert(point):
            return True
        elif self.ne.insert(point):
            return True
        elif self.sw.insert(point):
            return True
        elif self.se.insert(point):
            return True
        
        return False
    
    # Create Recursive quadthree function
    def divide(self):
        center_x = self.boundary.center.x # X axix of subdivided rectangle
        center_y = self.boundary.center.y # Y axix of subdivided rectangle
        new_width = self.boundary.width / 2 # Half width of subdivided rectangle
        new_height = self.boundary.height / 2 # Half height of subdivided rectangle

        # Initialise SubRectangle 
        nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height) # North West Side
        self.nw = QuadTree(nw)

        ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height) # North East Side
        self.ne  = QuadTree(ne)

        sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height) # South West Side
        self.sw = QuadTree(sw)

        se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height) # South East Side
        self.se = QuadTree(se)

        self.divided = True

    # Calculate how many points are in quadtree including subtree
    def __len__(self):
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





        

