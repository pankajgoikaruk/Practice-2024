# import libraries.
import numpy as np

class Point:    # Point class with x and y attributes.
    def __init__(self, x, y):   # constructor.
        self.x = x
        self.y = y

class Rectangle:    # Rectangle class with x, y, width, and height attributes.
    def __init__(self, center, width, height):  # constructor.
        self.center = center    # center of rectangle x and y.
        self.width = width      # width of rectangle.
        self.height = height    # height of rectangle.
        self.west = self.center.x - self.width    # west side of rectangle.
        self.east = self.center.x + self.width    # east side of rectangle.
        self.north = self.center.y - self.height  # north side of rectangle.
        self.south = self.center.y + self.height  # south side of rectangle.      

    def containsPoint(self, point):    # returns true if the point is inside the rectangle.
        return (self.west <= point.x < self.east and 
                self.north <= point.y < self.south)
    
    def draw(self, ax, c='k', lw=1, **kwargs):    # draw the rectangle.
        x1, y1 = self.west, self.north
        x2, y2 = self.east, self.south
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)

class QuadTree:    # QuadTree class with boundary, capacity, points, and divided attributes.
    def __init__(self, boundary, capacity):    # constructor.
        self.boundary = boundary    # rectangle
        self.capacity = capacity    # max number of points in a quadtree, 4 by default.
        self.points = []    # list of points
        self.divided = False    # is the quadtree divided or not?

    def insert(self, point):    # point is a Point object with x and y attributes and we are inserting points into the quadtree.
        # if the point is in the range of current quadtree.
        if not self.boundary.containsPoint(point):
            print('point is out of boundary.')
            return False

        # if has not reached capacity, add the point.
        if len(self.points) < self.capacity:    # if there is space in the quadtree, add the point. Points is less than capacity.
            print('capacity: ', self.capacity)
            print('Lenth of points: ', len(self.points))
            self.points.append(point)
            print('point added in the quadtree.')
            return True
        else:
            # Recursive insertion.
            if not self.divided:      # if the quadtree is not divided.
                self.subdivide()      # subdivide the quadtree.

            if self.northeast.insert(point):   # if the point is in the northeast rectangle.
                return True
            elif self.northwest.insert(point):  # if the point is in the northwest rectangle.
                return True
            elif self.southeast.insert(point):  # if the point is in the southeast rectangle.
                return True
            elif self.southwest.insert(point):  # if the point is in the southwest rectangle.
                return True
        
        return False
    
    def subdivide(self):    # subdivide the quadtree into 4 smaller quadtrees.
        # center of the rectangle.
        center_x = self.boundary.center.x
        center_y = self.boundary.center.y
        # half width of the rectangle.
        new_width = self.boundary.width / 2
        # half height of the rectangle.
        new_height = self.boundary.height / 2

        # northeast rectangle.
        ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height)
        self.northeast = QuadTree(ne, self.capacity)
        # northwest rectangle.
        nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height)
        self.northwest = QuadTree(nw, self.capacity)
        # southeast rectangle.
        se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height)
        self.southeast = QuadTree(se, self.capacity)
        # southwest rectangle.
        sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height)
        self.southwest = QuadTree(sw, self.capacity)

        self.divided = True    # set divided to true.
    
    # Check how many points are in the range.
    def __len__(self):
        count = len(self.points)
        if self.divided:
            count += len(self.northeast) + len(self.northwest) + len(self.southeast) + len(self.southwest)
        return count

    # To draw recursively subrectangle in subtree.
    def draw(self, ax):
        self.boundary.draw(ax)
        if self.divided:
            self.northeast.draw(ax)
            self.northwest.draw(ax)
            self.southeast.draw(ax)
            self.southwest.draw(ax)