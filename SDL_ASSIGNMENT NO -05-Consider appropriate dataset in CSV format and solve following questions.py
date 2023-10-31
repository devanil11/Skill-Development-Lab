import math
class Shape:                                            # Shape class with draw, area, and perimeter methods
    def draw(self):
        pass 
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):                                     # Circle class inheriting from Shape
    def __init__(self, radius):
        self.radius = radius
    def draw(self):
        print("Drawing a Circle")       
    def area(self):
        return math.pi * self.radius * self.radius   
    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):                                      # Square class inheriting from Shape
    def __init__(self, side_length):
        self.side_length = side_length
    def draw(self):
        print("Drawing a Square")       
    def area(self):
        return self.side_length * self.side_length    
    def perimeter(self):
        return 4 * self.side_length
# Example usage of the classes
if __name__ == "__main__":
    circle = Circle(7)  # Circle with radius 5
    square = Square(4)   # Square with side length 4
    circle.draw()                                           # Polymorphic behavior: calling draw method of Circle
    print("Area of Circle:", circle.area())
    print("Perimeter of Circle:", circle.perimeter())

    square.draw()                                          # Polymorphic behavior: calling draw method of Square
    print("Area of Square:", square.area())
    print("Perimeter of Square:", square.perimeter())