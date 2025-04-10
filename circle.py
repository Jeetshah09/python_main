import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
circle = Circle(5)  # Create a Circle object with radius 5
print("Area:", circle.area())  # Compute and print the area
print("Perimeter:", circle.perimeter())  # Compute and print the perimeter
