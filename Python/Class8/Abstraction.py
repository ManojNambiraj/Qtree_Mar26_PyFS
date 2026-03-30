# Abstraction:

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

radius = 5
circle = Circle(radius)
print(f"The area of the circle with radius {radius} is: {circle.area()}")

width = 10
height = 5
rectangle = Rectangle(width, height)
print(f"The area of the rectangle with width {width} and height {height} is: {rectangle.area()}")