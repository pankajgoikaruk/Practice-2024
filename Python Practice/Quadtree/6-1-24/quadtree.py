class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height
        self.west = self.center.x - self.width
        self.east = self.center.x + self.width
        self.north = self.center.y + self.height
        self.south = self.center.y - self.height

    def contains_point(self, point):
        return abs(self.west<= point.x < self.east and 
                   self.north <= point.y < self.south)

    def draw(self, ax, c='k', lw=1, **kwargs):
        x1, y1 = self.west, self.north
        x2, y2 = self.east, self.north
        ax.plot([x1, x2, x2, x1], [y1, y1, y2, y2], c=c, lw=lw, **kwargs)

class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self, point):
        if not self.boundary.contains_point(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            return (self.northeast.insert(point) or
                    self.northwest.insert(point) or
                    self.southeast.insert(point) or
                    self.southwest.insert(point))

    def subdivide(self):
        center_x, center_y = self.boundary.center.x, self.boundary.center.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2

        ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height)
        self.southwest = QuadTree(sw, self.capacity)

        self.divided = True

    def draw(self, ax):
        self.boundary.draw(ax)
        if self.divided:
            self.northeast.draw(ax)
            self.northwest.draw(ax)
            self.southeast.draw(ax)
            self.southwest.draw(ax)
