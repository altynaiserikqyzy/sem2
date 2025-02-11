import math 
class Areas():
    def __init__(self , sides , length ):
        self.sides = int(input("Enter the number of sides:"))
        self.length = int(input("Enter the length:"))
    def area(self):
        if self.sides == 4:
            self.area = self.length * self.length
        else:
            self.area = self.length * self.length * self.sides / (4 * math.tan(math.pi / self.sides))
        return self.area
