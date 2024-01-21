import numpy as np
import pandas as pd

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height
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
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)

class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False
        self.nw, self.ne, self.sw, self.se = None, None, None, None
        self.dcrs = {}
        self.id = 1

    def insert(self, point):
        if not self.boundary.contains_points(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            self.add_point_to_dcr(point)
            return True

        if not self.divided:
            self.divide()

        if self.nw.insert(point):
            return True
        elif self.ne.insert(point):
            return True
        elif self.sw.insert(point):
            return True
        elif self.se.insert(point):
            return True

        return False

    def divide(self):
        center_x = self.boundary.center.x
        center_y = self.boundary.center.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2

        nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height)
        self.nw = QuadTree(nw)

        ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height)
        self.ne = QuadTree(ne)

        sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height)
        self.sw = QuadTree(sw)

        se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height)
        self.se = QuadTree(se)

        self.divided = True

    def __len__(self):
        count = len(self.points)
        if self.divided:
            count += len(self.nw) + len(self.ne) + len(self.sw) + len(self.se)
        return count

    def draw(self, ax):
        self.boundary.draw(ax)

        if self.divided:
            self.nw.draw(ax)
            self.ne.draw(ax)
            self.sw.draw(ax)
            self.se.draw(ax)

    def add_point_to_dcr(self, point):
        dcr_name = f'DCR_{self.id}'
        if dcr_name not in self.dcrs:
            self.dcrs[dcr_name] = pd.DataFrame(columns=['x', 'y'])
        self.dcrs[dcr_name] = self.dcrs[dcr_name].append({'x': point.x, 'y': point.y}, ignore_index=True)
