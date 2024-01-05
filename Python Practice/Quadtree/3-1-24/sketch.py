from p5 import background
def setup():
    createCanvas(400, 400)
    background(255)
    stroke(0)
    strokeWeight(1)
    noFill()
    rectMode(CENTER)
    global qtree
    qtree = QuadTree(Rectangle(200, 200, 200, 200), 4)
    for i in range(0, 100):
        p = Point(random(width), random(height))
        qtree.insert(p)
    qtree.show()


def draw():
    background(255)
    qtree.show()
    range = Rectangle(mouseX, mouseY, 50, 50)
    rect(range.x, range.y, range.w * 2, range.h * 2)
    points = qtree.query(range)
    for p in points:
        strokeWeight(4)
        point(p.x, p.y) # noqa: F821


def mousePressed():
    p = Point(mouseX, mouseY)
    qtree.insert(p)
    background(255)
    qtree.show()   