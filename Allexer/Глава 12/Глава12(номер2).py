from math import pi
class Circle:
    def __init__(self,R):
        self.radius=R
    def area(self):
        return (self.radius**2)*pi
circle=Circle(14)
print("S=",circle.area())
