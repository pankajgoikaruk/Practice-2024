import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x  # center x
        self.y = y  # center y
        self.w = w  # half width
        self.h = h  # half height      

    def contains(self, point):
        return (point.x >= self.x - self.w and point.x < self.x + self.w and point.y >= self.y - self.h and point.y < self.y + self.h)
    
    # def intersects(self, range):
    #     return not (range.x - range.w > self.x + self.w or range.x + range.w < self.x - self.w or range.y - range.h > self.y + self.h or range.y + range.h < self.y - self.h)
    

class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary    # rectangle
        self.capacity = capacity    # max number of points in a quadtree, 4 by default.
        self.points = []    # list of points
        self.divided = False    # is the quadtree divided or not?

    def insert(self, point):    # point is a Point object with x and y attributes and we are inserting points into the quadtree.
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:    # if there is space in the quadtree, add the point.
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()
            if self.northeast.insert(point):
                return True
            elif self.northwest.insert(point):
                return True
            elif self.southeast.insert(point):
                return True
            elif self.southwest.insert(point):
                return True

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h

        ne = Rectangle(x + w / 2, y - h / 2, w / 2, h / 2)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(x - w / 2, y - h / 2, w / 2, h / 2)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        self.southwest = QuadTree(sw, self.capacity)

        self.divided = True

    def query(self, range):
        found = []
        if not self.boundary.intersects(range):
            return found
        else:
            for p in self.points:
                if range.contains(p):
                    found.append(p)
            if self.divided:
                found += self.northeast.query(range)
                found += self.northwest.query(range)
                found += self.southeast.query(range)
                found += self.southwest.query(range)
        return found