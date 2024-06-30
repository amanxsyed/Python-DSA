import math

class Circle:
    def __init__(self, radius=1):
        self.radius=radius
    
    def area(self):
        return math.pi*self.radius**2

user_radius = float(input("Enter the radius of the circle: "))
user_radius1 = float(input("Enter the radius of the circle: "))

circle = Circle(user_radius)
circle2 = Circle(user_radius1)
print(f"The area of the circle is: {circle.area()}")
print(f"The area of 2nd circle is: {circle2.area()}")